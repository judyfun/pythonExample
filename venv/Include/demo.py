import re, fnmatch, sys, MsgHandle

str = '13013013130'
str1 = "身份证:13013013130"
msg = re.findall(r'身份证', str1)
print(msg)

if msg:
    print('yes')
else:
    print('no')


def age(n):
    if n == 1:
        return 18
    return age(n - 1) + 2


print(age(7))

str = "adfad"
print(str[0:1])

if re.findall('temp', 'print(aaa)'):
    print('yes')
else:
    print('no')

fnmatch_fnmatch = fnmatch.fnmatch('123.py', '*.py')
print(fnmatch_fnmatch)

print('lala' * 4)
print(2 ** 4)
print(9 // 4)

print('============')
a = input("你说啥:")
print(a)


def printMax(x, y):
    '''Prints the maximun of two  numbers.

    The tow values must be integers.'''
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')


printMax(3, 5)
print(printMax.__doc__)

for i in sys.argv:
    print(i)
print('===========')

print(dir(sys))
print(dir())