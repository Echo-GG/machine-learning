date = input("请输入第一个字母: ")
if date == 'M':
    print("Monday")
elif date == 'W':
    print("Wednesday")
elif date == 'F':
    print("Friday")
elif date == 'T':
    date2 = input("请输入第二个字母: ")
    if date2 == 'u':
        print("Tuesday")
    elif date2 == 'h':
        print("Thursday")
elif date == 'S':
    date2 = input("请输入第二个字母: ")
    if date2 == 'a':
        print("Saturday")
    elif date2 == 'u':
        print("Sunday")
else:
    print("Input Error!")