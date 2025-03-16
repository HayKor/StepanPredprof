import logging


def configure_logging(level) -> None:
    logging.basicConfig(
        level=level,
        format="%(asctime)s   %(name)-25s %(levelname)-8s %(message)s",
    )
