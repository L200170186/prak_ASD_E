class Queue():
    def __init__(self):
        self.qlist = []
    def is_empty(self):
        return len(self) == 0
    def __len__(self):
        return len(self.qlist)
    def enqueue(self, data):
        self.qlist.append(data)
    def dequeue(self):
        assert not self.is_empty(), 'Antrian sedang kosoong'
        return self.qlist.pop(0)
    def getFrontMost(self):
        assert not self.is_empty(), 'Antrian sedang kosoong'
        return self.qlist[0]
    def getRearMost(self):
        assert not self.is_empty(), 'Antrian sedang kosoong'
        return self.qlist[-1]

Q = Queue()
Q.enqueue(28)
Q.enqueue(19)
Q.enqueue(45)
Q.enqueue(13)
Q.enqueue(7)
Q.enqueue(98)
Q.enqueue(54)

print(Q.getFrontMost())
print(Q.getRearMost())
print(Q.qlist)
