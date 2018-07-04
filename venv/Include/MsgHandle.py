import re

sourcePath = 'msg.txt'
targetPath = 'msg-target.txt'
phoneRex = r'手机号'
idCardRex = r'身份证号'

sourceFile = open(sourcePath, 'r', 1024, 'utf-8')
targetFile = open(targetPath, 'w', 1024, 'utf-8')

##数据
sourceData = sourceFile.readlines()
print(sourceData)


def handleData(data):
    strList = []
    for i in data:
        if re.findall(phoneRex, i):
            phoneNum = re.findall(r'1\d{10}', i)
            s = i[:4] + ': ' + phoneNum[0][:3] + "****" + phoneNum[0][7:11]
            print(s)
            strList.append(s)

        elif re.findall(idCardRex, i):
            idCardNum = re.findall(r'\d{18}|\d{17}X', i)
            k = i[:4] + ": " + idCardNum[0][:5] + "**********" + idCardNum[0][15:]
            print(k)
            strList.append(k)

        else:
            strList.append(i)

    return strList


msgList = handleData(sourceData)
print(msgList)
for m in msgList:
    targetFile.write(m)
