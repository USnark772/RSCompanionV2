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
    COMPANY_NAME = auto()
    APP_NAME = auto()
    PROG_OUT_HDR = auto()
    LOG_VER_ID = auto()
    ABOUT_COMPANY = auto()
    ABOUT_APP = auto()
    UPDATE_AVAILABLE = auto()
    NO_UPDATE = auto()
    ERR_UPDATE_CHECK = auto()
    DEV_CON_ERR = auto()
    LOG_OUT_NAME = auto()
    RESTART_PROG = auto()
    UPDATE_HDR = auto()
    UPDATE_HDR_ERR = auto()


company_name = "Red Scientific"
app_name = "RS Companion"
log_out_filename = "companion_app_log.txt"


english = {StringsEnum.COMPANY_NAME: company_name,
           StringsEnum.APP_NAME: app_name,
           StringsEnum.LOG_OUT_NAME: log_out_filename,
           StringsEnum.LOG_VER_ID: company_name + " app version: ",
           StringsEnum.PROG_OUT_HDR: "Timestamp, Author, Location, Message\n",
           StringsEnum.ABOUT_COMPANY: company_name + " Inc was founded in 2015 by Joel Cooper PhD\n\n"
                                                     " Contact Information:\n"
                                                     " joel@redscientific.com\n"
                                                     " 1-801-520-5408",
           StringsEnum.ABOUT_APP: "- Most things in this app have tooltips. Mouse over different parts to see"
                                  " respective tooltips for more information\n\n"
                                  " Along the top of the app you will find a control bar containing the following:\n"
                                  " - Create/End button: Create or end an experiment. Choose a location folder for the"
                                  " app to save device data.\n"
                                  " - Play/Pause button: Begin/resume or pause an experiment in progress.\n"
                                  " - Optional condition name: An optional name that will be associated with the newly"
                                  " created experiment.\n\n"
                                  " - Key Flag: Press a letter key at any time to make a quick reference key that will"
                                  " be associated with the data coming in from the Devices during an experiment.\n\n"
                                  " - Note: Enter a note into the box and press Post to apply that note to all device"
                                  " data files within the current experiment.\n\n"
                                  " - Information: Displays information in regards to the current experiment.\n\n"
                                  " - Drive Info: Displays information in regards to the current volume where data is"
                                  " being saved to.",
           StringsEnum.UPDATE_HDR: "Update",
           StringsEnum.UPDATE_HDR_ERR: "Error",
           StringsEnum.UPDATE_AVAILABLE: "An update is available.",
           StringsEnum.NO_UPDATE: "Your program is up to date.",
           StringsEnum.ERR_UPDATE_CHECK: "There was an unexpected error connecting to the repository. Please check"
                                         " https://redscientific.com/downloads.html manually or contact Red Scientific"
                                         " directly.",
           StringsEnum.DEV_CON_ERR: "There was a problem connecting the device, please retry connection.",
           StringsEnum.RESTART_PROG: "This app must restart for changes to take effect."
           }

# TODO: Verify French
french = {StringsEnum.COMPANY_NAME: company_name,
          StringsEnum.APP_NAME: app_name,
          StringsEnum.LOG_OUT_NAME: log_out_filename,
          StringsEnum.LOG_VER_ID: company_name + " Version de l'application: ",
          StringsEnum.PROG_OUT_HDR: "Horodatage, Auteur, Emplacement, Message\n",
          StringsEnum.ABOUT_COMPANY: company_name + " Inc a été fondée en 2015 par Joel Cooper PhD\n\n"
                                                    " Informations de contact:\n"
                                                    " joel@redscientific.com\n"
                                                    " 1-801-520-5408",
          StringsEnum.ABOUT_APP: "- La plupart des éléments de cette application comportent des info-bulles."
                                 " Passez la souris sur différentes parties pour voir les info-bulles respectives"
                                 " pour plus d'informations.\n\n"
                                 " En haut de l'application, vous trouverez une barre de contrôle contenant les"
                                 " éléments suivants:\n"
                                 " - Bouton Créer/Fin: créez ou terminez une expérience. Choisissez un dossier"
                                 " d'emplacement pour l'application pour enregistrer les données de l'appareil.\n"
                                 " - Bouton Lecture / Pause: commence / reprend ou suspend une expérience en cours.\n"
                                 " - Nom de condition facultatif: nom facultatif qui sera associé à la nouvelle"
                                 " expérience créée.\n\n"
                                 " - Indicateur de touche: appuyez sur une touche de lettre à tout moment pour créer"
                                 " une touche de référence rapide qui sera associée aux données provenant des"
                                 " appareils pendant une expérience.\n\n"
                                 " - Remarque: entrez une note dans la case et appuyez sur Publier pour appliquer"
                                 " cette note à tous les fichiers de données de l'appareil dans l'expérience"
                                 " en cours.\n\n"
                                 " - Informations: affiche des informations concernant l'expérience en cours.\n\n"
                                 " - Informations sur le lecteur: affiche des informations concernant le volume"
                                 " actuel sur lequel les données sont enregistrées.",
          StringsEnum.UPDATE_HDR: "Mise à jour",
          StringsEnum.UPDATE_HDR_ERR: "Erreur",
          StringsEnum.UPDATE_AVAILABLE: "Une mise à jour est disponible.",
          StringsEnum.NO_UPDATE: "Votre programme est à jour.",
          StringsEnum.ERR_UPDATE_CHECK: "Une erreur inattendue s'est produite lors de la connexion au référentiel."
                                        " Veuillez vérifier https://redscientific.com/downloads.html manuellement"
                                        " ou contacter directement Red Scientific.",
          StringsEnum.DEV_CON_ERR: "Un problème est survenu lors de la connexion de l'appareil. Veuillez réessayer.",
          StringsEnum.RESTART_PROG: "Cette application doit redémarrer pour que les modifications prennent effet."
          }

