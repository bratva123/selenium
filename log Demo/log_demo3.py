import logging
from . import customLogger as cl
class LoggingDemo3():
    log = cl.customLoggers(logging.DEBUG)


    def method1(self):
        self.flog.debug("debug message")
        self.log.info("info message")
        self.log.warn("warn message")
        self.log.error("error message")
        self.log.critical("critical message")

    def method2(self):
        self.flog.debug("debug message")
        self.log.info("info message")
        self.log.warn("warn message")
        self.log.error("error message")
        self.log.critical("critical message")

    def method3(self):
        self.flog.debug("debug message")
        self.log.info("info message")
        self.log.warn("warn message")
        self.log.error("error message")
        self.log.critical("critical message")

demo = LoggingDemo3()
demo.method1()
demo.method2()
demo.method3()

