row = 1
col = 1
print(f'{row}*{col}={row*col}')
while row<=9:
    col = 1
    row = row + 1
    while(col<=row):
        print(f'{row}*{col}={row*col}',end = " ")
        col = col + 1
    print(end = "\n")

# Another solution:
for i in range(1,10):
    print(end='\n')
    for j in range(1,i+1):
        print(f'\t{i}*{j}={i*j}',end=' ')

# print() i.e. print(end = '\n')