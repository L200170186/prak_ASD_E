from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from tkinter import filedialog
from tkinter import *
import subprocess
import os
import sys
from asdd import *
import pygame

root = Tk()
root.withdraw()

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.folder = []
        self.file = []
        self.daftar = ""
        self.index = 0
        self.a = 0
    
        self.tanda = 0
        self.folderCari = []
        self.fileCari = []

        self.open.clicked.connect(self.tambah)
        self.pushButton_2.clicked.connect(self.cari)
        self.pushButton_7.clicked.connect(self.urut)
        self.pushButton.clicked.connect(self.hapus)
        self.pushButton_3.clicked.connect(self.putar)
        self.pushButton_5.clicked.connect(self.lanjut)
        self.pushButton_6.clicked.connect(self.sebelum)
        self.pushButton_4.clicked.connect(self.pause)

        
    def pause(self):
        if self.a==0:
            pygame.mixer.music.pause()
            self.a=1
        else:
            pygame.mixer.music.unpause()
            self.a=0
            
            
    def tambah(self):
        self.daftar = ''
        openfile = filedialog.askopenfilenames(parent=root,title='pilih file')
        file = root.tk.splitlist(openfile)
        for i in range(len(file)):
            self.folder.append(file[i])
            self.file.append(os.path.basename(file[i]))
        for i in range(len(self.file)):
            self.daftar = self.daftar + self.file[i] + "\n"
        self.textEdit.setText(self.daftar)

    def cari(self):
        self.tanda = 1
        self.daftar = ''
        self.folderCari = []
        self.fileCari = []
        target = self.lineEdit.text()
        for i in range(len(self.file)):
            if target.lower() in self.file[i].lower():
                self.folderCari.append(self.folder[i])
                self.fileCari.append(self.file[i])
                self.daftar = self.daftar + self.file[i] + "\n"
        self.textEdit.setText(self.daftar)
        
    def urut(self):
        self.tanda = 0
        self.daftar = ""
        for i in range(len(self.file)):
            for j in range(0, len(self.file)-i-1):
                if self.file[j] > self.file[j+1]:
                    self.file[j], self.file[j+1] = self.file[j+1],self.file[j]
                    self.folder[j], self.folder[j+1] = self.folder[j+1],self.folder[j]
        for i in range(len(self.file)):
            self.daftar = self.daftar + self.file[i] + "\n"
        self.textEdit.setText(self.daftar)

    def hapus(self):
        self.daftar = ""
        self.file.pop()
        self.folder.pop()
        for i in range(len(self.file)):
            self.daftar = self.daftar + self.file[i] + "\n"
        self.textEdit.setText(self.daftar)

    def putar(self):
        if self.tanda==0:
            self.index = 0
            pygame.mixer.init()
            pygame.mixer.music.load(self.folder[self.index])
            pygame.mixer.music.play()
        else:
            self.index = 0
            pygame.mixer.init()
            pygame.mixer.music.load(self.folderCari[self.index])
            pygame.mixer.music.play()
            
    def lanjut(self):
        try:
            if self.tanda==0:
                self.index += 1
                pygame.mixer.init()
                pygame.mixer.music.load(self.folder[self.index])
                pygame.mixer.music.play()
            else:
                self.index += 1
                pygame.mixer.init()
                pygame.mixer.music.load(self.folderCari[self.index])
                pygame.mixer.music.play()
        except:
            self.index = -1
            if self.tanda==0:
                self.index += 1
                pygame.mixer.init()
                pygame.mixer.music.load(self.folder[self.index])
                pygame.mixer.music.play()
            else:
                self.index += 1
                pygame.mixer.init()
                pygame.mixer.music.load(self.folderCari[self.index])
                pygame.mixer.music.play()


    def sebelum(self):        
        try:
            if self.tanda==0:
                self.index -= 1
                pygame.mixer.init()
                pygame.mixer.music.load(self.folder[self.index])
                pygame.mixer.music.play()
            else:
                self.index -= 1
                pygame.mixer.init()
                pygame.mixer.music.load(self.folderCari[self.index])
                pygame.mixer.music.play()
        except:
            
            if self.tanda==0:
                self.index = len(self.folder)-1
                self.index += 1
                pygame.mixer.init()
                pygame.mixer.music.load(self.folder[self.index])
                pygame.mixer.music.play()
            else:
                self.index = len(self.folderCari)-1
                self.index += 1
                pygame.mixer.init()
                pygame.mixer.music.load(self.folderCari[self.index])
                pygame.mixer.music.play()
        

if __name__ == "__main__":
    a = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    a.exec_()

