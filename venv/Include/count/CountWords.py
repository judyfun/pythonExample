import operator

str = 'History is his story.'


def count(words):
    myDict = {}
    length = len(words)
    print(length)
    for i in words:
        if myDict.get(i):
            myDict[i] += 1
        else:
            # 如果为空，则放入1
            myDict[i] = 1

    # 第一种排序
    sorted_x = sorted(myDict.items(), key=operator.itemgetter(1))
    print(type(sorted_x))
    x = dict(sorted_x)

    # 第二种排序
    sorted_by_value = sorted(myDict.items(), key=lambda kv: kv[1])
    print(type(sorted_by_value))

    for i in sorted_x:
        print(i)


count(str)
