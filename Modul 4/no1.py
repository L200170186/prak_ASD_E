class mhsTIF():
    def __init__(self, nama, nim, kota, uangsaku):
        self.nama = nama
        self.nim = nim
        self.kota = kota
        self.uangsaku = uangsaku
c0 = mhsTIF('ika',10,'sukoharjo',240000)
c1 = mhsTIF('budi',51,'sragen',230000)
c2 = mhsTIF('ahmad',2,'surakarta',250000)
c3 = mhsTIF('chandra',18,'surakarta',234000)
c4 = mhsTIF('eka',4,'boyolali',240000)
c5 = mhsTIF('fandi',31,'salatiga',250000)
c6 = mhsTIF('deni',13,'klaten',245000)
c7 = mhsTIF('galuh',5,'wonogiri',245000)
c8 = mhsTIF('janto',23,'klaten',245000)
c9 = mhsTIF('hasan',64,'karanganyar',270000)
c10 = mhsTIF('khalid',29,'purwodadi',265000)

daftar = [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]

def carikota(n):
    ck = []
    for i in range(len(n)):
        if(n[i].kota.lower() == 'klaten'):
            ck.append(i)
    return ck

print(carikota(daftar))
