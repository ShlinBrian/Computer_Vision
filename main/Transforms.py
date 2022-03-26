# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hw1_4.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import cv2
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets

img = cv2.imread("../Dataset_OpenCvDl_Hw1/Q4_Image/SQUARE-01.png")


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(355, 543)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 0, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Resize = QtWidgets.QPushButton(self.centralwidget)
        self.Resize.setGeometry(QtCore.QRect(40, 70, 251, 91))
        self.Resize.setObjectName("Resize")
        self.Translation = QtWidgets.QPushButton(self.centralwidget)
        self.Translation.setGeometry(QtCore.QRect(40, 170, 251, 91))
        self.Translation.setObjectName("Translation")
        self.Rotation_Scaling = QtWidgets.QPushButton(self.centralwidget)
        self.Rotation_Scaling.setGeometry(QtCore.QRect(40, 270, 251, 91))
        self.Rotation_Scaling.setObjectName("Rotation_Scaling")
        self.Shearing = QtWidgets.QPushButton(self.centralwidget)
        self.Shearing.setGeometry(QtCore.QRect(40, 370, 251, 91))
        self.Shearing.setObjectName("Shearing")
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

        self.Resize.clicked.connect(lambda: self.resize(img))
        self.Translation.clicked.connect(lambda: self.translation(img))
        self.Rotation_Scaling.clicked.connect(lambda: self.rotation(img))
        self.Shearing.clicked.connect(lambda: self.shearing(img))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "4.  Transformation"))
        self.Resize.setText(_translate("MainWindow", "4.1 Resize"))
        self.Translation.setText(_translate("MainWindow", "4.2 Translation"))
        self.Rotation_Scaling.setText(_translate("MainWindow", "4.3 Rotation_Scaling"))
        self.Shearing.setText(_translate("MainWindow", "4.4 Shearing"))

        # hw1_4.1
    def resize(self,img):
        res=cv2.resize(img,(256,256))
        cv2.imshow('res',res)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # hw1_4.2
    def translation(self,img):
        img = cv2.resize(img,(256,256))
        trans_mtx = np.float32([[1,0,0],[0,1,60]])
        trans = cv2.warpAffine(img,trans_mtx,(400, 300))
        cv2.imshow('translation', trans)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # hw1_4.3
    def rotation(self,img):
        img = cv2.resize(img,(256,256))
        trans_mtx = np.float32([[1,0,0],[0,1,60]])
        rotate_mtx = cv2.getRotationMatrix2D((188,128),10,0.5)
        trans = cv2.warpAffine(img,trans_mtx,(400, 300))
        rotate = cv2.warpAffine(trans,rotate_mtx,(400, 300)) 
        cv2.imshow('translation', rotate)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # hw1_4.4
    def shearing(self,img):
        img = cv2.resize(img,(256,256))
        trans_mtx = np.float32([[1,0,0],[0,1,60]])
        rotate_mtx = cv2.getRotationMatrix2D((188,128),10,0.5)
        trans = cv2.warpAffine(img,trans_mtx,(400, 300))
        rotate = cv2.warpAffine(trans,rotate_mtx,(400, 300))
        pts1 = np.float32([[50,50],[200,50],[50,200]])
        pts2 = np.float32([[10,100],[200,50],[100,250]])
        shear_mtx = cv2.getAffineTransform(pts1,pts2)
        shear = cv2.warpAffine(rotate,shear_mtx,(400,300))
        cv2.imshow('shearing', shear)
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
