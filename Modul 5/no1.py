from b import mahasiswa
import sys
c0 = mahasiswa('ika',10,'sukoharjo',240000)
c1 = mahasiswa('budi',51,'sragen',230000)
c2 = mahasiswa('ahmad',2,'surakarta',250000)
c3 = mahasiswa('chandra',18,'surakarta',234000)
c4 = mahasiswa('eka',4,'boyolali',240000)
c5 = mahasiswa('fandi',31,'salatiga',250000)
c6 = mahasiswa('deni',13,'klaten',245000)
c7 = mahasiswa('galuh',5,'wonogiri',245000)
c8 = mahasiswa('janto',23,'klaten',245000)
c9 = mahasiswa('hasan',64,'karanganyar',270000)
c10 = mahasiswa('khalid',29,'purwodadi',265000)

daftar = [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]

def mengurutkan(n):
    baru = {}
    for i in range(len(n)):
        baru [n[i].nama,n[i].kotaTinggal,n[i].uangSaku] = n[i].NIM
    listofTuples = sorted(baru.items(), key=lambda x: x[1])
    for elem in listofTuples :
        print (elem[1] ,":", elem[0])


mengurutkan(daftar)
