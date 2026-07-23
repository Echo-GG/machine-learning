# 给定一个字符串，请判断其中每个字符是否全都不同。

# Method 1:
def all_unique1(str):
    for i in range(len(str)-1):
        for j in range(i+1,len(str)):
            if str[i] == str[j]:
                return False
    return True

# Method 2:
def all_unique2(str):
    return len(set(str))==len(str)

# Method 3:
def all_unique3(str):
    for i in range(len(str)):
        if str[i] in str[i+1:]:
            return False
    return True

str = input("请输入一个字符串: ")
print(all_unique1(str))
print(all_unique2(str))
print(all_unique3(str))