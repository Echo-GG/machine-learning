def getHeight(h,times):
    Sum = 0
    temp = h
    for i in range(times):
        temp /= 2
        Sum += 3 * temp
    return [temp,Sum]
[h,times] = map(int,input("请输入初始高度和反弹次数: ").split())
[resHeight,Sum] = getHeight(h,times)
print(f'从高度{h}经过{times}次反弹：共经过{Sum}米，第{times}次反弹高度为：{resHeight}')