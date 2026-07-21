from math import sqrt
factors = []

def isPrime(n):
    if n==2:
        return True
    if n%2==0:
        return False
    limit = int(sqrt(n)) + 1
    for i in range(3,limit,2):
        if n%i ==0:
            return False
    return True

def FindPrimeFactor(n):
    if n == 1:
        return
    for i in range(2, n + 1):
        if n % i == 0 and isPrime(i):  
            factors.append(i)
            FindPrimeFactor(n // i)     
            break                      

number = int(input("请输入一个正整数: "))
FindPrimeFactor(number)

print(factors)

# Another solution:
a = int(input("请输入一个自然数: "))
list = []
factor = 2
while a != factor:
    if a % factor == 0:
        list.append(factor)
        a = a // factor
    else:
        factor = factor + 1
list.append(a)
print(list)