import logging
import os

def configure_logging(
    level=None,
    log_file=None
):
    level = level or os.getenv("LOG_LEVEL", "INFO")
    handlers = [logging.StreamHandler()]
    
    if log_file:
        handlers.append(logging.FileHandler(log_file))
    
    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format='%(asctime)s - %(levelname)s - %(funcName)s - %(message)s',
        datefmt='%Y-%m-%dT%H:%M:%S',
        handlers=handlers
    )

configure_logging(log_file="app.log")
info = logging.info
warning = logging.warning
error = logging.error
critical = logging.critical
exception = logging.exception
