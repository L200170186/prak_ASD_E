tahun=int(input("Masukkan Tahun untuk mengetahui kabisat atau tidak:"))
if(tahun%4==0 and tahun%100!=0 or tahun%400==0):
    print ("True")
else:
    print ("False")

