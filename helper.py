import application
import config

class Helper:
    __instance = None

    @staticmethod
    def getInstance():
        if Helper.__instance == None:
            Helper()
        return Helper.__instance

    def __init__(self):
        if Helper.__instance != None:
            raise Exception("This helper class is a singleton!")
        else:
            Helper.__instance = self