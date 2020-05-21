"""
Logger Demo
"""
import logging
class LoggerDemoConsole():
    def testLog(self):
        #create logger
        logger = logging.getLogger('sample_log')
        logger.setLevel(logging.INFO)
        #create console handler and set level to info
        chandler = logging.StreamHandler()
        chandler.setLevel(logging.INFO)

        #create formator
        formator = logging.Formatter('%(asctime)s -%(name)s: %(levelname)s: %(message)s',
                        datefmt="%m/%d/%Y %I:%M:%S %p")
        chandler.setFormatter(formator)

        #add console..to handler
        logger.addHandler(chandler)
        logger.debug("debug message")
        logger.info("info message")
        logger.warn("warn message")
        logger.error("error message")
        logger.critical("critical message")

ld = LoggerDemoConsole()
ld.testLog()

