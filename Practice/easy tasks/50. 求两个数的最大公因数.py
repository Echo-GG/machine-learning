def gcd(a,b):
    a,b = abs(a),abs(b)
    while(b != 0):
        a,b = b,a%b
    return a
a,b = map(int,input("请输入两个数: ").split())
res = gcd(a,b)
print(res)

# Another solution:

def GCD(a,b):
    a,b = abs(a),abs(b)
    if a == b:
        return a
    num = min(a,b)
    while a % num != 0 or b % num != 0:
        num -= 1
    return num
print(GCD(a,b))