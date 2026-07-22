def getSum(n):
    list = []
    p = [2,3]
    q = [1,2]

    for i in range(2,n):
        Q = q[i-2] + q[i-1]
        q.append(Q)

    for i in range(2,n):
        P = p[i-1] + q[i-1]
        p.append(P)    

    for i in range(0,n):
        ele = p[i]/q[i]
        list.append(ele)

    sum = 0
    for i in list:
        sum += i
    for i in list:
        print(i)
    return sum

N = int(input("计算前N项的和: "))

sum = getSum(N)
print(f'前{N}项的和: {sum}')

# Another solution:
sum = 0
up = 2
down = 1

for i in range(N):
    sum += up/down
    temp = down
    down = up
    up = up + temp
print(sum)