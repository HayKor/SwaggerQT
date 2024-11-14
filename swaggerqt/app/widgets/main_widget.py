import logging

from app.ui.main_window_ui import Ui_MainWindow
from app.widgets.generate_yaml import GenerateYAML
from models.parsing import JsonParser
from PyQt6.QtWidgets import QWidget


class MainWidget(QWidget, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.parser = JsonParser()
        self.generate_yaml_window = GenerateYAML()
        self.generate_yaml_btn.clicked.connect(self.on_click_generate_yaml)

        logging.debug("Widget '%s' has initialized", self.__class__.__name__)

    def on_click_generate_yaml(self):
        self.generate_yaml_window.show()