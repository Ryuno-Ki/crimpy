from PySide2.QtCore import Slot
from PySide2.QtWidgets import (
    QAction,
    QApplication,
    QMessageBox,
    QMainWindow,
    QPushButton,
    QVBoxLayout
)

from crimpy import __version__ as app_version


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(self._get_translation("window.title"))
        self._build_menu()

    @Slot()
    def exit_app(self, checked):
        QApplication.quit()

    @Slot()
    def show_version(self):
        version = QMessageBox()
        version.setText("Version {}".format(app_version))
        version.exec_()

    def _build_menu(self):
        self.menu = self.menuBar()
        self._build_file_menu()
        self._build_help_menu()

    def _build_file_menu(self):
        self.file_menu = self.menu.addMenu(self._get_translation("menu.file"))
        self._build_exit_action()

    def _build_help_menu(self):
        self.help_menu = self.menu.addMenu(self._get_translation("menu.help"))
        self._build_version_action()

    def _build_exit_action(self):
        exit_action = QAction(self._get_translation("action.exit"), self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.exit_app)
        self.file_menu.addAction(exit_action)

    def _build_version_action(self):
        version_action = QAction(self._get_translation("action.version"), self)
        version_action.setShortcut("?")
        version_action.triggered.connect(self.show_version)
        self.help_menu.addAction(version_action)

    def _get_translation(self, key):
        translations = {
            "action.exit": "Exit",
            "action.version": "Version",
            "menu.file": "File",
            "menu.help": "Help",
            "window.title": "Tutorial"
        }
        return translations[key] if key in translations else ""