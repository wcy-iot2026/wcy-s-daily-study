# 需求:定义一个名为 TextFileHandler 的类，支持文本文件的读取和写入
class TextFileHandler:
    def __init__(self, filename):
        # 保存要读写的文件路径
        self.filename = filename

    # 读取整个文件；文件不存在时给出提示
    def read_file(self):
        try:
            # r：只读，utf-8：按中文编码打开
            with open(self.filename, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            print(f"文件{self.filename}不存在")

    # 把内容追加到文件末尾；文件不存在会自动创建
    def write_file(self, content):
        # a：追加写入，不会清空原来的内容
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(content)


# 创建实例，文件保存在 python练习 文件夹
handler = TextFileHandler(r"d:\学习\python练习\示例.txt")
handler.write_file("你好，这是写入的文本。\n")
print(handler.read_file())
