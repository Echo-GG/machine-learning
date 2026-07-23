def change(x):
    sum = 0
    while x != 0:
        temp = x % 10
        sum += temp * temp
        x //= 10
    return sum

def isHappy(x):
    while x >= 10:
        x = change(x)
    if x == 1:
        return True
    return False

n = int(input("请输入待判断的数: "))
print(isHappy(n))