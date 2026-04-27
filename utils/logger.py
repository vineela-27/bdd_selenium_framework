import logging
import os
from datetime import datetime

def get_logger(name="test_logger"):
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)

    log_file = f"{log_dir}/test_{datetime.now().strftime('%Y-%m-%d')}.log"

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        fh = logging.FileHandler(log_file)
        ch = logging.StreamHandler()

        formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        logger.addHandler(fh)
        logger.addHandler(ch)

    return logger
