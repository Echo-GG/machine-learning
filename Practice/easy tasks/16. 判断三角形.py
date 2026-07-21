a,b,c = map(int,input("请输入待检测的三条边: ").split())
list = [a,b,c]
list.sort()
if a<=0 or b<=0 or c<=0:
    print("Input Error")
elif a+b<=c or c-a>=b:
    print("No")
else:
    print("Yes")

# Another solution:
a = int(input("请输入第一条边:"))
b = int(input("请输入第二条边:"))
c = int(input("请输入第三条边"))

if a<=0 or b<=0 or c<=0:
    print("输入数据不合法! ")
if a + b > c and a + c > b and b + c > a:
    print("这三条边可以是三角形的边长")
else:
    print("这三条边不可以是三角形的边长")