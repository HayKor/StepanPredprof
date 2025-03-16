import logging

from PyQt6.QtWidgets import QWidget

from app.ui.main_widget_ui import Ui_MainWidget


class MainWidget(QWidget, Ui_MainWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        logging.debug("Widget '%s' has initialized", self.__class__.__name__)
