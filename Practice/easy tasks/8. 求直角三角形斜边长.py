from numpy import sqrt
a,b = map(float,(input("请输入直角三角形的两条直角边的长度:").split()))
c = pow(a,2) + pow(b,2)
c = sqrt(c)
print(f"直角三角形的斜边长为:{c}")