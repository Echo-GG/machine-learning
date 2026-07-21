def fact(num):
    if num == 1:
        return 1
    return num*fact(num-1)

number = int(input("请输入需要计算的数的阶乘:"))
res = fact(number)
print(f'{number}的阶乘是{res}')