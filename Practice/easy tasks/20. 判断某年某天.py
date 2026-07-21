import datetime

year,month,day = map(int,input("请输入日期信息，年月日之间使用空格隔开: ").split(' '))
FirstDayofYear = datetime.datetime(year,1,1)
Today = datetime.datetime(year,month,day)
print((Today - FirstDayofYear).days + 1)
# print(Today)
