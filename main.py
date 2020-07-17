import sys

from PySide2.QtCore import Slot, Qt, QUrl
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
from crimpy.views import MainObject


class MyWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.text = QLabel("Qt for Python!")
        self.text.setAlignment(Qt.AlignCenter)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text)
        self.setLayout(self.layout)

class Form(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("My Form")
        self.edit = QLineEdit("Write my name here...")
        self.button = QPushButton("Show greetings")
        self.button.clicked.connect(self.greetings)

        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def greetings(self):
        print("Hello {}".format(self.edit.text()))

if __name__ == "__main__":
    major = 1
    minor = 0
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    main_object = MainObject()
    engine.rootContext().setContextProperty("main", main_object)
    qmlRegisterType(TwitterModel, 'Twitter', major, minor, 'TwitterModel')
    engine.load(QUrl.fromLocalFile(MainObject.qml_file))
    # view = QQuickView()
    # view.setResizeMode(QQuickView.SizeRootObjectToView)

    # if view.status() == QQuickView.Error:
    #     sys.exit(-1)
    # view.show()

    # button = QPushButton("Click me")
    # button.clicked.connect(log)
    # button.show()

    # form = Form()
    # form.show()
    
    # view = QQuickView()
    # url = QUrl("view.qml")
    # view.setSource(url)
    # view.show()

    # widget = MyWidget()
    # widget.resize(800, 600)
    # widget.show()

    sys.exit(app.exec_())
