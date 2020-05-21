import logging
import logging.config
class LoggerConf():
    def testCOnfLog(self):
        # create logger
        logging.config.fileConfig('logging.conf')
        logger = logging.getLogger(LoggerConf.__name__)

        #logging messages

        logger.debug("debug message")
        logger.info("info message")
        logger.warn("warn message")
        logger.error("error message")
        logger.critical("critical message")

demo = LoggerConf()

demo.testCOnfLog()