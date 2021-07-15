import os
from shutil import copy2

origin_path = 'D:/2021.5/王云数据集/数据集/coil-100'
clas_path = 'D:/2021.5/王云数据集/数据集/class_coil_100'
image_name = [file for file in os.listdir(origin_path)]

class_list = list(set([file.split('_')[0] for file in os.listdir(origin_path)]))
for cls in class_list:
    dir = clas_path + '/' + cls
    os.mkdir(dir)

for file_name in os.listdir(origin_path):
    source_file_name = origin_path + '/' + file_name

    target_file_name = clas_path + '/' + file_name.split('_')[0] + '/'+  file_name
    copy2(src=source_file_name, dst=target_file_name)

print(len(class_list))

