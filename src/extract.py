import os
import requests
import zipfile

def download_zip_gdfs(url, path, chunk_size=4096):

    if os.path.exists(path):
        os.remove(path)

    chunks = requests.get(url, stream=True)
    with open(path, 'wb') as f:
        for chunk in chunks.iter_content(chunk_size=chunk_size):
            f.write(chunk)


def extract_zip_file(zip_file, dir_dest):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(dir_dest)
