import logging
logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt="%m/%d/%Y %I:%M:%S %p",
                    level=logging.DEBUG)

logging.warning("warning msg")
logging.info("info msg")
logging.error("error msg")