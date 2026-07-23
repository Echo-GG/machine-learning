from gmpy2 import iroot

a = int(input("请输入一个正整数: "))
res1 = iroot(a,3)
res2 = pow(a,1/3)
print(res1,"\n",res2)