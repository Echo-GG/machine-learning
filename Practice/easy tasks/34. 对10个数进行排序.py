x = input("请输入10个数: ")
arr = x.split()
arr = [int(arr[i]) for i in range(len(arr))]
arr.sort()
print(arr)


# Anohter solution:
a = map(int,input("请输入10个数: ").split())
a = list(a)
a.sort(reverse=False) # 升序（默认）
a.sort(reverse=True) # 降序
print(a)