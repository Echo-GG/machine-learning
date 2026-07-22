def Fibonaci(n):
    if n == 1 or n == 2:
        return 1
    return Fibonaci(n-1) + Fibonaci(n-2)

n = int(input("寻找第n项: "))
print(f'第{n}项是: {Fibonaci(n)}')

# Another solution: 
# 非递归:
fibs = [1,1]
for i in range(2,n+1):
    fibs.append(fibs[i-1]+fibs[i-2])
print(fibs[n-1])