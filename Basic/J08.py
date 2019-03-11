# -*-coding:utf-8-*-


x=input('输入x的值：')
y=input('输入y的值：')

temp=x
x=y
y=temp
# x,y=y,x

print('交换后的x值为：{}'.format(x))
print('交换后的y值为：{}'.format(y))

