# 华氏温度 = 摄氏温度 × 1.8 + 32
op = int(input("摄氏度转华氏度请按1，华氏度转摄氏度请按2: "))
if op == 1:
    a = float(input("请输入待转换的摄氏温度: "))
    print(f'对应的华氏温度: {a*1.8+32}')
elif op == 2:
    b = float(input("请输入待转换的华氏温度: "))
    print(f'对应的摄氏温度: {(b-32)/1.8}')
else:
    print("Invalid operation code!")