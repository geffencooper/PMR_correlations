'''
unload_util.py
Helper functions to extract tar and zip files
'''

import tarfile
import zipfile
import os

# extracts contents of a tar file to a folder
# in the specified directory path
def extract_tarfile(src_path, dest_path):
    my_tar = tarfile.open(src_path)
    my_tar.extractall(dest_path)
    my_tar.close()

# extracts contents of a zip file to a folder
# in the specified directory path
def extract_zipfile(src_path, dest_path):
    with zipfile.ZipFile(src_path,'r') as zipref:
        zipref.extractall(dest_path)


if __name__ == "__main__":

    # Step 1: extract all the zip files
    # zip_dir_name = "C:/Users/gcooper/Downloads/"
    # zip_dest_path = "C:/Users/gcooper/Downloads/avec_data"

    # zip_files = [(zip_dir_name + file_name) for file_name in os.listdir(zip_dir_name) if file_name.startswith("drive-download")]
    # for zf in zip_files:
    #     extract_zipfile(zf,zip_dest_path)

    # Step 2: extract all the tar files
    tar_dir_name = "C:/Users/gcooper/Downloads/avec_data/"
    tar_dest_path = "../../avec_data"

    tar_files = [(tar_dir_name + file_name) for file_name in os.listdir(tar_dir_name)]
    for tf in tar_files:
        extract_tarfile(tf,tar_dest_path)
