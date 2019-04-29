# CGI
# Common Gateway Interface, 通用网关接口，它是一段程序，运行在服务器上，提供同客户端HTML页面的接口。


# CGI脚本输出CGI变量
import os
print("Content-type: text/html")
print()
print("<meta charset=\"utf-8\">")
print("<ul>")
for key in os.environ.keys():
    print("<li><span style='color:green'>%30s </span>: %s </li>" % (key, os.environ[key]))
print("</ul>")

# CGI处理Get请求 /cgi-bin/test.py?name=cnjc&url=http://www.runoob.com
# !/usr/bin/python3

# CGI处理模块
import cgi,cgitb

# 创建FieldStorge的实例化
form = cgi.FieldStorage()

# 获取数据
site_name = form.getvalue('name')
site_url = form.getvalue('url')

print("Content-type:text/html")
print()
print("<html>")
print("<head>")
print("<meta charset=\"utf-8\">")
print("<title>菜鸟教程 CGI 测试实例</title>")
print("</head>")
print("<body>")
print("<h2>%s官网：%s</h2>" % (site_name, site_url))
print("</body>")
print("</html>")

# 设置cookie Set-cookie:name=name;expires=date;path=path;domain=domain;secure
print('Set-Cookie: name="菜鸟教程"; expires=Wed, 28 Aug 2016 18:30:00 GMT')
