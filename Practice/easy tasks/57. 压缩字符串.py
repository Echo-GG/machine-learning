# 利用字符串重复出现的次数，编写一种方法，实现基本的字符串压缩功能。比如，字符串aabcccccaaa会变成a2bc5a3。
# 1. 如果只有一个字符，1不用写;
# 2. 字符串中只包含大小写英文字母 (a~z and A~Z)

def func(s):
    list = []
    for i in s:
        if not list or list[-2] != i:
            list.append(i)
            list.append(1)
        else:
            list[-1] += 1
    return ''.join(map(str,[x for x in list if x != 1]))

s = input("请输入一个字符串: ")
print(func(s))