# 将一个列表的数据复制到另一个列表中:
def CopyList(list):
    newlist = []
    for i in list:
        newlist.append(i)
    return newlist

list1 = [1,2,3,4,5]
list2 = CopyList(list1)
print(list2)

# Another solution:
import copy

list = [1,2,3,4]
list1 = copy.copy(list)
print(list1)

copiedlist = input("请输入原列表信息".split(' '))
print(copy.copy(copiedlist))