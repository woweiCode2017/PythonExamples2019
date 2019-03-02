# some methods to translate data type
int(x)
float(x)
complex(real)
str(x)
repr(x)
eval(str)
tuple(s)
list(s)
set(s)
dict(d)
frozenset(s)    #make a set unchangeable
chr(x)
ord(x)  #make a char to int
hex(x)  #make a number to sixten formate
oct(x)  

""" mutiply rows of
    commit
"""
**  # 返回x的y次幂
//  # 取整除（向下取接近除数的整数）

# some math function
abs(x)
ceil(x)
cmp(x,y)  #比较两个数字的大小
exp(x)
fabs(x)
floor(x)
log(x)
log10(x)
max(x1,x2,...)
min(x1,x2,...)
modf(x)   #return the int part and tinyint part
pow(x,y)
round(x)
sqrt(x)

# random function
choice(seq)
randrange([start],stop,[step])
seed([x])
shuffle(lst)
uniform(x,y)

# triangle function
acos(x)
asin(x)
atan(x)
atan2(y,x)
cos(x)
sin(x)
tan(x)

#字符串截取遵循左闭右开原则
# str format kind
%c
%s
%d
%f
%E
print("我叫 %s 今年%d岁"%('小明',10))

# some function to handle with str
capitalize()
count(str,beg=0,end=len(string))
bytes.decode(encode="utf-8",errors="strict")
encode(encode="utf-8",errors="strict")
endswith(suffic,beg=0,end=len(string))
find(str,beg=0,end=len(string))
index(str,beg=0,end=len(string))
isalnum()
join()
len(string)
replace(old,new,[max])
split(str="",num=string.count(str))


# some function to handle with list
del lsit[2]
len(list)
max(list)
min(list)
list(seq)
list.append(obj)
list.count(obj)
list.extend(seq)
list.index(obj)
list.insert(index,obj)
list.pop([index=-1])
list.remove(obj)
list.reverse()
list.sort(key=None,reverse=False)
list.clear()
list.copy()

# some function to handle with tuple
del tup
len(tuple)
max(tuple)
min(tuple)
tuple(seq)

# some function handle with dict
dict={'Name':'zs','age':12}
dict['Name']
del dict
del dict['Name']
dict.clear()

len(dict)
str(dict)
type(variable)

randiansdict.clear()
randiansdict.copy()
randiansdict.fromkeys()
randians.get(key,default=None)
key in dict
randiansdict.items()
randiansdict.keys()
randiansdict.setdefalut(key,default=None)
randiansdict.update(dict2)
randiansdict.values()
pop(key)
popitem()

# some function handle with set
parame={value1,value2,...}
s.add(x)
s.upfate(x)
s.remove(x)
s.discard(x)  #移除的元素不存在时不会抛出错误
s.pop()
len(s)
s.clear()
x in s

add()
clear()
copy()
difference()
difference_update()
discard()
intersection()
intersection_update()
isdisjoint()
issubset()
issuperset()
pop()
remove()
symmetric_difference()
symmetric_difference_update()
union()
update()


# first example
a,b=0,1
while b<1000:
    print(b,end-',')
    a,b=b,a+b

# second example
if condition_1:
    statement_block_1
elif condition_2:
    statement_block_2
else:
    statement_block_3

# third example
for x in languages:
    print(x)
    
# forth example
count=0
while count<5:
    print(count,"小于5")
    count=count+1
else:
    print(count,"大于或等于5")
"""
在while···else在条件语句为flase时执行else的语句块
"""

# fifth example
for i in range(5):
    print(i)

# break continue pass

# iteration对象是一个可以记住遍历的位置的对象，迭代器从第一个元素开始访问，只进不退，有iter(),next()两个方法
import sys
list=[1,2,3,4]
it=iter(list)
while true:
    try:
        print(next(it))
        except StopIteration:
            sys.exit()
"""
把一个类作为一个迭代器使用需要在类中实现两个方法_iter_(),_next_()
"""

#使用了yield的函数称为生成器
"""
生成器是一个返回迭代器的函数，只能用于迭代操作，类似于一个迭代器
每次运行到yield函数时会返回yield的值，并暂停运行，当调用next()方法时继续执行。
"""
import sys
def fibonacci(n):
    a,b,counter=0,1,0
    while true:
        if(counter>n):
            return
        yield a
        a,b=b,a+b
        counter+=1
f=fibonacci(10)

while true:
    try:
        print(next(f),end=" ")
    except StopIteration:
        sys.exit()


# some definition and rules about function
#1.definition and call
def hello():
    print("Hello World!")

hello()

# parameters transform
"""
1 在python中变量没有类型，类型属于对象的
2 在pyhon中对象分为可变对象（list,dict）和不可变对象（string,tuples,numbers）
3 指向不可变类型的变量重新赋值后，实际上创建了一个新的对象，并将变量指向新的对象
4 关于pyhon参数传递的问题分为两类：
    1 不可变类型传递时，传递的是值，不会影响对象本身
    2 可变类型传递时，会将对象传递过去，相当于引用传递
5  必需参数、关键字参数（str="zs")、默认参数、不定长参数（*与**）

"""

# lambda 表达式用于创建匿名函数
sum=lambda arg1,arg2:arg1+arg2

# 作用域
"""
L(Local) 局部作用域
E(Enclosing) 闭包函数外的函数中
G(Global) 全局作用域
B(Built-in) 内置作用域（内置函数做再模块的范围）
以L->E->G->B的顺寻查找变量
当内部作用域想修改外部作用域的变量时，要用到global和nonlocal（修改Eclosing作用域中的变量）关键字
"""

# DataStructure
# 列表推导
vec=[2,4,6]
[x*3 for x in vec]
[[x,x*x] for x in vec]
[x*3 for x in vec if x>3]

# 序列遍历
# enumerate()函数可以同时获得序列的索引和值
for i,v in enumerate(['tic','tac','toe']):
    print(i,v)

# zip()函数可以缝合两个序列，同时进行遍历
for q,a in zip(questions,answers):
    print('What is your {0}? It is {1}.'.format(q,a))

# reversed()   sorted()

# module
import sys
print("命令行参数如下：")
for i in sys.args:
    print(i)
print('\n\nPython 路径为：',sys.path,'\n')

# from modname import *

if _name_=='_main_':
    print('program is runing selfly')
else:
    print('program is running as a module')

#dir()

"""包是一种管理Python模块命名空间的形式，采用“点模块的形式”。将包含有_init_.py文件的目录视为一个包
   _all_是_init_.py文件中的一个变量列表，记录了包里所有的模块名
"""
from sound.effects import echo

print('{}网址："{}!"'.format('菜鸟教程','www.runbo.com'))
print('{0}和{1}'.format('Google','Runob'))
print('{name}网址：{site}'.formate(name='菜鸟教程',site='www.runoob.com'))
# ':'可以对值进行格式化，或者对其格式（后面跟整数时）
print('常量PI的值近似为：{0:.3f}。'.formate(math.pi))

table={'Google':1,'Runoob':2,'Taobao':3}
for name,number in table.items():
    print('{0:10}==>{1:10d}'.formate(name,number))
# 另一种格式化方法%
print('常量PI的值近似为：%5.3f。' % math.pi)

#  读取键盘输入
str=input("请输入：")
print("您输入的内容是：",str)

