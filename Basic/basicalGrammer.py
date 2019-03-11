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
#  **  返回x的y次幂
#  //  取整除（向下取接近除数的整数）

# some math function
abs(x)
ceil(x)
cmp(x,y)  #比较两个数字的大小
exp(x)
fabs(x)
floor(x)
log(x)
log10(x)
# max(x1,x2,...)
# min(x1,x2,...)
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
# %c
# %s
# %d
# %f
# %E
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
# list.pop([index=-1])
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
# parame={value1,value2,...}
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
        print(next(f))
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


"""
文件读写：r, rb, r+, rb+; w, wb, w+, wb+; a, ab, a+, ab, a+, ab+
"""
f=open("/tmp/foo.txt","w")  #open函数返回一个file对象
f.write("Python是一个非常好的语言。\n是的，的确非常的好！！\n")
f.close()

# some function for file object
f.read()
f.readline()
f.readlines()
f.write()
f.tell()
f.seek(offset,from_what)    #0,1,2分别表示从起始位置，当前位置和终点位置偏移相应的字符数
f.close()

# pickle模块可以对基本的数据进行序列和反序列化
import pickle
data1={'a':[1,2.0,3,4+6j],'b':('string',u'Unicode string'),
       'c':None}
selfref_list=[1,2,3]
slefref_list.append(selfref_list)
output=open('data.pk1','wb')

# Pickle dictionary using ptotocol 0.
pickle.dump(data1,output)

# Pickle the list using the highest protocol available
pickle.dump(selfref_list,output,-1)
output.close()


import pprint,pcikle


#使用pickle模块从文件中重构python对象
pkl_file=open('data.pkl','rb')
data1=pickle.load(pkl_file)
pprint.pprint(data1)
pkl_file.close()

# File methods
"""open方法用于打开一个文件，返回文件对象，在对文件进行处理过程中都需要使用到这个函数，如果文件无法被打开，会抛出OSError。
使用open()方法，一定要确保关闭文件对象，即调用close()方法
"""

# open(file,mode='r',buffering=-1,encoding=None,errors=None,newline=None,closefd=True,opener=None)
file.close()
file.flush()
file.fileno()
file.isatly()
file.next()
file.read([size])
file.readlines([sizeint])
file.seek(offset,[whence])
file.tell()
file.truncate([size])
file.write(str)
file.writelines(sequence)


# OS methods
os.access(path,mode)
os.chdir(path)
os.chmod(path,mode)
os.chown(path,uid,gid)
os.close(fd)
os.dup(fd)
os.dup2(fd,fd2)
os.fchdir(fd)
os.fchmod(fd,mod)
os.fchown(fd,uid,fid)
os.fdopen(fd,[mode],[bufsize])
os.fstat(fd)
os.getcwdu()
os.listdir(path)
os.makedirs(path,[mode])
os.open(file,flags,[mode])
os.remove(path)
os.removedirs(path)
os.rename(src,dst)
os.path()

# warning and error

#example one
while True:
    try:
        x=int(input("Please enter a number"))
        break
    except ValueError:
        print("Oops! That was not a valid number, Try again!")

##except(RuntimeError,TypeError,NameError):
##    pass

# example second
import sys


try:
    f=open('myfile.txt')
    s=f.readline()
    i=int(s.strip())
except OSError as err:
    print("OS error:{}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexcepted erroe:",sys.exc_info()[0])
    raise

#example third
for arg in sys.argv[1:]:
    try:
        f=open(arg,'r')
    except IOError:
        print('cannot open',arg)
    else:   # do this when no errot hanppen
        print(arg,'has',len(f.readlines()),'lines')
        f.close()

# example fourth
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by')
    raise

# example fifth
class MyError(Exception):
    def _init_(self,value):
        self.value=value
    def _str_(self):
        return repr(self.value)

try:
    raise MyError(2*2)
except MyError as e:
    print('My exception occured, value',e.value)

"""
当创建一个模块有可能抛出多种不同的异常时，一种通常的做法是为这个包建立一个基础异常类，然后基于这个基础类为不同的错误情况创建不同的子类
"""

# example sixth
try:
    raise KeyboardInteerupt
finally:
    print("Goodbye, world!")

# example seventh
"""预定义的清理行为，一些对象定义了标准的清理行为，无论系统是否成功调用了它，一旦不需要它了，这个标准的清理行为就会执行"""
with open("myfile.txt") as f:
    for line in f:
        print(line)


"""
Python3 面向对象
类、方法、类变量、数据成员、方法重写、局部变量、实例变量、继承、实例化、对象
对象是通过类定义的数据结构实例，对象包括两个数据成员（类变量和实例变量）和方法。
Python中类机制：允许多个基类，派生类可以覆盖基类中的任何方法，方法中可以调用基类中的同名方法。
"""
# 类对象；类对象支持两种操作：属性引用和实例化
# example first  
class MyClass:
    """一个简单的类实例"""
    i=12345
    def f(self):
        return 'hello world'
#实例化类--类对象创建后，类命名空间中所有的命名都是有效属性名
x=MyClass()
print("MyClass 类的属性i为：",x.i)
print("MyClass 类的方法f输出为：",x.f())


