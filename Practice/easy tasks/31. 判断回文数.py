
def Reverse(str):
    stack = []
    for i in str:
        stack.append(i)
    res = ""
    while len(stack)!=0:
        ele = stack[-1]
        res += ele
        stack.pop()
    return res

def isPalindrome():

    str = input("请输入一个字符串: ")
    str_ = (Reverse(str))
    print(str_)
    if(int(str) == int(str_)):
        return True
    
    return False

if isPalindrome():
    print("Yes")
else:
    print("No")

# Another solution:
a = int(input("请输入数字: "))
a = str(a)
b = a[::-1]
if a == b:
    print("是回文数")
else:
    print("不是回文数")