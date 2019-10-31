import json
import logging
import os
import datetime


class LogFilter(logging.Filter):
    def filter(self, record):
        env = os.getenv("ENV", "dev")
        record.application = f"dc-broadcast-ingest-worker-{env}"
        return True


class LogHandler(logging.StreamHandler):
    def __init__(self):
        self.remove_existing_handlers()
        super().__init__()
        self.formatter = self.set_formatter()
        self.addFilter(LogFilter())

    def set_formatter(self):
        return logging.Formatter(
            "%(asctime)s | %(application)s | module=%(name)s  | level=%(levelname)s | msg=%(message)s"
        )

    def remove_existing_handlers(self):
        logger = logging.getLogger()
        if logging.getLogger().handlers:
            for handler in logger.handlers:
                logger.removeHandler(handler)


def set_log_config():
    logger = logging.getLogger()
    logger_handler = LogHandler()
    logger.addHandler(logger_handler)
    logger.setLevel(logging.INFO)
    logging.getLogger("boto3").setLevel(logging.CRITICAL)
    logging.getLogger("botocore").setLevel(logging.CRITICAL)
    logging.getLogger("nose").setLevel(logging.CRITICAL)