# TODO: verify German
german = {StringsEnum.COMPANY_NAME: company_name,
          StringsEnum.APP_NAME: app_name,
          StringsEnum.LOG_OUT_NAME: log_out_filename,
          StringsEnum.LOG_VER_ID: company_name + " app version: ",
          StringsEnum.PROG_OUT_HDR: "Zeitstempel, Autor, Standort, Nachricht\n",
          StringsEnum.ABOUT_COMPANY: company_name + " Inc wurde 2015 von Joel Cooper PhD gegründet\n\n"
                                                    " Kontakt Informationen:\n"
                                                    " joel@redscientific.com\n"
                                                    " 1-801-520-5408",
          StringsEnum.ABOUT_APP: "- Die meisten Dinge in dieser App haben Tooltips. Fahren Sie mit der Maus über"
                                 " verschiedene Teile, um die entsprechenden QuickInfos für weitere Informationen"
                                 " anzuzeigen\n\n"
                                 " Am oberen Rand der App finden Sie eine Steuerleiste mit den folgenden Angaben:\n"
                                 " - Schaltfläche Erstellen/Beenden: Erstellen oder beenden Sie ein Experiment."
                                 " Wählen Sie einen Speicherortordner für die App, um Gerätedaten zu speichern.\n"
                                 " - Schaltfläche Abspielen/Unterbrechen: Starten/Fortsetzen oder Unterbrechen eines"
                                 " laufenden Experiments.\n"
                                 " - Optionaler Bedingungsname: Ein optionaler Name, der dem neu erstellten Experiment"
                                 " zugeordnet wird.\n\n"
                                 " - Schlüsselflagge: Drücken Sie jederzeit eine Buchstabentaste, um eine"
                                 " Kurzreferenztaste zu erstellen, die den Daten zugeordnet wird, die während eines"
                                 " Experiments von den Geräten eingehen.\n\n"
                                 " - Notiz: Geben Sie eine Notiz in das Feld ein und drücken Sie Posten, um diese"
                                 " Notiz auf alle Gerätedatendateien im aktuellen Experiment anzuwenden.\n\n"
                                 " - Information: Zeigt Informationen zum aktuellen Experiment an.\n\n"
                                 " - Laufwerksinformationen: Zeigt Informationen zum aktuellen Volume an, auf dem"
                                 " Daten gespeichert werden.",
          StringsEnum.UPDATE_HDR: "Aktualisieren",
          StringsEnum.UPDATE_HDR_ERR: "Error",
          StringsEnum.UPDATE_AVAILABLE: "Eine Aktualisierung ist verfügbar.",
          StringsEnum.NO_UPDATE: "Ihr Programm ist auf dem neuesten Stand.",
          StringsEnum.ERR_UPDATE_CHECK: "Beim Herstellen einer Verbindung zum Repository ist ein unerwarteter Fehler"
                                        " aufgetreten. Bitte überprüfen Sie https://redscientific.com/downloads.html"
                                        " manuell oder wenden Sie sich direkt an Red Scientific.",
          StringsEnum.DEV_CON_ERR: "Beim Anschließen des Geräts ist ein Problem aufgetreten. Versuchen Sie erneut,"
                                   " die Verbindung herzustellen.",
          StringsEnum.RESTART_PROG: "Diese App muss neu gestartet werden, damit die Änderungen wirksam werden."
          }

