
# 正则表达式
# re.match(pattern, string, flags=0) # 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，就返回none
import re
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))  # 不在起始位置匹配

# re.search(pattern, string, flags=0)  # 扫描整个字符串并返回第一个成功的匹配

# re.sub(pattern, repl, string, count=0)  # 替换字符串中的匹配项
phone = "2004-959-559 # 这是一个电话号码"
print("电话号码：", re.sub(r'#.*$', "", phone))  # 删除注释
print("电话号码：", re.sub(r'/D', "", phone))  # 移除非数字的内容


def double(matched):
    value = int(matched.group('value'))
    return str(value*2)


s = 'A23G4HFD567'
print(re.sub(r'(\d+)', double, s))

# compile函数用于编译正则表达式，生成一个正则表达式对象，提供match和search两个函数使用
# re.compile(pattern[, flags])
pattern = re.compile(r'\d')
m = pattern.match('one12twothree34four')
print(m)
m = pattern.match('onw12twothree34four', 2, 10)
m = pattern.match('onw12twothree34four', 3, 10)
print(m.group())
print(m.start(0))
print(m.end(0))
print(m.span(0))

# findall 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表
# findall(string[, pos[, endpos]])
pattern = re.compile(r'/d')
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('runoob123google456', 0, 10)
print(result1)
print(result2)

# finditer 在字符串中找到正则表达式所匹配的所有子串，并把他们作为一个迭代器返回
# re.finditer(pattern, string, flags=0)
it = re.finditer(r"\d+", "12a32bc43jf3")
for match in it:
    print(match.group())

# re.split 按照匹配的子串将字符串分割后返回列表
# re.split(pattern, string[, maxsplit=0, flags=0])
re.split(r'\W+', 'runoob, runoob, runoob.')
re.split('a*', 'hello world')





