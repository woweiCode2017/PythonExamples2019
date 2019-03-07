#二次方程ax**2+bx+c=0
#a,b,c用户提供，为实数，a<>0

#导入cmath(复杂数学运算)模块
import cmath

a=float(input('请输入a:'))
b=float(input('请输入b:'))
c=float(input('请输入c:'))

#计算
d=(b**2)-(4*a*c)

#求解
sol1=(-b-cmath.sqrt(d))/(2*a)
sol2=(-b+cmath.sqrt(d))/(2*a)

print('结果为{0}和{1}'.format(sol1,sol2))
