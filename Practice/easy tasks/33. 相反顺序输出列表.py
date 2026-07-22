x = input("请输入数字: ")
list = x.split(',')

list = [int(list[i]) for i in range(len(list))] 
# 将字符串整型化: 
# e.g. ['4', '3', '2', '1'] --> [4, 3, 2, 1]

list_ = list[::-1]
list.reverse()
print(list)
print(list_)