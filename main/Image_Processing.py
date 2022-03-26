# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hw1_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import cv2
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets


image_sun = cv2.imread("../Dataset_OpenCvDl_Hw1/Q1_Image/Sun.jpg")
image_strong_dog = cv2.imread("../Dataset_OpenCvDl_Hw1/Q1_Image/Dog_Strong.jpg")
image_weak_dog = cv2.imread("../Dataset_OpenCvDl_Hw1/Q1_Image/Dog_Weak.jpg")

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
        self.load_image = QtWidgets.QPushButton(self.centralwidget)
        self.load_image.setGeometry(QtCore.QRect(40, 70, 251, 91))
        self.load_image.setObjectName("load_image")
        self.color_separate = QtWidgets.QPushButton(self.centralwidget)
        self.color_separate.setGeometry(QtCore.QRect(40, 170, 251, 91))
        self.color_separate.setObjectName("color_separate")
        self.color_transform = QtWidgets.QPushButton(self.centralwidget)
        self.color_transform.setGeometry(QtCore.QRect(40, 270, 251, 91))
        self.color_transform.setObjectName("color_transform")
        self.blend = QtWidgets.QPushButton(self.centralwidget)
        self.blend.setGeometry(QtCore.QRect(40, 370, 251, 91))
        self.blend.setObjectName("blend")
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

        self.load_image.clicked.connect(lambda:self.load_image_file(image_sun))
        self.color_separate.clicked.connect(lambda:self.color_separation(image_sun))
        self.color_transform.clicked.connect(lambda:self.color_transformation(image_sun))
        self.blend.clicked.connect(lambda:self.blending(image_strong_dog, image_weak_dog))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "1. Image Processing"))
        self.load_image.setText(_translate("MainWindow", "1.1 Load Image"))
        self.color_separate.setText(_translate("MainWindow", "1.2 Color Separation"))
        self.color_transform.setText(_translate("MainWindow", "1.3 Color Transformation"))
        self.blend.setText(_translate("MainWindow", "1.4 Blending"))
    
    # hw1_1.1
    def load_image_file(self,img):
        image_shape = img.shape
        height = image_shape[0]
        width = image_shape[1]
        x1 = 5
        y1 = 435
        # 顏色
        color = (0, 0, 0)
        text_color = (255, 255, 255)
        # 文字內容 
        text1 = f'Height : {height}'
        text2 = f'Width : {width} '
        # 加入邊框
        img = cv2.copyMakeBorder(img, 0, 100, 0, 0, cv2.BORDER_CONSTANT, value = (255,255,255))
        # 計算文字的大小
        (w1, h1), _ = cv2.getTextSize(text1, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 1)
        (w2, h2), _ = cv2.getTextSize(text2, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 1)
        # 加入文字背景區塊 
        img = cv2.rectangle(img, (x1, y1 - 20), (x1 + w1, y1), color, -1)
        img = cv2.rectangle(img, (x1, y1 + 20), (x1 + w2, y1), color, -1)
        # 加入文字
        img = cv2.putText(img, text1, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, text_color, 1)
        img = cv2.putText(img, text2, (x1, y1 + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.6, text_color, 1)
        #  顯示圖片
        cv2.imshow('Output', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # hw1_1.2
    def color_separation(self,img):
        B, G, R = cv2.split(img)
        zero_matrix = np.zeros(img.shape[:2], dtype = "uint8")  # 創建與image大小相同的零矩陣，最多2的8次方(255)
        cv2.imshow("BLUE", cv2.merge([B, zero_matrix, zero_matrix]))  # 如果直接show會變灰階值eg.[B,B,B]
        cv2.imshow("GREEN", cv2.merge([zero_matrix, G, zero_matrix]))
        cv2.imshow("RED", cv2.merge([zero_matrix, zero_matrix, R]))
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # hw1_1.3
    def color_transformation(self,img):
        img_shape = img.shape
        height = img_shape[0]
        width = img_shape[1]
        cvt_func = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow('OpenCV function', cvt_func)
        B, G, R = cv2.split(img)
        avg_weight = np.zeros([height, width], np.uint8)
        for i in range(height):
            for j in range(width):
                avg_weight[i, j] = (int(B[i, j]) + int(G[i, j]) + int(R[i, j]))/3
        cv2.imshow('Average weighted', avg_weight)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # hw1_1.4
    def blending(self,img1, img2):
        def nothing(x):
            pass
        # 建立一個黑色背景的視窗
        img = np.zeros(img1.shape[:2], np.uint8)
        cv2.namedWindow('Blend')

        cv2.createTrackbar('blend','Blend',0,100,nothing)

        while(1):
            cv2.imshow('Blend',img)
            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                break

            r = cv2.getTrackbarPos('blend','Blend')
            r=float(r)/100.0

            img=cv2.addWeighted(img1,r,img2,1.0-r,0)
            
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
