import os
from shutil import copy2
from math import floor



if __name__ == '__main__':
    splite_ratio = 1100
    # D:\2021.5\王云数据集\数据集\王云DL方法对比\原始数据\AR50x40
    pre_origin_path = 'D:/2021.5/王云数据集/数据集/王云DL方法对比/原始数据/usps16x16'
    clas_path = 'D:/2021.5/王云数据集/数据集/王云DL方法对比/划分后的数据/usps16x16'


    file_list = [file for file in os.listdir(pre_origin_path)]
    file_list.sort(key=lambda x:int(x.split('.')[0]))
    for index,file in enumerate(file_list):
        if index%splite_ratio==0:
            dir = clas_path + '/' +str(int(index/splite_ratio))
            os.mkdir(dir)
        origin_file = pre_origin_path + '/' + file
        target_file = dir + '/' + file
        print(origin_file)
        print(target_file)
        copy2(src=origin_file,dst=target_file)
# for index
# print(file_list)

# image_name = [file for file in os.listdir(origin_path)]
#
# class_list = list(set([file.split('_')[0] for file in os.listdir(origin_path)]))
# for cls in class_list:
#     dir = clas_path + '/' + cls
#     os.mkdir(dir)
#
# for file_name in os.listdir(origin_path):
#     source_file_name = origin_path + '/' + file_name
#
#     target_file_name = clas_path + '/' + file_name.split('_')[0] + '/'+  file_name
#     copy2(src=source_file_name, dst=target_file_name)
#
# print(len(class_list))