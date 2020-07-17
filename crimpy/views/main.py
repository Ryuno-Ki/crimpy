import os

from PySide2.QtCore import Property, QObject, Signal, Slot

from crimpy import __version__ as app_version


class MainObject(QObject):
    qml_file = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "main.qml")
    )

    def __init__(self):
        super().__init__()
        # self._build_menu()

    def get_exit_label(self):
        return self.__get_translation("action.exit")

    def get_help_menu_label(self):
        return self.__get_translation("menu.help")

    def get_version(self):
        return "Version {}".format(app_version)

    exitLabelChanged = Signal(str)
    helpMenuLabelChanged = Signal(str)
    versionChanged = Signal(str)

    exit_label = Property(
        str,
        get_exit_label,
        notify=exitLabelChanged
    )

    help_menu_label = Property(
        str,
        get_help_menu_label,
        notify=helpMenuLabelChanged
    )

    version = Property(
        str,
        get_version,
        notify=versionChanged
    )

    def __get_translation(self, key):
        translations = {
            "action.exit": "Exit",
            "action.version": "Version",
            "menu.file": "File",
            "menu.help": "Help",
            "window.title": "Tutorial"
        }
        return translations[key] if key in translations else ""
