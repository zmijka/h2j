# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'h2j.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import os, fnmatch
from PySide2 import QtCore, QtWidgets
from wand.image import Image


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(20, 30, 121, 18))
        self.label_1.setObjectName("label_1")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 130, 191, 18))
        self.label_2.setObjectName("label_2")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 230, 361, 18))
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setObjectName("label_3")
        
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(120, 70, 88, 34))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_1.clicked.connect(h2j.HEIC_file)
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 170, 88, 34))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(h2j.HEIC_folder)
        
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 270, 88, 34))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(h2j.dest_folder)
        
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(430, 350, 88, 34))
        self.pushButton_4.setObjectName("pushButton_4")
        # Action Convert / Connect to convert function
        self.pushButton_4.clicked.connect(h2j.set_to_convert)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "h2j - HEVC to JPEG"))
        self.label_1.setText(_translate("MainWindow", "Wybierz plik HEVC"))
        self.label_2.setText(_translate("MainWindow", "Wybierz folder z plikami HEVC"))
        self.label_3.setText(_translate("MainWindow", "Wybierz folder do którego zapisać przekonwertowane pliki"))
        self.pushButton_1.setText(_translate("MainWindow", "Wybierz"))
        self.pushButton_2.setText(_translate("MainWindow", "Wybierz"))
        self.pushButton_3.setText(_translate("MainWindow", "Wybierz"))
        self.pushButton_4.setText(_translate("MainWindow", "Konwertuj"))

    
class h2j_class():
    
    # wybor pliku do konwersji
    def HEIC_file(self):
        self.file_path = QtWidgets.QFileDialog.getOpenFileName(None, 'Wybierz plik HEIC...', './', 'HEIC File(*.heic)')
        # zapis pelnej sciezki do pliku w zmiennej file_path
        self.file_path = self.file_path[0]
               
      
    # wybor folderu z plikami HEIC
    def HEIC_folder(self):
        # zapis sciezki do folderu z plikami do konwersji i zapisanie jej w zmiennej folder_path
        self.folder_path = str(QtWidgets.QFileDialog.getExistingDirectory())
        
    
    # wybor folderu do ktorego zapiszemy pliki po konwersji
    def dest_folder(self):
        # zapis sciezki do folderu docelowego w zmiennej dest_path
        self.dest_path = str(QtWidgets.QFileDialog.getExistingDirectory())


    def set_to_convert(self):
        
        if self.dest_folder:
            if self.file_path:
                # wywolanie funkcji convert dla pliku
                self.convert(self.file_path)
                # czyscimy zmienna file_path
                self.file_path = None

            elif self.folder_path:
            
                for file in os.listdir(self.folder_path):
                    full_path = os.path.join(self.folder_path, file)
                    # wywolanie funkcji convert dla folderu z plikami
                    self.convert(full_path)

    # czyscimy zmienne
    folder_path = None
    dest_path = None


# funkcja file
    def convert(self, file):
        
        # sprawdzanie czy w przekazanej zmiennej file
        # znajduje sie plik Heic
        if fnmatch.fnmatch(file, '*.heic'):
            with Image(filename=file) as img:

                # obciecie rozszerzenia w nazwie pliku
                jpeg_file = os.path.splitext(file)[0]
                
                # zapisanie do zmiennej jpeg_file sciezki do zapisu pliku 
                # podanej w zmiennej dest_path oraz doklejenie nowego rozszerzenia .jpg
                jpeg_file = self.dest_path + '/' + os.path.basename(jpeg_file) + '.jpg'
                
                # zapisanie pliku jako jpg
                img.format = 'jpeg'
                img.save(filename=jpeg_file)


if __name__ == "__main__":
    import sys
    
    h2j = h2j_class()
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())