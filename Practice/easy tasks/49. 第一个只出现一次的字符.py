# 在一个字符串中找到第一个只出现一次的字符,并返回它的位置,如果没有则返回-1(需要区分大小写)(从0开始计数)
str = 'Hello World!' #0
# str = 'ddhh' # -1
a = -1
mp = dict()

for i in str:
    if i in mp:
        mp[i] += 1
    else:
        mp[i] = 1

for i in range(len(str)):
    if mp[str[i]] == 1:
        a = i
        break
print(a)