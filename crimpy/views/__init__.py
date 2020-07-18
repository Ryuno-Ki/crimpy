import os

from .contexts import RootContext


qml_file = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "main.qml")
)