# TODO: verify Spanish
spanish = {StringsEnum.COMPANY_NAME: company_name,
           StringsEnum.APP_NAME: app_name,
           StringsEnum.LOG_OUT_NAME: log_out_filename,
           StringsEnum.LOG_VER_ID: company_name + " version de aplicacion: ",
           StringsEnum.PROG_OUT_HDR: "Marca de tiempo, Autor, Ubicación, Mensaje\n",
           StringsEnum.ABOUT_COMPANY: company_name + " Inc fue fundada en 2015 por Joel Cooper PhD\n\n"
                                                     " Información del contacto:\n"
                                                     " joel@redscientific.com\n"
                                                     " 1-801-520-5408",
           StringsEnum.ABOUT_APP: "- La mayoría de las cosas en esta aplicación tienen información sobre herramientas."
                                  " Pase el mouse sobre diferentes partes para ver la información sobre herramientas"
                                  " respectiva para obtener más información.\n\n"
                                  " En la parte superior de la aplicación, encontrará una barra de control"
                                  " que contiene lo siguiente:\n"
                                  " - Botón Crear/Finalizar: Crea o finaliza un experimento. Elija una carpeta de"
                                  " ubicación para que la aplicación guarde los datos del dispositivo.\n"
                                  " - Botón Reproducir/Pausa: Comience / reanude o pause un experimento en progreso.\n"
                                  " - Nombre de condición opcional: Un nombre opcional que se asociará con el"
                                  " experimento recién creado.\n\n"
                                  " - Bandera clave: Presione una tecla de letra en cualquier momento para crear"
                                  " una tecla de referencia rápida que se asociará con los datos provenientes"
                                  " de los Dispositivos durante un experimento.\n\n"
                                  " - Nota: Ingrese una nota en el cuadro y presione Publicar para aplicar esa nota a"
                                  " todos los archivos de datos del dispositivo dentro del experimento actual.\n\n"
                                  " - Información: Muestra información sobre el experimento actual.\n\n"
                                  " - Información de la unidad: Muestra información sobre el volumen actual donde"
                                  " se guardan los datos.",
           StringsEnum.UPDATE_HDR: "Actualizar",
           StringsEnum.UPDATE_HDR_ERR: "Error",
           StringsEnum.UPDATE_AVAILABLE: "Hay una actualización disponible.",
           StringsEnum.NO_UPDATE: "Tu programa está actualizado.",
           StringsEnum.ERR_UPDATE_CHECK: "Hubo un error inesperado al conectarse al repositorio."
                                         " Consulte https://redscientific.com/downloads.html manualmente o comuníquese"
                                         " directamente con Red Scientific.",
           StringsEnum.DEV_CON_ERR: "Hubo un problema al conectar el dispositivo. Vuelva a intentar la conexión.",
           StringsEnum.RESTART_PROG: "Esta aplicación debe reiniciarse para que los cambios surtan efecto."
           }

# TODO: Verify Chinese (simplified)
chinese = {StringsEnum.COMPANY_NAME: company_name,
           StringsEnum.APP_NAME: app_name,
           StringsEnum.LOG_OUT_NAME: log_out_filename,
           StringsEnum.LOG_VER_ID: company_name + " 应用版本: ",
           StringsEnum.PROG_OUT_HDR: "时间戳记, 作者, 位置, 信息\n",
           StringsEnum.ABOUT_COMPANY: company_name + " Inc 由Joel Cooper PhD于2015年创立\n\n"
                                                     " 联系信息:\n"
                                                     " joel@redscientific.com\n"
                                                     " 1-801-520-5408",
           StringsEnum.ABOUT_APP: "- 此应用程序中的大多数内容都有工具提示。"
                                  " 将鼠标移到不同的部分上可以查看相应的工具提示，以获取更多信息\n\n"
                                  " 在应用程序顶部，您将找到一个包含以下内容的控制栏:\n"
                                  " - 创建/结束按钮: 创建或结束实验。 选择应用程序的位置文件夹以保存设备数据。\n"
                                  " - 播放/暂停按钮: 开始/继续或暂停正在进行的实验。\n"
                                  " - 可选条件名称: 与新创建的实验相关联的可选名称。\n\n"
                                  " - 钥匙旗: 随时按字母键以创建快速参考键，该参考键将与实验期间从设备输入的数据相关联。\n\n"
                                  " - 注意: 在框中输入注释，然后按发布以将该注释应用于当前实验中的所有设备数据文件。\n\n"
                                  " - 信息: 显示有关当前实验的信息。\n\n"
                                  " - 驱动器信息: 显示有关将数据保存到的当前卷的信息。",
           StringsEnum.UPDATE_HDR: "更新资料",
           StringsEnum.UPDATE_HDR_ERR: "错误",
           StringsEnum.UPDATE_AVAILABLE: "有可用的更新。",
           StringsEnum.NO_UPDATE: "您的程序是最新的。",
           StringsEnum.ERR_UPDATE_CHECK: "连接到存储库时发生意外错误。 请手动检查"
                                         "https://redscientific.com/downloads.html或直接联系Red Scientific。",
           StringsEnum.DEV_CON_ERR: "连接设备时出现问题，请重试连接。",
           StringsEnum.RESTART_PROG: "此应用必须重新启动才能使更改生效。"
           }

strings = {LangEnum.ENG: english,
           LangEnum.FRE: french,
           LangEnum.GER: german,
           LangEnum.SPA: spanish,
           LangEnum.CHI: chinese}
