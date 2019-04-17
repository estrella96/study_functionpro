import logging
import logging.handlers
import datetime

# logging.basicConfig(level=logging.DEBUG)
# logging.debug("This is a debug logging")
# logging.info("This is a info logging")

#定义logger
logger=logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)

rf_handler=logging.handlers.TimedRotatingFileHandler('all.log',when='midnight')
rf_handler.setFormatter(logging.Formatter("%(asctime)s-%(levelname)s-%(message)s"))

logger.addHandler(rf_handler)

logger.debug("debug message")