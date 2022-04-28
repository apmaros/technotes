import logging


def set_logger(log_level):
    logging.root.setLevel(log_level)
    logging.basicConfig(format='%(levelname)s:%(message)s', level=log_level)
