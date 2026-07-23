# 给定一个长度为n的无序数组，包含正数、负数和0，请从中找出3个数，使得乘积最大，返回这个乘积:
def func(list):
    list.sort()
    return max(list[0]*list[1]*list[-1],list[-1]*list[-2]*list[-3])
print(func([0,34,-1,45]))