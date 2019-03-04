import random
def game():
    a=random.randrange(0, 100)
    print ("permainan tebak angka")
    print ("Saya menyimpan sebuah angka bulat antara 1 sampai 100. coba tebak.")
    while(True):
        b=int(input("masukan angka: "))
        if(b>a):
            print("terlalu besar, coba lagi")
        elif(b<a):
            print("terlalu kecil, coba lagi")
        else:
            print("benar")
            break
game()
