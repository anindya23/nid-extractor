import application
import config
from helper import Helper
from util import Util

def extract_nid():
    try:
        files = Util.getInstance().get_image_files_from_directory(config.IN_FILE_DIR)
        Helper.getInstance().process_and_save(files)
    except Exception as e:
        Util.getInstance().get_logger().error(e)

if __name__ == "__main__":
    extract_nid()