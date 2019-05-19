# Python提供了两个级别访问的网络服务：Socket, SocketServer
# Socket又称“套接字”，应用程序通常通过“套接字”向网络发出请求或者应答网络请求，使主机间或一台计算机上的进程间可以通讯

# 服务端
import sys
import socket

# socket.socket(family[,type[,proto]])
# 创建socket对象
serversocket = socket.socket(socket.AF_INET, socket.Sock_STREAM)

# 获取本地主机名
host = socket.gethostname()
port = 9999

# 绑定端口号
serversocket.bind((host, port))

# 设置最大连接数，超过后排队
serversocket.listen(5)

# 建立客户端连接
while True:
    clientsocket,addr = serversocket.accept()

    print("连接地址: %s" % str(addr))

    msg = '欢迎访问菜鸟教程！'+'\r\n'

    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()


# 客户端
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999

s.connect(host, port)

msg = s.recv(1024)

s.close()
print(msg.decode('utf-8'))


# Python Internet 模块
# HTTP(网页访问, 80)-httplib, urllib, xmlrpclib
# NNTP(阅读和张贴新闻文章, 119)-nntplib
# FTP(文件传输, 20)-ftplib, urllib
# SMTP(发送邮件, 25)-smtplib
# POP3(接受邮件, 110)-poplib
# IMAP4(获取邮件, 143)-imaplib
# Telnet(命令行, 23)-telnetlib
# Gopher(信息查找, 70)-gopherlib, urllib



# SMTP(Simple Mail Transfer Protocol) 发送邮件
# smtpObj = smtplib.SMTP([host[, port [, local_hostname]]])
# SMTP.sentmail(from_addr, to_addrs, msg[, mail_options, rcpt_options])
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'from@runoob.com'
receivers = ['4298377@qq.com']

message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("菜鸟叫阿称", 'utf-8')
message['To'] = Header("测试", 'utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error：邮件无法发送")

