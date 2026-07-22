str = input("请输入一行字符: ")
Characters = []
Spaces = []
Numbers = []
Others = []

for s in str:
    if (s>='a' and s<='z' or s>='A' and s<='Z'):
        Characters.append(s)
    elif (s==' '):
        Spaces.append(s)
    elif (s>='0' and s<='9'):
        Numbers.append(s)
    else:
        Others.append(s)

def getSize(list):
    count = 0
    for i in list:
        count = count + 1
    return count

print(f'Characters: \nTotal elements: {getSize(Characters)}\nElements: {Characters}\n')
print(f'Spaces: \nTotal elements: {getSize(Spaces)}\n')
print(f'Numbers: \nTotal elements: {getSize(Numbers)}\nElements: {Numbers}\n')
print(f'Others: \nTotal elements: {getSize(Others)}\nElements: {Others}\n')

# Another solution:
char = 0
number = 0
space = 0
other = 0

string = input("请输入一串字符: ")
for i in string:
    if i.isalpha():
        char += 1
    elif i.isdigit():
        number += 1
    elif i.isspace():
        space += 1
    else:
        other += 1
print(f'英文字母有{char}个，数字有{number}个，空格有{space}个，其他字符有{other}个。')