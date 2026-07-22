list = [1,3,8,20,40]
list.reverse()
n = int(input("请输入数据: "))
list.append(n)
if list[0]<list[1]:
    list.sort()
else:
    list.sort(reverse=True)
print(list)
# 默认列表元素不重复且数量大于1