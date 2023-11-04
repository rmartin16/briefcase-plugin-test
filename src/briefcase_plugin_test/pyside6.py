from briefcase.bootstraps import PySide6GuiBootstrap


class PySide6AutomationBootstrap(PySide6GuiBootstrap):
    def app_source(self):
        return """\
import importlib.metadata
import sys

from PySide6 import QtWidgets
from PySide6.QtCore import QTimer


class {{ cookiecutter.class_name }}(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("{{ cookiecutter.app_name }}")
        self.show()

        QTimer.singleShot(2000, self.exit_app)

    def exit_app(self):
        print(">>> successfully started...exiting <<<")
        print(">>>>>>>>>> EXIT 0 <<<<<<<<<<")
        QtWidgets.QApplication.quit()


def main():
    app_module = sys.modules["__main__"].__package__
    metadata = importlib.metadata.metadata(app_module)

    QtWidgets.QApplication.setApplicationName(metadata["Formal-Name"])

    app = QtWidgets.QApplication(sys.argv)
    main_window = {{ cookiecutter.class_name }}()
    sys.exit(app.exec())
"""

