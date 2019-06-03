class simpulpohonbiner(object):
    def __init__(self, data):
        self.data=data
        self.kiri=None
        self.kanan=None

    def __str__(self):
        return str(self.data)

A=simpulpohonbiner('Ambarawa')
B=simpulpohonbiner('Bantul')
C=simpulpohonbiner('Cimahi')
D=simpulpohonbiner('Denpasar')
E=simpulpohonbiner('Enrekang')
F=simpulpohonbiner('Flores')
G=simpulpohonbiner('Garut')
H=simpulpohonbiner('Halmahera Timur')
I=simpulpohonbiner('Indramayu')
J=simpulpohonbiner('Jakarta')

A.kiri=B; A.kanan=C
B.kiri=D; B.kanan=E
C.kiri=F; C.kanan=G
E.kiri=H
G.kanan=I

datalist=[A.data, B.data, C.data, D.data, E.data, F.data, G.data, H.data, I.data, J.data]
level=[]

def traverse(root):
    lvlist=[]
    current_level = [root]
    lv=0
    while current_level:
        next_level = list()
        for n in current_level:
            if n.kiri:
                next_level.append(n.kiri)
                level.append(lv+1)
            if n.kanan:
                next_level.append(n.kanan)
                level.append(lv+1)
            current_level = next_level
            
        lv+=1
        lvlist.append(lv)
    return lvlist
        
def cetakdatadanlevel(root):
    traverse(A)
    print(root.data, ', Level 0')
    for i in range(len(level)):
          print(datalist[i+1], ', Level', level[i])

cetakdatadanlevel(A)

