character = str(input("请输入这个字符:"))
def isCharacter(character):
    if character <= 'Z' and character >= 'A' or character <= 'z' and character >= 'a':
        return True
    else:
        return False
# print(isCharacter(character))
flag = False
for ch in character:
    if(not isCharacter(ch)):
        print("No")
        flag = True
        break
if not flag:
    print("Yes")

# Another solution:
a = input("请输入这个字符")
result = a.isalpha()
if result:
    print(f'{a}是字母')
else:
    print(f'{a}不是字母')

# str(input()) i.e. input()
# isalpha()方法能够一次性检测一整个字符串,本例中的isCharacter()方法一次只能检测一个字符