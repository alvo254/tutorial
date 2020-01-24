class Queue:
    def __init__(self, contents):
        self._hiddenlist=list(contents)

    def push(self, value):
        self._hiddenlist.insert(0, value)

    def pop(self):
        return self._hiddenlist.pop(-1)

    def __rep__(self):
        return"Queue({})".format(self._hiddenlist)


queue = Queue([1, 2, 3, 4])
print(queue)
queue.push(0)
queue.pop()
print(queue)
print(queue._hiddenlist)
