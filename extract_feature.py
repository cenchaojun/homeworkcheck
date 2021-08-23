fname = './134_0050.jpg.txt'

with open(fname,'r+',encoding='utf-8') as f:
    s = [i[:-1].split(',') for i in f.readlines()]

print(len(s[0]))