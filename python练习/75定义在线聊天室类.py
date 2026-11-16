# 需求:定义一个简单的在线聊天室类
class ChatRoom:
    def __init__(self):
        # users 保存已加入的用户，messages 保存发出的消息
        self.users = []
        self.messages = []

    # 添加用户；已经在聊天室里就不再添加
    def add_user(self, name):
        if name in self.users:
            print("用户已存在")
            return "用户已存在"
        self.users.append(name)
        print(f"{name}加入聊天室")
        return f"{name}加入聊天室"

    # 用户发一条消息；没加入聊天室就不能发
    def send_message(self, name, content):
        if name not in self.users:
            print("用户不存在")
            return
        message = f"{name}: {content}"
        self.messages.append(message)
        print(message)

    # 按顺序显示全部消息
    def show_messages(self):
        if not self.messages:
            print("暂无消息")
            return
        for message in self.messages:
            print(message)


# 调用示例
room = ChatRoom()
room.add_user("张三")
room.add_user("张三")  # 第二次添加，会提示用户已存在
room.add_user("李四")
room.send_message("张三", "你好")
room.send_message("李四", "你好，张三")
print("全部消息：")
room.show_messages()
