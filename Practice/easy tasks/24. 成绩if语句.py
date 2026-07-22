# scores = [100,30,50,72,83,64,90,98]
scores = map(int,input("请输入成绩: ").split())
A = []
B = []
C = []

for i in scores:
    if i>=90:
        A.append(i)
    elif i>=60 and i<=89:
        B.append(i)
    elif i<60:
        C.append(i)
    else:
        print(f"Invalid Score: {i}")

print(f'A: {A}')
print(f'B: {B}')
print(f'C: {C}')