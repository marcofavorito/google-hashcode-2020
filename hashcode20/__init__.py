import logging

_DEFAULT_LOG_FORMAT = '[%(asctime)s][%(name)s][%(funcName)s][%(levelname)s] %(message)s'
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter(_DEFAULT_LOG_FORMAT)
handler.setFormatter(formatter)
logger.addHandler(handler)
