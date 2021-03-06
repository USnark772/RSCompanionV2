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
    FLAG_TT = auto()


english = {StringsEnum.TITLE: "Key Flag",
           StringsEnum.FLAG_TT: "The most recent key pressed for reference in save file",
           }

# TODO: Verify French
french = {StringsEnum.TITLE: "Drapeau clé",
          StringsEnum.FLAG_TT: "La touche la plus récente appuyée pour référence dans le fichier de sauvegarde",
          }

# TODO: Verify German
german = {StringsEnum.TITLE: "Schlüsselflagge",
          StringsEnum.FLAG_TT: "Die zuletzt als Referenz in der Sicherungsdatei gedrückte Taste",
          }

# TODO: Verify Spanish
spanish = {StringsEnum.TITLE: "Bandera clave",
           StringsEnum.FLAG_TT: "La tecla más reciente presionada para referencia en guardar archivo",
           }

# TODO: Verify Chinese (simplified)
chinese = {StringsEnum.TITLE: "钥匙旗",
           StringsEnum.FLAG_TT: "在保存文件中按下以供参考的最新键",
           }

strings = {LangEnum.ENG: english,
           LangEnum.FRE: french,
           LangEnum.GER: german,
           LangEnum.SPA: spanish,
           LangEnum.CHI: chinese}
