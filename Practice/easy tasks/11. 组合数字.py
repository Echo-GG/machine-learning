arr = [1,2,3,4]
temp = [1,2,3,4]
count = 0
list = []
for i in arr:
    temp = [1,2,3,4]
    b = i
    temp.remove(b)
    for j in temp:
        temp = [1,2,3,4]
        temp.remove(b)
        s = j
        temp.remove(s)
        for k in temp:
            temp = [1,2,3,4]
            temp.remove(i)
            temp.remove(j)
            g = k
            count = count + 1
            number = g + s*10 + b*100
            list.append(number)
print(count)
print(list)

# Another solution:
cnt = 0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i!=j) and (i!=k) and (j!=k):
                print(f'{i}{j}{k}')
                cnt = cnt+1

print(f'总个数:{cnt}')