import logging

from PyQt6.QtWidgets import QMainWindow

from app.widgets.main_widget import MainWidget


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("PyQT Swagger Builder")

        main_widget = MainWidget()
        self.setCentralWidget(main_widget)

        logging.debug("Window '%s' has initialized", self.__class__.__name__)
