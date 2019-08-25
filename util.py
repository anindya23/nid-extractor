import application
import config
import logging

class Util:
    __instance = None
    __logger = None

    @staticmethod
    def getInstance():
        if Util.__instance == None:
            Util()
        return Util.__instance

    def __init__(self):
        if Util.__instance != None:
            raise Exception("This helper class is a singleton!")
        else:
            Util.__instance = self

    def get_logger(self):
        global __logger

        if not __logger:
            logging.config.fileConfig(config.LOG_CONFIG_FILE)
            __logger = logging.getLogger(__name__)

        return __logger