import os
import xlrd

homework_path ='D:/2021.5/杨普科技/7.5-科技论文写作-朝君 - 副本/结课作业-综述/homework'
excel_path = 'D:/2021.5/杨普科技/7.5-科技论文写作-朝君 - 副本/科技论文写作成绩-21春-北京和烟台.xls'

# 获取excel里面的所有学号，或者homework里面所有的作业，之后进行匹配
# 学号
wb = xlrd.open_workbook(excel_path)
print(f"包括的表单数量：{wb.nsheets}")
print(f"表单的名分别为：{wb.sheet_names()}")
#获取指定的sheet对象
sheet = wb.sheet_by_name("北京成绩")
data = sheet.col_values(1,2,221)
print(data)
# 获取homework
homework_file = []
file = os.listdir(homework_path)
for file_name in file:
    name,_ = file_name.split('_')
    homework_file.append(name)
print(homework_file)


print("名单长度：{0}".format(len(data)))
print("作业长度：{0}".format(len(homework_file)))

# 这个比较两个列表所有的不同，是两个
# different = set(data).symmetric_difference(set(homework_file))
# print(different)

# 看看作业中有哪些与名单上的不同
different = set(homework_file).difference(set(data))
print(different)

