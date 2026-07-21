import math
a,b,c = map(int,input("请输入三角形的三边: ").split())
p = (a+b+c)/2
S = math.sqrt(p*(p-a)*(p-b)*(p-c))
print(S)
print("三角形的面积是%.2f"%S)
# a,b,c = map(int,input().split()) i.e. a,b,c = map(int,input().split(' '))