from src import extract as extract
from src import utils
import time


if __name__ == '__main__':
    print(utils.dir_path)
    print(f'{time.asctime()}: Download Zip File ...')
    extract.download_zip_gdfs(utils.url_zip, path=utils.zip_path)
    print(f'{time.asctime()}: Success zip file Downloaded...')
    extract.extract_zip_file(utils.zip_path, utils.zip_path_extract)
    print(f'{time.asctime()}: Success Extract zip file on {utils.zip_path_extract}...')

