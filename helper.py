import re
import config
import pytesseract
from PIL import Image, ImageFilter, ImageEnhance
from util import Util

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

    def process_and_save(self, files):
        try:
            for file in files:
                im = Image.open(config.IN_FILE_DIR + file)
                im = im.filter(ImageFilter.MedianFilter())
                enhancer = ImageEnhance.Contrast(im)
                im = enhancer.enhance(2)
                im = im.convert('1')
                im.save(config.OUT_FILE_DIR + file)
        except FileNotFoundError as fnf:
            Util.getInstance().get_logger().error(fnf)
        except Exception as e:
            Util.getInstance().get_logger().error(e)

    def get_nid(self, file):
        nid = None

        text = pytesseract.image_to_string(Image.open(config.OUT_FILE_DIR + file))

        res = text.partition("N0")[2]
        if not res:
            res = text.partition("NO")[2]

        if res.find(" ") == 1:
            res = res[1:]

        res = res.replace(" ", "")

        list = re.findall(r'\d+', res)
        item = "".join(list)

        if len(str(item)) == 13 or len(str(item)) == 17:
            nid = item
        return nid

    def get_nid_list(self, files):
        nid_list = []
        try:
            for file in files:
                nid_list.append(self.get_nid(file))
            return nid_list
        except FileNotFoundError as fnf:
            Util.getInstance().get_logger().error(fnf)
        except Exception as e:
            Util.getInstance().get_logger().error(e)