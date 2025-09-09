import logging
import sys
from logging.handlers import RotatingFileHandler

formatter = logging.Formatter(
    "%(asctime)s [%(levelname)s] %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

def get_logger(name):
    logger = logging.getLogger(name)
    # To avoid duplicate loggers: GPT suggested
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)
    return logger

def get_prod_logger(name):
    logger = logging.getLogger(name)
    # To avoid duplicate loggers: GPT suggested
    if not logger.handlers:
        handler = RotatingFileHandler(
            "project-album.log", maxBytes=5_000_000, backupCount=3
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger