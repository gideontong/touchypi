import logging

log_format = "%(asctime)-6s: %(name)s - %(levelname)s - %(message)s"
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter(log_format))
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(console_handler)
