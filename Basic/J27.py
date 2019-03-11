with open("E:\\git\\PythonExamples2019\\text.txt","wt") as out_file:
    out_file.write("该文本会写入到文件中\n看到我了吧")

with open("E:\\git\\PythonExamples2019\\text.txt","rt") as in_file:
    text=in_file.read()

print(text)
