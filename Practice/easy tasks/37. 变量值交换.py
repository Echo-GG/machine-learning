a,b = map(int,input("请输入两个变量: ").split())
print(f'交换前: {a},{b}')
temp = a
a = b
b = temp
print(f'交换后: {a},{b}')

# Another solution: 
a,b = b,a
print(a,b)