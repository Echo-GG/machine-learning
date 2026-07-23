import random

target = random.randint(1,99)
times = 7
print('猜数字游戏开始, 请猜100以内的整数~')
flag = False
while times != 0:
    num = int(input('请输入你要猜的数字: \n'))
    if num > target:
        print('你猜的数字有点大, 请继续猜! \n')
        times -= 1
        print('你还剩',times,'次机会!\n')
        continue
    elif num < target:
        print('你猜的数字有点小, 请继续猜! \n')
        times -= 1
        print('你还剩',times,'次机会!\n')
        continue
    else:
        print('恭喜你! 猜对了, 正确答案是',target)
        flag = True
        break
if flag == False:
    print("你失败了!")