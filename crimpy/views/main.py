from PySide2.QtCore import Slot
from PySide2.QtWidgets import QAction, QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(self._get_translation("window.title"))
        self._build_menu()

    @Slot()
    def exit_app(self, checked):
        QApplication.quit()

    def _build_menu(self):
        self.menu = self.menuBar()
        self._build_file_menu()

    def _build_file_menu(self):
        self.file_menu = self.menu.addMenu(self._get_translation("menu.file"))
        self._build_exit_action()

    def _build_exit_action(self):
        exit_action = QAction(self._get_translation("action.exit"), self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.exit_app)
        self.file_menu.addAction(exit_action)

    def _get_translation(self, key):
        translations = {
            "action.exit": "Exit",
            "menu.file": "File",
            "window.title": "Tutorial"
        }
        return translations[key] if key in translations else ""