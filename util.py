import application
import os
import config
import logging.config
from PIL import Image, ImageFilter, ImageEnhance

_logger = None

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

    def get_logger(self):
        global _logger

        if not _logger:
            logging.config.fileConfig(config.LOG_CONFIG_FILE)
            _logger = logging.getLogger(__name__)

        return _logger

    def is_image_file(self, path):
        try:
            Image.open(path)
        except IOError:
            return False
        return True

    def get_image_files_from_directory(self, path):
        files = []

        for entry in os.scandir(path):
            if not self.is_image_file(entry.path):
                self.get_logger().warning(entry.path + " is not an image file")
                continue

            if entry.is_file():
                files.append(os.path.basename(entry.path))

        if not files:
            raise Exception("No files under input directory")

        return files