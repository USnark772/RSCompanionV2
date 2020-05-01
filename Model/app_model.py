"""
Licensed under GNU GPL-3.0-or-later

This file is part of RS Companion.

RS Companion is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

RS Companion is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with RS Companion.  If not, see <https://www.gnu.org/licenses/>.

Author: Phillip Riskin
Author: Nathan Rogers
Date: 2020
Project: Companion App
Company: Red Scientific
https://redscientific.com/index.html
"""

import os
import glob
import importlib.util
from logging import StreamHandler, getLogger
from asyncio import gather, Event, create_task
from aioserial import AioSerial
from PySide2.QtWidgets import QMdiArea
from Model.rs_device_com_scanner import RSDeviceCommScanner
from Model.app_defs import LangEnum
from Devices.AbstractDevice.View.abstract_view import AbstractView


# TODO: Figure out close_flag. How to remove views?
class AppModel(RSDeviceCommScanner):
    def __init__(self, view_parent: QMdiArea, ch: StreamHandler):

        self._profiles = self.get_profiles()
        self._controllers = self.get_controllers()
        super().__init__(self._profiles)

        self._logger = getLogger(__name__)
        self._logger.addHandler(ch)
        self._logger.debug("Initializing")
        self._ch = ch
        self._view_parent = view_parent
        self._new_dev_view_flag = Event()
        self._remove_dev_view_flag = Event()
        self._devs = dict()
        self._dev_inits = dict()
        self._new_dev_views = []
        self._remove_dev_views = []
        self._tasks = []
        self._logger.debug("Initialized")

    def com_event_error(self):
        """
        Handles com errors.
        :return: None.
        """
        print("A COM ERROR HAS OCCURRED!")

    def com_event_connect(self):
        """
        Get new device info from new device queue and make new device.
        :return: None.
        """
        while not self.com_new_q.empty():
            dev_type, connection = self.com_new_q.get()
            self._make_device(dev_type, connection)

        self._logger.debug("done")

    def com_event_remove(self):
        """
        Remove lost devices.
        :return: None.
        """
        while not self.com_remove_q.empty():
            to_remove = None
            dev_conn = self.com_remove_q.get()
            for key in self._devs:
                if self._devs[key].get_conn().port == dev_conn.device:
                    self._remove_dev_views.append(self._devs[key].get_view())
                    self._devs[key].cleanup()
                    to_remove = key
                    self._remove_dev_view_flag.set()
            if to_remove:
                del self._devs[to_remove]

    def set_lang(self, lang: LangEnum) -> None:
        """
        Set language in each device controller.
        :param lang: The enum for the language.
        :return: None.
        """
        for controller in self._devs.values():
            controller.set_lang(lang)

    def get_next_new_view(self) -> AbstractView:
        """
        :return AbstractView: The next unhandled new view
        """
        if self.has_unhandled_new_views():
            return self._new_dev_views.pop(0)

    def has_unhandled_new_views(self) -> bool:
        """
        :return bool: Whether or not there are new views to add.
        """
        return len(self._new_dev_views) > 0

    def get_next_view_to_remove(self) -> AbstractView:
        """
        :return AbstractView: The next unhandled view to remove.
        """
        if self.has_unhandled_views_to_remove():
            return self._remove_dev_views.pop(0)

    def has_unhandled_views_to_remove(self) -> bool:
        """
        :return bool: Whether or not there are unhandled views to remove.
        """
        return len(self._remove_dev_views) > 0

    def signal_create_exp(self) -> bool:
        """
        Call create_exp on all device controllers.
        :return bool: If there was an error.
        """
        self._logger.debug("running")
        devices_running = list()
        try:
            for controller in self._devs.values():
                controller.create_exp()
                devices_running.append(controller)
            self._logger.debug("done")
            return True
        except Exception as e:
            self._logger.exception("Failed creating exp on a controller.")
            for controller in devices_running:
                controller.end_exp()
            return False

    def signal_end_exp(self) -> bool:
        """
        Call end exp on all device controllers.
        :return bool: If there was an error.
        """
        self._logger.debug("running")
        try:
            for controller in self._devs.values():
                controller.end_exp()
            self._logger.debug("done")
            return True
        except Exception as e:
            self._logger.exception("Failed ending exp on a controller.")
            return False

    def signal_start_exp(self) -> bool:
        """
        Starts an experiment.
        :return bool: Return false if an experiment failed to start, otherwise return true.
        """
        self._logger.debug("running")
        devices = list()
        try:
            for controller in self._devs.values():
                controller.start_exp()
                devices.append(controller)
                return True
        except Exception as e:
            self._logger.exception("Failed trying to start exp on controller.")
            for controller in devices:
                controller.end_exp()
                return False

    def signal_stop_exp(self) -> bool:
        """
        Stops an experiment.
        :return bool: Return false if an experiment failed to stop, otherwise return true.
        """
        self._logger.debug("running")
        try:
            for controller in self._devs.values():
                controller.stop_exp()
            return True
        except Exception as e:
            self._logger.exception("Failed trying to stop exp on controller")
            return False

    def _make_device(self, dev_type: str, conn: AioSerial) -> None:
        """
        Make new controller for dev_type.
        :param dev_type: The type of device.
        :param conn: The device connection.
        :return None:
        """
        self._logger.debug("running")
        if dev_type not in self._controllers.keys():
            self._logger.warning("Could not recognize device type")
            return
        ret = self._make_controller(conn, dev_type)
        if not ret:
            self._logger.warning("Failed making controller for type: " + dev_type)
            return
        self._logger.debug("done")

    def _make_controller(self, conn: AioSerial, dev_type) -> bool:
        """
        Create controller of type dev_type
        :param conn:
        :param dev_type:
        :return:
        """
        self._logger.debug("running")
        ret = True
        try:
            controller = self._controllers[dev_type](conn, self._view_parent, LangEnum.ENG, self._ch)
            self._devs[conn.port] = controller
            self._new_dev_views.append(controller.get_view())
            self._new_dev_view_flag.set()
        except Exception as e:
            self._logger.exception("Problem making controller")
            ret = False
        self._logger.debug("done")
        return ret

    def start(self):
        self._logger.debug("running")
        self.com_start()
        self._logger.debug("done")

    def cleanup(self):
        self._logger.debug("running")
        self.com_cleanup()
        for dev in self._devs.values():
            dev.cleanup()
        create_task(self.end_tasks())
        self._logger.debug("done")

    async def end_tasks(self):
        for task in self._tasks:
            task.cancel()
            await gather(self._tasks)

    # TODO add debugging
    @staticmethod
    def get_profiles():
        profs = {}
        for device in os.listdir('Devices'):
            if device != "AbstractDevice":
                fpath = glob.glob("Devices/" + device + "/Model/*defs.py")
                if fpath:
                    spec = importlib.util.spec_from_file_location("stuff", fpath[0])
                    mod = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(mod)
                    profs.update(mod.profile)
        return profs

    # TODO add debugging
    @staticmethod
    def get_controllers():
        controllers = {}
        for device in os.listdir('Devices'):
            if device != "AbstractDevice":
                fpath = glob.glob("Devices/" + device + "/Controller/*controller.py")
                if fpath:
                    spec = importlib.util.spec_from_file_location(device, fpath[0])
                    mod = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(mod)
                    controllers.update({device: mod.Controller})
        return controllers
