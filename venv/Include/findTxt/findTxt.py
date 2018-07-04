import os;
import fnmatch;

print(os.getcwd())
result = os.listdir('d://')


def txt(path):
    for root, dirs, files in os.walk(path, topdown=True):
        txtlist = []
        for name in files:
            if (fnmatch.fnmatch(name, '*.txt\\Z')):
                print(os.path.join(root, name))
                if fnmatch.fnmatch(name, "*.txt"):
                    txtlist.append(os.path.join(root, name))

    return txtlist


txt('D:\project\project1\python');
