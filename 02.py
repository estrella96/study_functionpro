#返回函数
def myF2():
    def myF3():
        print("In myF3")
        return 3
    return myF3
f3=myF2()
print(type(f3))
print(f3)
print(f3())

#复杂例子 标准闭包结构
def myF4(*args):
    def myF5():
        rst=0
        for n in args:
            rst += n
        return rst
    return myF5
f5=myF4(1,2,3,4,5,6,7,8,9,0)
a=f5()
print(a)

#闭包
def count():
    fs=[]
    for i in range(1,4):
        #闭包结构
        def f():
            return i*i
        fs.append(f)
    return fs

f1,f2,f3=count()
print(f1()) #9
print(f2()) #9
print(f3()) #9
#返回函数引用的变量i，i不是立即执行，而是等三个函数都返回时才统一使用 i变为3
#返回闭包时，返回函数不能引用任何循环变量
#解决方案：再创建一个函数，用函数的参数绑定循环变量的当前值
#修改
def count1():
    def f(j):
        def g():
            return j*j
        return g
    fs=[]
    for i in range(1,4):
        fs.append(f(i))
    return fs

f1,f2,f3=count1()
print(f1())
print(f2())
print(f3())

#装饰器
# def hello():
#     print("hello world")
# f=hello
# f()
#对hello功能进行扩展 打印之前打印当前系统时间 不改动现有代码
import time
#高阶函数
def printTime(f):
    def wrapper(*args,**kwargs):
        print("Time: ",time.ctime())
        return f(*args,**kwargs)
    return wrapper()
def hello3():
    print("手动")

hello3=printTime(hello3)
hello3


@printTime
def hello():
    print("hello world")

a = hello

# 偏函数
# 字符串转化为十进制数字
print(int("12345"))
#八进制12345转化为十进制5349
print(int("12345", base=8))

#函数默认输入字符串是十六进制数字 返回十进制
def int16(x,base=16):
    return int(x,base)
a=int16("1f")
print(a)

import functools
int161=functools.partial(int,base=16)
a=int161("2f")
print(a)

