from no2 import Manusia
class mahasiswa(Manusia):
    """Class Mahasiswa yang dibangun dari class Manusia."""
    matkul = []
    def __init__(self,nama,NIM,kota,us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia."""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama + ', NIM ' + str(self.NIM) \
            + '. Tinggal di ' + self.kotaTinggal \
            + '. Uang Saku Rp ' + str(self.uangSaku) \
            + '. tiap bulanya.'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self, s):
        """metode ini menutupi metode 'makan'-nya class Manusia.
        Mahasiswa kalau makan sambil belajar."""
        print("Saya baru saja makan",s,"sambil balajar")
        self.keadaan = 'kenyang'
    def ambilKotaTinggal(self):
        return self.kotaTinggal
    def perbaruiKotaTinggal(self, x):
        self.kotaTinggal = x
    def tambahUangSaku(self,x):
        self.uangSaku += x
    def ambilKuliah(self, mk):
        self.matkul.append(mk)
    def listKuliah(self):
        print(self.matkul)
m234 = mahasiswa('nugroho',186,'solo',100000)
