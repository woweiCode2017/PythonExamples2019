# Python有三种方法解析XML, SAX, DOM, ElementTree

# SAX(simple API for XML)
# 1. Python标准库包含SAX解析器，SAX用事件驱动模型，通过在解析XML的过程中触发一个个的事件并调用用户定义的回调函数来处理XML文件。

# DOM (Document Object Model)
# 将XML数据在内存中解析成一个树，通过对树的操作来操作XML


# SAX是一种基于事件驱动的API，利用SAX解析XML文档牵涉到两个部分：解析器和事件处理器
# 解析器负责读取XML文档，并向事件处理器（ContentHandler）发送事件。

import xml.sax


class MovieHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.type = ""
        self.format = ""
        self.year = ""
        self.rating = ""
        self.stars = ""
        self.description = ""

    # 元素开始时调用
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "movie":
            print("*****Movie*****")
            title = attributes["title"]
            print("Title:", title)

    # 元素结束时调用
    def endElement(self, tag):
        if self.CurrentData == "Type":
            print("Type:", self.type)
        elif self.CurrentData == "format":
            print("Format:", self.format)
        elif self.CurrentData == "year":
            print("Year:", self.year)
        elif self.CurrentData == "rating":
            print("Rating:", self.rating)
        elif self.CurrentData == "stats":
            print("Stars:", self.stats)
        elif self.CurrentData == "description":
            print("Description:", self.description)

    # 读取字符时调用
    def characters(self, content):
        if self.CurrentData == "type":
            self.type = content
        elif self.CurrentData == "format":
            self.format = content
        elif self.CurrentData == "year":
            self.year = content
        elif self.CurrentData == "rating":
            self.rating = content
        elif self.CurrentData == "stars":
            self.stars = content
        elif self.CurrentData == "description":
            self.description = content


if __name__ == "__main__":

    # 创建一个XMLReader
    parser = xml.sax.make_parser()
    # 关闭命名空间啊
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # 重写 ContentHandler
    Handler = MovieHandler()
    parser.setContentHandler(Handler)

    parser.parse("movies.xml")


# 使用xml.dom解析xml
# 一个DOM的解析器在解析一个XML文档时，一次性读取整个文档，把文档中所有元素保存在内存中的一个树结构里。

from xml.dom.minidom import parse
import xml.dom.minidom

# 使用minidom解析器打开XML文档
DomTree = xml.dom.minidom.parse("movies.xml")
collection = DomTree.documentElement
if collection.hasAttribute("shelf"):
    print("Root element: %s"% collection.getAttribute("shelf"))

# 在集合中获取所有电影
movies = collection.getElementsByTagName("movie")

# 打印每部电影的详细信息
for movie in movies:
    print("*****Movie*****")
    if movie.hasAttribute("title"):
        print("Title: %s" % movie.getAttribute("title"))

    movieType = movie.getElementByTagName('type')[0]
    print("Type: %s" % movieType.childNodes[0].data)
    movieFormat = movie.getElementByTagName('format'[0])
    print("Format: %s" % movieFormat.chileNodes[0].data)
    movieRating = movie.getElementByTagName('rating')[0]
    print("Rating: %s" % movieRating.childNodes[0].data)
    movieDescription = movie.getElementByTagName('description')[0]
    print("Description: %s" % movieDescription.chileNodes[0].data)

