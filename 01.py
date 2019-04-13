
#lambda表达式
stm=lambda x:x*100
print(stm(89))
stm2=lambda x,y,z:x+y*10+z*100
print(stm2(1,8,9))

#高阶函数
def funA(n):
    return n * 100
#正常调用
def funB(n):
    return funA(n)*3

print(funB(9))
#高阶函数
def funC(n,f):
    return f(n)*3
print(funC(9,funA))

#map
l1=[i for i in range(10)]
print(l1)
def mulTen(n):
    return n*10
l2=map(mulTen,l1)
print(l2)
for i in l2:
    print(i)


#reduce
from functools import reduce
def myAdd(x,y):
    return x + y
rst=reduce(myAdd,[1,2,3,4,5,6])
print(rst)

#filter
def isEven(a):
    return a%2==0
l=[2,34,52,45,34,667,2324]
rst=filter(isEven,l)
print(rst)
print([i for i in rst])

#排序
a=[2,34,52,45,34,667,2324,5,6]
al=sorted(a,reverse=True)
print(al)

#按绝对值倒序排序
a=[2,-34,52,45,34,-667,-2324,5,6]
al=sorted(a,key=abs,reverse=True)
print(al)

#按字符串排序
astr=['Jane','luis','jing','apple']
str1=sorted(astr)
print(str1)
str2=sorted(astr,key=str.lower)
print(str2)
