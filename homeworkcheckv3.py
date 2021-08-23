import os
import xlrd

mate = '2021博士.xlsx'
total ='127947576_2_2021级新生文化衫统计_271_271.xlsx'
# excel_path = 'D:/2021.5/杨普科技/7.5-科技论文写作-朝君 - 副本/科技论文写作成绩-21春-北京和烟台.xls'



# 获取excel里面的所有学号，或者homework里面所有的作业，之后进行匹配
# 学号
wb = xlrd.open_workbook(mate)
print(f"包括的表单数量：{wb.nsheets}")
print(f"表单的名分别为：{wb.sheet_names()}")
#获取指定的sheet对象
sheet = wb.sheet_by_name("blq")
# 取第三列从三行的数据
# 去第6列，从第二行到
data_mate = sheet.col_values(5,1,45)
print(data_mate)
print(len(data_mate))

# 或者所有的名单
total_number = xlrd.open_workbook(total)
sheet_total = total_number.sheet_by_name('Sheet1')
data_total = sheet_total.col_values(6,1,272)
print(data_total)
print(len(data_total))

# 先求出并集，之后再求出差
# 并集
same_vale = set(data_mate) & set(data_total)
print(same_vale)
print(len(same_vale))
no_submite = set(data_mate).difference(same_vale)
print(no_submite)

# 找出差异
# 获取homework
# homework_file = []
# file = os.listdir(homework2_path)
# for file_name in file:
#     _,name = file_name.split('_')
#     homework_file.append(name)
# print(homework_file)
#
#
# print("名单长度：{0}".format(len(data)))
# print("作业长度：{0}".format(len(homework_file)))
#
# # 这个比较两个列表所有的不同，是两个
# # different = set(data).symmetric_difference(set(homework_file))
# # print(different)
#
# # 看看作业中有哪些与名单上的不同
# different = set(homework_file).difference(set(data))
# print(different)
#
# # 在检查一下还有谁没有提交作业
# no_submit = set(data).difference(set(homework_file))
# print(no_submit)