# 类初始化方法_init_(),方法参数可以传递到类的实例化操作上
# example second
class Complex:
    def _init_(self,realpart,imagpart):
        self.r=realpart
        self.i=imagpart
x=Complex(3.0,-4.5)
print(x.r,x.i)


# example third
# self代表类的实例；类的方法与普通的函数只有一个特别的区别，它们必须有一个额外的第一参数名称，按照惯例它的名称是self
class Test:
    def prt(self):
        print(self)
        print(slef._class_)
t=Test()
t.prt()


# 类的方法必须包含参数self，且为第一个参数，self代表的是类的实例
# example forth
class people:
    # 定义基本属性
    name=''
    age=0
    # 定义私有属性，在类外部无法直接进行访问
    _weight=0
    # 定义构造方法
    def _init_(self,n,a,w):
        self.name=n
        self.age=a
        slef._weight=w
    def speak(self):
        print("%s说：我%d岁。"%(self.name,self.age))

p=pepple('runoob',10,30)
p.speak()


# 继承，类可以多重继承，子类在调用父类方法时，若无特别指明，则按照从左到右的顺序在基类中查找方法
# example fifth
# 类定义
class people:
    # 定义基本属性
    name=''
    age=0
    # 定义私有属性
    _weight=0
    # 定义构造方法
    def _init_(self,n,a,w):
        self.name=n
        self.age=a
        self._weight=w
    def speak(self):
        print("%s说：我%d岁。"%(self.name,self.age))
        
# 单继承示例
class student(people):
    grade=''
    def _init_(slef,n,a,w,g):
        # 调用父类的构造函数
        people._init(self,n,a,w)
        self.grade=g
    # 覆盖父类的方法
    def speak(slef):
        print("%s说：我%d岁，我在读%d年纪"%(self.name,self.age,slef.grade))
        
# 另写一个类，多继承之前的准备
class speaker():
    topic=''
    name=''
    def _init_(self,n,t):
        self.name=n
        self.topic=t
    def speak(self):
        print("我叫%s，我是一个演说家，我演讲的主题是%s"%(self.name,self.topic))
        
# 多重继承
class sample(speaker,student):
    a=''
    def _init_(self,n,a,w,g,t):
        student._init_(self,n,a,w,g)
        speaker._init_(self,n,t)

test=sample("Tim",25,80,4,"Python")
test.speak()

# 方法重写
class Parent:
    def myMethod(self):
        print("调用父类方法")

class Child(Parent):
    def myMethod(self):
        print("调用子类方法")

c=Child()
c.myMethod()
super(Child,c).myMethod()


# 类属性和方法
"""
类的私有属性：以两个下划线开头，不能在类的外部使用或直接访问。类内部的方法中使用方法self.__private_attrs
类的方法：使用def关键字来定义方法，类方法必须包含参数self,且为第一个参数
类的私有方法：两个下划线开头的方法，声明该方法为私有方法，只能在类的内部调用。self__private_methods
"""
# example sixth
class Site:
    def __init__(self,name,url):
        slef.name=name
        self.__url=url

    def who(self):
        print('name:',slef.name)
        print('url:',self.__url)

    def __foo(self):
        print('这是私有方法')

    def foo(self):
        print("这是公共方法")

x=Site('菜鸟教程','www.runoob.com')
x.who()
x.foo()
x.__foo()   # 报错


# 类的专有方法，可以对该方法进行重载
__init__
__del__     # 析构函数
__repr__    # 打印，转换
__setitem__  
__getitem__
__len__
__cmp__     #比较运算
__call__
__add__
__sub__
__mul__
__truediv__
__mod__
__pow__



"""
标准库概览
"""
# 操作系统接口
import os
os.getcwd() #show working directory
os.chdir('/server/accesslogs')  # changing working directory
os.system('mkdir today')

import shutil
shutil.copyfile('data.db','archive.db')
shutil.move('/build/executables','installdir')

# 文件通配符
import glob
glob.glob('*.py')

# 命令行参数
import sys
print(sys.argv)

# 错误输出重定向和程序终止
sys.stderr.write('Warning,log file not found starting a new one\n')

# 字符串正则匹配
import re
re.findall(r'\bf[a-z]*','which foot or hand fell fastest')
re.sub(r'(\b[a-z]+) \1',r'\1','cat in the the hat')

# 数学
import math
math.cos(math.pi/4)
matg.log(1024,2)

import random
random.choice(['apple','pear','banana'])
random.sample(range(100),10)
random.random()
random.randrange(6)

# 访问互联网
from urllib.request import urlopen
for line in urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
    line=line.decode('utf-8')
    if 'EST' in line or 'EDT' in line:
        print(line)

import smtplib
server=smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org','jcaesar@example.org')
server.quit()

# 日期和时间
from datatime import date
now=date.today()
now
now.strftime('%m-%d-%y.%d %b %Y is a %A on the %d day of %B.')

birthday=date(1964,7,31)
age=now-birthday
age.days

# 数据压缩
import zlib
s=b'witch which has which witches wrist watch'
len(s)

t=zlib.compress(s)
len(t)

zlib.decompress(t)

zlib.crc32(s)

# 性能度量
from timeit import Timer
Timer('t=a;a=b;b=t','a=1;b=2').timeit()

# 测试模块
"""
doctest模块
unittest模块
"""

