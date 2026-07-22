a = []
sum = 0
for i in range(3):
    a.append([])
    for j in range(3):
        x = int(input("请输入元素: "))
        a[i].append(x)
        if i == j:
            sum += a[i][j]
print(a)
print(sum)