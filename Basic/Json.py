# Python3 使用json模块对Json数据及逆行编解码，它包含两个函数
# json.dumps() 对数据进行编码
# json.loads() 对数据进行解码

# 在json的编解码过程中，python原始类型与json类型会相互转换，规则如： https://www.runoob.com/python3/python3-json.html

import json

# python 字典类型转换为Json对象
data = {
    'no': 1,
    'name': 'Runoob',
    'url': 'http://www.runoob.com'
}

json_str = json.dumps(data)
print("Python 原始数据：", repr(data))
print("Json对象：", json_str)

# Python 字典转换为Json对象
data1 = {
    'no': 1,
    'name': 'Runoob',
    'url': 'http://www.runoob.com'
}

json_str1 = json.dumps(data1)
print("Python原始数据：", repr(data1))
print("JSON对象：", json_str1)

# 将json对象转换为python字典
data2 = json.loads(json_str1)
print("data2['name]:", data2['name'])
print("data2[''url]", data2['url'])


# 向文件写入Json数据
with open('data.json', 'w') as f:
    json.dump(data, f)

# 从文件读取数据
with open('data.json', 'r') as f:
    data = json.load(f)
