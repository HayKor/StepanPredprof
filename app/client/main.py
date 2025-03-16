import logging
import sys

from PyQt6.QtWidgets import QApplication
from qt_material import apply_stylesheet
from settings import configure_logging, except_hook

from app.main_window import MainWindow


def main():
    configure_logging(level=logging.DEBUG)

    app = QApplication(sys.argv)
    # See https://pypi.org/project/qt-material/
    apply_stylesheet(app, theme="dark_teal.xml")
    main_window = MainWindow()

    logging.info("App started")

    main_window.show()

    sys.excepthook = except_hook

    exit_code = app.exec()
    logging.info("App exited with code %s", exit_code)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
