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


def ukuranpohon(akar):
    if akar is None: 
        return 0
    else: 
        return (ukuranpohon(akar.kiri)+ 1 + ukuranpohon(akar.kanan))

print('Ukuran dari Binary Tree adalah', ukuranpohon(A))
