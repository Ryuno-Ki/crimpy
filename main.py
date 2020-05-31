import sys

from PySide2.QtCore import Qt, QUrl
from PySide2.QtQuick import QQuickView
from PySide2.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout


class MyWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.text = QLabel("Qt for Python!")
        self.text.setAlignment(Qt.AlignCenter)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text)
        self.setLayout(self.layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = QQuickView()
    url = QUrl("view.qml")

    view.setSource(url)
    view.show()
    # widget = MyWidget()
    # widget.resize(800, 600)
    # widget.show()

    sys.exit(app.exec_())
