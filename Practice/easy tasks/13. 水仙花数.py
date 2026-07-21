list = []
for i in range(100,1000):
    g = i%10
    s = i%100//10
    b = i//100
    if pow(g,3) + pow(s,3) + pow(b,3) == i:
        list.append(i)
print(list)