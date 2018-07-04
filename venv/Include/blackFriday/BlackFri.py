import time;
import calendar;

ticks = time.time()
print(ticks)

localtime = time.localtime(time.time())
print(localtime)

ltime = time.asctime(time.localtime(time.time()))
print(ltime)

print(time.strftime('%Y-%m-%d %H-%M-%S', time.localtime()))

cal = calendar.month(2016, 1)
print(cal)

c = calendar.weekday(2016, 1, 13)
print(c)

print('请输入年份')


def isBlack(year):
    for i in range(1, 13):
        if ((calendar.weekday(year, i, 13)) == 4):
            print(str(year) + str(i) + "13")


isBlack(2046)