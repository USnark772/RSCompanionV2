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

from logging import getLogger, StreamHandler
from asyncio import create_task, sleep
from datetime import datetime, timedelta
from Devices.AbstractDevice.View.base_graph import BaseGraph
from Devices.DRT.Resources.drt_strings import strings, StringsEnum, LangEnum


class DRTGraph(BaseGraph):
    def __init__(self, parent, dev_name: str, log_handlers: [StreamHandler]):
        self._logger = getLogger(__name__)
        for h in log_handlers:
            self._logger.addHandler(h)
        self._logger.debug("Initializing")
        super().__init__(parent, log_handlers)
        self._data = list()
        self._strings = dict()
        self._dev_name = dev_name
        self._logger.debug("Initialized")

    async def show(self) -> None:
        self.set_subplots([x[0] for x in self._data])
        await create_task(self.plot(self.get_new()))

    def clear_graph(self) -> None:
        """
        Clear this graph of any device data.
        :return None:
        """
        for i in range(len(self._data)):
            self._data[i] = [self._data[i][0], [], []]
        self.set_new(True)
        create_task(self.show())

    def set_lang(self, lang: LangEnum) -> None:
        """
        Set this device graph's language.
        :param lang: The lang enum to use.
        :return None:
        """
        self._logger.debug("running")
        super(DRTGraph, self).set_lang(lang)
        self._strings = strings[lang]
        self._change_plot_names([self._strings[StringsEnum.PLOT_NAME_RT], self._strings[StringsEnum.PLOT_NAME_CLICKS]])
        create_task(self.show())
        self._logger.debug("done")

    async def plot_device_data(self, axes, name) -> []:  #, show_in_legend) -> []:
        self._logger.debug("running")
        data = list()
        for x in self._data:
            if x[0] == name:
                data = x
        lines = []
        left = datetime.now()
        right = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        # if show_in_legend:
        #     the_label = self._dev_name
        # else:
        #     the_label = "_nolegend_"
        await sleep(.001)
        line, = axes.plot(data[1], data[2], marker='o')  #, label=the_label)
        await sleep(.001)
        lines.append((self._dev_name, line))
        if len(data[1]) > 0:
            if right < data[1][-1]:
                right = data[1][-1]
            if left > data[1][0]:
                left = data[1][0]
        temp_left = right - timedelta(minutes=2)
        if left < temp_left:
            left = temp_left
        await sleep(.001)
        axes.set_xlim(left=left - timedelta(seconds=10), right=right + timedelta(seconds=10))
        await sleep(.001)
        self._logger.debug("done")
        return lines

    def add_data(self, data: []) -> None:
        """ Ensure data comes in as type, x, y """
        self._logger.debug("running")
        self.set_new(False)
        for item in data:
            for i in range(len(self._data)):
                if item[0] == self._data[i][0]:
                    self._data[i][1].append(item[1])
                    self._data[i][2].append(item[2])
                    break
        create_task(self.plot())
        self._logger.debug("done")

    def add_empty_point(self, timestamp):
        if self.get_new():
            return
        for data in self._data:
            data[1].append(timestamp)
            data[2].append(None)
        self.refresh_self()

    def _change_plot_names(self, names) -> None:
        if len(self._data) == 0:
            for name in names:
                self._data.append([name, [], []])
        else:
            for i in range(len(names)):
                self._data[i][0] = names[i]
