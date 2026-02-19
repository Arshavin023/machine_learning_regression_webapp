import logging
import json
import sys


class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "level": record.levelname,
            "message": record.getMessage(),
            "time": self.formatTime(record, self.datefmt),
            "module": record.module,
        }
        return json.dumps(log_record)


logger = logging.getLogger()
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(JsonFormatter())

logger.addHandler(handler)
logger.setLevel(logging.INFO)
