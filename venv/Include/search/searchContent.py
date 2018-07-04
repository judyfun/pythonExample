import os;
import fnmatch;
import re;

findPath = "D:\project\project1\python\example"


def findCotent(path, content):
    temAll = []
    for root, dirs, files in os.walk(findPath):
        for name in files:
            start, splitext = os.path.splitext(name)
            filePath = os.path.join(root, name)
            if fnmatch.fnmatch(splitext, '*.py'):
                with  open(filePath) as file:
                    try:
                        data = file.readlines()
                        for i in data:
                            if re.findall(content, i):
                                temAll.append(filePath)
                    except:
                        print("except: " + filePath)

    return temAll


print(findCotent(findPath, 'except'))
