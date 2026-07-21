from numpy import sqrt
def isPrime(num):
    if(num==2):
        return True
    if(num%2==0):
        return False
    limit = int(sqrt(num)) + 1
    for i in range(3,limit,2):
        if num%i==0:
            return False
    return True

number = int(input("请输入需要判断的数字:"))
# print(type(number))
if isPrime(number):
    print("Yes")
else:
    print("No")