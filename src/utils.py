import os
from pathlib import Path

dir_path = os.path.dirname(__file__)
data_dirname = 'Data'
zip_filename = 'idfm-gdfs.zip'
zip_extract_name = 'gdfs-extract-tmp'

download_base_dir = Path(dir_path) / data_dirname
zip_path = download_base_dir / zip_filename
zip_path_extract = download_base_dir / zip_extract_name

if not download_base_dir.exists():
    os.makedirs(download_base_dir)
else:
    print(f'{download_base_dir} already exist')
