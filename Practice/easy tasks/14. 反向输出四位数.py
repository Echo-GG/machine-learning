number = int(input("请输入一个四位整数:"))
q = number//1000
b = number%1000//100
s = number%100//10
g = number%10//1
Number = g*1000+s*100+b*10+q
print(f"Reversed number of {number} is {Number}")

# Another solution:
a = int(input("请输入这个数字:"))
a = str(a)
a = a[::-1]
a = int(a)
print(a)