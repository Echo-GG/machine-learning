def func(s):
    l = s.split(' ')
    # print(l)
    l = l[::-1]
    s = ''
    for i in l:
        i = i.swapcase()
        s += i
        s += ' '
    return s[0:len(s)-1] # 去掉末尾空格
s = input("请输入一个字符串: ")
print(func(s)) 