arr = []
for i in range (1,4):
    number = float(input(f"请输入待比较的数{i}:"))
    arr.append(number)
arr.sort()
print(f"从小到大依次是:{arr}")
