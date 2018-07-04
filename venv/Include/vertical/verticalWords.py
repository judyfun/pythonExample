import queue

# q = queue.Queue()
q = queue.LifoQueue()

# put items at the end of the queue
# for x in range(4):
#     q.put("item-" + str(x))
#
# # remove items from the head of the queue
# while not q.empty():
#     print(q.get())

str = "静夜思 李白床前明月光，疑似地上霜。举头望明月，低头思故乡。"
q.put(str[:6])
q.put(str[6:12])
q.put(str[12:18])
q.put(str[18:24])
q.put(str[24:30])
while not q.empty():
    list = []
    str = q.get()
    list.append(str)
    for i in range(0,5):
        for k in list:
            print(k[i:i+1])






