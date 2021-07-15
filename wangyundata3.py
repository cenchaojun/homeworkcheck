import os
from shutil import copy2
from math import floor


def partition_cut2(ls: list, ncut):
    """
    Returns a new list with elements
    of which is a list of certain size.
        >>> partition_cut([1, 2, 3, 4, 5], 3)
        [[1, 4], [2, 5], [3]]

    :param ls:
    :param n:
    :return: list has been cut
    """
    n = len(ls)
    if n <= 1 or ncut <= 1:
        return ls

    res = [[] for _ in range(ncut)]
    for i in range(n):
        idx = i % ncut
        res[idx].append(ls[i])

    return res


if __name__ == '__main__':

    pre_origin_path = 'D:/2021.5/王云数据集/数据集/COIL_crop'
    clas_path = 'D:/2021.5/王云数据集/数据集/class_coil_crop'
    file_list = [file for file in os.listdir(pre_origin_path)]
    file_list.sort(key=lambda x:int(x.split('.')[0]))
    for index,file in enumerate(file_list):
        if index%72==0:
            dir = clas_path + '/' +str(int(index/72))
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