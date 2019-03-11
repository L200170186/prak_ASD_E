class Pesan(object):
    """
        Sebuah class bernama Pesan.
        Untuk memahami konsep Class dan Object.
    """
    def __init__(self, sebuahString):
        self.teks = sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))
    def jumKar(self):
        return len(self.teks)
    def cetakJumlahKarakterku(self):
        print('Kalimatku mampunyai',len(self.teks),'karakter.')
    def perbarui(self,stringBaru):
        self.teks = stringBaru

    def apakahTerkandung(self, teks):
        if str(teks) in self.teks:
            print("true")
        else:
            print("false")
    def hitungKonsonan(self):
        v = "aiueoAIUEO"
        x = 0
        for i in self.teks:
            if i not in v:
                x+=1
        return x

    def hitungVokal(self):
        v = "aiueoAIUEO"
        x = 0
        for i in self.teks:
            if i in v:
                x+=1
        return x

