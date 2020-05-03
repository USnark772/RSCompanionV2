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

from Model.app_defs import LangEnum
from enum import Enum, auto


class StringsEnum(Enum):
    TITLE = auto()
    STORAGE_ID = auto()
    PERC_FREE = auto()
    GB_FREE = auto()
    MB_FREE = auto()


english = {StringsEnum.TITLE: "Storage Information",
           StringsEnum.STORAGE_ID: 'Storage ID:',
           StringsEnum.PERC_FREE: "Percent free:",
           StringsEnum.GB_FREE: "GB free:",
           StringsEnum.MB_FREE: "MB free:",
           }

# TODO: Verify French version
french = {StringsEnum.TITLE: "Informations de Stockage",
           StringsEnum.STORAGE_ID: 'ID de Stockage:',
           StringsEnum.PERC_FREE: "Pourcentage inutilisé:",
           StringsEnum.GB_FREE: "GB Inutilisé:",
           StringsEnum.MB_FREE: "MB Inutilisé:",
           }

strings = {LangEnum.ENG: english,
           LangEnum.FRE: french}
