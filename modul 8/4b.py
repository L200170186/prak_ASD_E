import heapq
class PriorityQueue(object):
    def __init__(self):
        self.qlist = []
    def __len__(self):
        return len(self.qlist)
    def isEmpty(self):
        return len(self) == 0
    def enqueue(self,data,priority):
        heapq.heappush(self.qlist, (priority,data))
        self.qlist.sort()
    def dequeue(self):
        return self.qlist.pop(-1)
    def getFrontMost(self):
        return self.qlist[0]
    def getRearMost(self):
        return self.qlist[-1]
    
Q = PriorityQueue()
Q.enqueue(28, 7)
Q.enqueue(19, 4)
Q.enqueue(45, 1)
Q.enqueue(13, 8)
Q.enqueue(7, 3)
Q.enqueue(98, 6)
Q.enqueue(54, 9)

print(Q.getFrontMost())
print(Q.getRearMost())
print(Q.qlist)
