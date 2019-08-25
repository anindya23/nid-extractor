import application
import config

class Util:
    __instance = None

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

