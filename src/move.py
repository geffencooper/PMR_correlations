import os
import shutil

dir_name = "C:/Users/gcooper/Downloads/drive-download-20210713T151601Z-001/"
dest_path = "../../avec_data"

files = [(dir_name + file_name) for file_name in os.listdir(dir_name)]
# print(os.path.basename(files[0])[:4]+"P")
for f in files:
    p = os.path.basename(f)[:4]+"P"
    shutil.move(f,dest_path+"/"+p)
