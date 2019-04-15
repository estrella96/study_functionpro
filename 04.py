#file-open
#r 后面字符串不需要转义
f=open(r"text01.txt",'r')
f.close()

#with
with open(r"text01.txt",'r') as f:
    # 按行读取内容
    strline=f.readline()
    while strline:
        print(strline)
        strline=f.readline()
# list能用打开的文件作为参数 把文件每一行作为一个元素
with open(r"text01.txt",'r') as f:
    l=list(f)
    for line in l:
        print(line)
#read
with open(r"text01.txt", 'r') as f:
    strChar=f.read(3)
    print(len(strChar))
    print(strChar)
#seek
with open(r"text01.txt", 'r') as f:
    f.seek(6,0)
    strChar=f.read()
    print(strChar)

import time
with open(r"text01.txt", 'r') as f:
    strChar=f.read(3)
    while strChar:
        print(strChar)
        # time.sleep(1)
        strChar=f.read(3)
#tell
with open(r"text01.txt", 'r') as f:
    strChar = f.read(3)
    pos=f.tell()
    while strChar:
        print(pos)
        print(strChar)
        strChar=f.read(3)
        pos=f.tell()
#write
with open(r"text01.txt", 'a') as f:
    f.write("君埋泉下泥销骨\n我寄人间雪满头")
    f.writelines("敬旷世温柔，至死方休")

#pickle 序列化
import pickle
age=19
with open(r"text02.txt", 'wb') as f:
    pickle.dump(age,f)
with open(r"text02.txt", 'rb') as f:
    age=pickle.load(f)
    print(age)