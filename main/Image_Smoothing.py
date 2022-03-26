# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hw1_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import cv2
from PyQt5 import QtCore, QtGui, QtWidgets

image_whitenoise = cv2.imread("../Dataset_OpenCvDl_Hw1/Q2_Image/Lenna_whiteNoise.jpg")
image_pepersalt = cv2.imread("../Dataset_OpenCvDl_Hw1/Q2_Image/Lenna_pepperSalt.jpg")

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(355, 437)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 0, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gaussianblur = QtWidgets.QPushButton(self.centralwidget)
        self.gaussianblur.setGeometry(QtCore.QRect(40, 70, 251, 91))
        self.gaussianblur.setObjectName("gaussianblur")
        self.bilateralfilter = QtWidgets.QPushButton(self.centralwidget)
        self.bilateralfilter.setGeometry(QtCore.QRect(40, 170, 251, 91))
        self.bilateralfilter.setObjectName("bilateralfilter")
        self.medianfilter = QtWidgets.QPushButton(self.centralwidget)
        self.medianfilter.setGeometry(QtCore.QRect(40, 270, 251, 91))
        self.medianfilter.setObjectName("medianfilter")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 355, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.gaussianblur.clicked.connect(lambda:self.Gaussian_blur(image_whitenoise))
        self.bilateralfilter.clicked.connect(lambda:self.Bilateral_filter(image_whitenoise))
        self.medianfilter.clicked.connect(lambda:self.Median_filter(image_pepersalt))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "2.  Image Smoothing"))
        self.gaussianblur.setText(_translate("MainWindow", "2.1 Gaussian Blur"))
        self.bilateralfilter.setText(_translate("MainWindow", "2.2 Bilateral Filter"))
        self.medianfilter.setText(_translate("MainWindow", "2.3 Median Filter"))
    
    # hw1_2.1
    def Gaussian_blur(self,img):
        blur = cv2.GaussianBlur(img, (5, 5), 0)
        cv2.imshow('Original', img)
        cv2.imshow('Gaussian blur', blur)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # hw1_2.2
    def Bilateral_filter(self,img):
        blur = cv2.bilateralFilter(img, 9, 90, 90)
        cv2.imshow('Original', img)
        cv2.imshow('Bilateral Filter', blur)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # hw1_2.3
    def Median_filter(self,img):
        blur3 = cv2.medianBlur(img, 3)
        blur5 = cv2.medianBlur(img, 5)
        cv2.imshow('Original', img)
        cv2.imshow('3x3 Median Filter', blur3) 
        cv2.imshow('5x5 Median Filter', blur5)
        cv2.waitKey(0)
        cv2.destroyAllWindows()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())