from math import sqrt
a = int(input("请输入闭区间的左端点:"))
b = int(input("请输入闭区间的右端点:"))

def isPrime(number):
    if number == 2:
        return True
    if number % 2==0:
        return False
    limit = int(sqrt(number)) + 1
    for i in range(3,limit,2):
        if number % i ==0 :
            return False
    return True

res = []

for i in range (a,b+1):
    if isPrime(i):
        res.append(i)
print(res)
