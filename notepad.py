import sys
import os
from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout,QFileDialog,QHBoxLayout
from PyQt5.QtWidgets import QAction,qApp,QMainWindow

class Pencere(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.yazi_alani = QTextEdit()
        self.temizle = QPushButton("Temizle")
        self.aç = QPushButton("Aç")
        self.kaydet = QPushButton("Kaydet")

        h_box = QHBoxLayout()

        h_box.addWidget(self.temizle)
        h_box.addWidget(self.aç)
        h_box.addWidget(self.kaydet)

        v_box = QVBoxLayout()
        v_box.addWidget(self.yazi_alani)
        v_box.addLayout(h_box)

        self.setLayout(v_box)

        self.setWindowTitle("Ahmet'in Notepad Uygulaması")
        self.setGeometry(250,50,500,300)

        self.temizle.clicked.connect(self.yaziyi_temizle)
        self.aç.clicked.connect(self.dosya_ac)
        self.kaydet.clicked.connect(self.dosya_kaydet)


    def yaziyi_temizle(self):
        self.yazi_alani.clear()

    def dosya_ac(self):

        dosya_ismi =QFileDialog.getOpenFileName(self,"Meyaba Yeni Dosya Açıyoruzz",os.getenv("Desktop"))
        with open(dosya_ismi[0],"r",encoding="UTF-8") as file:
            self.yazi_alani.setText(file.read())


    def dosya_kaydet(self):
        dosya_yolu = QFileDialog.getSaveFileName(self,"Dosyayı nereye kaydedlim Alperr?",os.getenv("Desktop"))

        with open(dosya_yolu[0],"w",encoding="UTF-8") as file:

            file.write(self.yazi_alani.toPlainText())

class Main(QMainWindow):
    def __init__(self):

        super().__init__()
        self.pencere = Pencere()
        self.setCentralWidget(self.pencere)

        self.menuleri_olustur()

    def menuleri_olustur(self):

        menu_bar = self.menuBar()
        dosya = menu_bar.addMenu("Dosya")
        self.setWindowTitle("Metin Editörü")
        self.show()

        dosya_ac = QAction("Dosya Aç",self)
        dosya_ac.setShortcut("Ctrl+O")

        dosya_kaydet = QAction("Dosya Kaydet",self)
        dosya_kaydet.setShortcut("Ctrl+S")

        cikis = QAction("Çıkış",self)
        cikis.setShortcut("Ctrl+W")

        temizle = QAction("Temizle",self)     
        temizle.setShortcut("Ctrl+Q")    

        dosya.addAction(dosya_ac)
        dosya.addAction(dosya_kaydet) 
        dosya.addAction(temizle) 
        dosya.addAction(cikis) 

        dosya.triggered.connect(self.response)
    
    def response(self,action):
        if action.text() == "Dosya Aç":
            self.pencere.dosya_ac()
        elif action.text() == "Dosya Kaydet":
            self.pencere.dosya_kaydet()
        elif action.text() == "Temizle":
            self.pencere.yaziyi_temizle()
        elif action.text() == "Çıkış":
            qApp.quit()

    
app = QApplication(sys.argv)
menu = Main()
sys.exit(app.exec_())