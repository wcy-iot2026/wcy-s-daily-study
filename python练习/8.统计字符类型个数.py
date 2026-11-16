"""统计字符串中各类字符个数：字母、数字、空格、其他字符
isalpha()判断是否为字母
isdigit()判断是否为数字
isspace()判断是否为空格"""
s = input("请输入一行字符：")
letters = 0
digits = 0
spaces = 0
others = 0
for i in s:
    if i.isalpha():
        letters += 1
    elif i.isdigit():
        digits += 1
    elif i.isspace():
        spaces += 1
    else:
        others += 1

print(f"字母：{letters}")
print(f"数字：{digits}")
print(f"空格：{spaces}")
print(f"其他：{others}")
