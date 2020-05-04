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
Date: 2020
Project: Companion App
Company: Red Scientific
https://redscientific.com/index.html
"""

from logging import getLogger, DEBUG
from abc import ABC, abstractmethod
from Model.app_defs import LangEnum
from aioserial import AioSerial
from Devices.AbstractDevice.View.abstract_view import AbstractView


# TODO: remove print statements at release.
class AbstractController(ABC):
    def __init__(self, view):
        super().__init__()
        self.view = view
        self._debugging = (getLogger(__name__).getEffectiveLevel() == DEBUG)

    def get_view(self) -> AbstractView:
        """
        :return AbstractView: This device's view object.
        """
        return self.view

    @abstractmethod
    def cleanup(self) -> None:
        """
        Handle cleanup and shut down of this code.
        :return: None.
        """
        pass

    @abstractmethod
    def set_output_path(self, path: str) -> None:
        """
        Set the output path for this device to save data to.
        :param path: The path to save data to.
        :return None:
        """
        pass

    def get_conn(self) -> AioSerial:
        """
        Return this device's com port if it exists.
        :return: This device's com port.
        """
        pass

    def set_lang(self, lang: LangEnum) -> None:
        """
        Set this device's view language.
        :param lang: The enum for the language.
        :return: None.
        """
        if self._debugging:
            print(__name__, "Got new language to use:", lang)
        pass

    def create_exp(self) -> None:
        """
        Logic for if this device needs to know about when an experiment is created.
        :return: None.
        """
        if self._debugging:
            print(__name__, "Got create signal, creating.")
        pass

    def end_exp(self) -> None:
        """
        Logic for if this device needs to know about when an experiment is ended.
        :return: None.
        """
        if self._debugging:
            print(__name__, "Got end signal, ending.")
        pass

    def start_exp(self) -> None:
        """
        Logic for if this device needs to know about when an experiment is running.
        :return: None.
        """
        if self._debugging:
            print(__name__, "Got start signal, starting.")
        pass

    def stop_exp(self) -> None:
        """
        Logic for if this device needs to know about when an experiment is stopped.
        :return: None.
        """
        if self._debugging:
            print(__name__, "Got stop signal, stopping.")
        pass
