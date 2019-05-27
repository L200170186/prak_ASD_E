class PriorityQueue():

    def __init__(self):
        self.qlist = []

    def __len__(self):
        return len(self.qlist)

    def isEmpty(self):
        return len(self) == 0

    def enqueue(self, data, priority):
        entry = _PriorityQEntry(data, priority)
        self.qlist.append(entry)

    def dequeue(self):
        A = []
        for i in self.qlist:
            A.append(i)

        c = 0
        for i in range (1, len(self.qlist)):
            if A[i].priority < A[c].priority:
                c = i

        hasil = self.qlist.pop(c)
        return hasil.item
    
class _PriorityQEntry():
    def __init__(self, data, priority):
        self.item = data
        self.priority = priority

p=PriorityQueue()
p.enqueue("jeruk",4)
p.enqueue("tomat",2)
p.enqueue("mangga",0)
p.enqueue("duku",5)
p.enqueue("pepaya",2)

print(p.dequeue())
print(p.dequeue())
print(p.dequeue())
print(p.dequeue())
print(p.dequeue())

