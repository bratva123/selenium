"""
there are different level of logging
DEBUG
INFO
WARNING
ERROR
CRITICAL

"""




import logging
logging.basicConfig(filename="test.log", level=logging.DEBUG)

logging.warning("warning msg")
logging.info("info msg")
logging.error("error msg")