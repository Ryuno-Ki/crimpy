import os
import sys

from PySide2.QtCore import Slot, QLocale, Qt, QTranslator, QUrl
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine, qmlRegisterType
from PySide2.QtQuick import QQuickView
from PySide2.QtWidgets import (
    QDialog,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget
)

from crimpy.models import TwitterModel
from crimpy.views import RootContext, qml_file

class MainApplication(QGuiApplication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__setup()
        self.__register_event_listeners()

        if not self.__engine.rootObjects():
            sys.exit(-1)

    @Slot()
    def language_changed(self, language):
        print('Language changed to {}'.format(language))
        if language == "de":
            translation_file_path = os.path.join(
                self.translation_directory,
                "crimpy_de.qm"
            )
            print("Installing {}".format(translation_file_path))
            self.__de_translator.load(translation_file_path)
            self.installTranslator(self.__de_translator)
        else:
            self.removeTranslator(self.__de_translator)
        self.__engine.retranslate()

    def __setup(self):
        self.__current_language = QLocale.system().name()
        self.__de_translator = QTranslator()

        self.translation_directory = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "crimpy", "languages")
        )

        self.__engine = QQmlApplicationEngine()
        self.__root_context = RootContext()
        self.__engine.rootContext().setContextProperty("main", self.__root_context)
        qmlRegisterType(TwitterModel, 'Twitter', major, minor, 'TwitterModel')
        self.__engine.load(QUrl.fromLocalFile(qml_file))

    def __register_event_listeners(self):
        self.__root_context.broadcast_language_changed.connect(self.language_changed)

if __name__ == "__main__":
    major = 1
    minor = 0
    app = MainApplication(sys.argv)
    sys.exit(app.exec_())
