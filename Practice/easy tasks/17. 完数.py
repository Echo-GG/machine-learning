def isComplete(n):
    result = 0
    for i in range(1,n):
        if(n%i==0):
            result = result + i
    if result == n:
        return True
    else:
        return False

res = []
for i in range(1001):
    if isComplete(i):
        res.append(i)
print(res)