import os
import shutil

dir_name = "../data/"
dest_path_plot = "../data/plots"
dest_path_csv = "../data/csv"

files = [(dir_name + file_name) for file_name in os.listdir(dir_name) if (file_name.endswith('.png') or file_name.endswith('.csv'))]
for f in files:
    p = os.path.basename(f)
    if p.endswith('.png'):
        shutil.move(f,dest_path_plot+"/"+p)
    if p.endswith('.csv'):
        shutil.move(f,dest_path_csv+"/"+p)
