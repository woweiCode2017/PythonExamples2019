#  list的常用操作


# list 定义
li=["a","b","mpilgrim","z","example"]

# list 索引
print(li)

print(li[1])

print(li[-1])

print(li[1:3])

print(li[1:-1])

# list 增加元素
li.append("new")

li.insert(2,"old")

li.extend(["two","elementst"])

# list 搜索
li.index("example")

print("c" in li)

# list 删除元素

li.remove("z")

print(li.pop()) # 删除最后一个元素

# list 运算符
li=li+['example','new']

li+=["two"]

li+=[1,2]*3

# join连接list成为字符串
params={"server":"mpilgrim","database":"master","uid":"sa","pwd":"secret"}

print(";".join(["%s=%s"%(k,v) for k,v in params.items()]))

# list 分割字符串
li=['server=mpilgrim','uid=sa','database=master','pwd=secret']
s=";".join(li)

print(s.split(";"))

print(s.split(";",1))

# list 的映射解析
print([elem*2 for elem in li])

# directory中的解析
params.keys()

params.values()

params.items()

print([k for k,v in params.items()])

# list过滤
print([elem for elem in li if len(elem)>1])

print([elem for elem in li if li.count(elem)==1])
