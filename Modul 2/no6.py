from no2 import Manusia
class siswaSMA(Manusia):
    jurusan = []
    universitas = []
    def __init__(self,nama,NISN,kota,kelas):
        self.nama = nama
        self.NISN = NISN
        self.kotaTinggal = kota
        self.kelas = kelas
    def __str__(self):
        s = self.nama + ', NISN ' + str(self.NISN) \
            + '. Tinggal di ' + self.kotaTinggal \
            + '. Kelas ' + str(self.Kelas) \
            + '. SMA.'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNISN(self):
        return self.NISN
    def ambilKelas(self):
        return self.kelas
    def ambilKotaTinggal(self):
        return self.kotaTinggal
    def perbaruiKotaTinggal(self, x):
        self.kotaTinggal = x
    def ambilJurusan(self, jur):
        self.jurusan.append(jur)
    def listJurusan(self):
        print(self.jurusan)
    def hapusJurusan(self, jur):
        return self.jurusan.remove(jur)
    def ambilUniversitas(self, unv):
        self.universitas.append(unv)
    def listUniversitas(self):
        print(self.universitas)
    def hapusUniversitas(self, unv):
        return self.universitas.remove(unv)    
sma = siswaSMA('nugroho',62288299,'solo',12)
