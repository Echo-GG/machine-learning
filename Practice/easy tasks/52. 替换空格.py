# 将字符串中的空格替换为'%'

str = input("请输入一个字符串: ")

# Python和Java中的字符串都是不可变对象，想更改就新建一个:

# Method 1:
str = str.replace(' ','%')
print(str)

# Method 2:
chars = list(str)
for i in range(len(str)):
    if chars[i] == ' ':
        chars[i] = '%'
str = ''.join(chars)
print(str)

# Method 3:
def func(s):
    res = ''
    for i in s:
        if i != ' ':
            res += i
        else:
            res += '%'
    return res

print(func(str))
