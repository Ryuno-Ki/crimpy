from PySide2.QtCore import (
    Property,
    QObject,
    Signal,
    Slot
)
from PySide2.QtGui import QGuiApplication

from crimpy import __version__ as app_version


class RootContext(QObject):
    language_changed = Signal(str)
    broadcast_language_changed = Signal(str)

    def __init__(self):
        super().__init__()

        self.language_changed.connect(self.select_language)

    def get_version(self):
        return "Version {}".format(app_version)

    @Slot()
    def select_language(self, language):
        if language == "de":
           self.broadcast_language_changed.emit(language)
        else:
           self.broadcast_language_changed.emit("en")

    versionChanged = Signal(str)

    version = Property(
        str,
        get_version,
        notify=versionChanged
    )
