import sys

from PySide2.QtCore import Slot, Qt, QUrl
from PySide2.QtQuick import QQuickView
from PySide2.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget


@Slot()
def log():
    print("Button clicked")

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

    button = QPushButton("Click me")
    button.clicked.connect(log)
    button.show()
    
    # view = QQuickView()
    # url = QUrl("view.qml")
    # view.setSource(url)
    # view.show()

    # widget = MyWidget()
    # widget.resize(800, 600)
    # widget.show()

    sys.exit(app.exec_())
