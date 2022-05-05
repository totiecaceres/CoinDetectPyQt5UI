# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Josephine\Documents\Qt Designer\Thresholding GUI\thresholding.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys, os
import cv2
import scipy.signal
import pylab
import numpy as np
from matplotlib import pyplot as plt

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage, QIntValidator

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Thresholding")
        MainWindow.resize(1200, 740)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1591, 740))
        self.tabWidget.setObjectName("tabWidget")
        self.pre_process = QtWidgets.QWidget()
        self.pre_process.setObjectName("pre_process")

        self.tabWidget.addTab(self.pre_process, "")
        self.eval_process = QtWidgets.QWidget()
        self.eval_process.setObjectName("eval_process")

        self.imageLbl = QtWidgets.QLabel(self.pre_process)
        self.imageLbl.setGeometry(QtCore.QRect(20, 5, 381, 311))
        self.imageLbl.setFrameShape(QtWidgets.QFrame.Box)
        self.imageLbl.setText("")
        self.imageLbl.setObjectName("imageLbl")
        self.threshLbl = QtWidgets.QLabel(self.pre_process)
        self.threshLbl.setGeometry(QtCore.QRect(410, 5, 381, 311))
        self.threshLbl.setFrameShape(QtWidgets.QFrame.Box)
        self.threshLbl.setText("")
        self.threshLbl.setObjectName("threshLbl")
        self.morph1Lbl = QtWidgets.QLabel(self.pre_process)
        self.morph1Lbl.setGeometry(QtCore.QRect(800, 5, 381, 311))
        self.morph1Lbl.setFrameShape(QtWidgets.QFrame.Box)
        self.morph1Lbl.setText("")
        self.morph1Lbl.setObjectName("morph1Lbl")
        self.morph2Lbl = QtWidgets.QLabel(self.pre_process)
        self.morph2Lbl.setGeometry(QtCore.QRect(20, 355, 381, 311))
        self.morph2Lbl.setFrameShape(QtWidgets.QFrame.Box)
        self.morph2Lbl.setText("")
        self.morph2Lbl.setObjectName("morph2Lbl")
        self.temachLbl = QtWidgets.QLabel(self.pre_process)
        self.temachLbl.setGeometry(QtCore.QRect(410, 355, 381, 311))
        self.temachLbl.setFrameShape(QtWidgets.QFrame.Box)
        self.temachLbl.setText("")
        self.temachLbl.setObjectName("temachLbl")

        self.selectimageBtn = QtWidgets.QPushButton(self.pre_process)
        self.selectimageBtn.setGeometry(QtCore.QRect(20, 320, 90, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(48, 115, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(48, 115, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.selectimageBtn.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.selectimageBtn.setFont(font)
        self.selectimageBtn.setMouseTracking(False)
        self.selectimageBtn.setCheckable(False)
        self.selectimageBtn.setObjectName("selectimageBtn")

        self.selecthreshBtn = QtWidgets.QPushButton(self.pre_process)
        self.selecthreshBtn.setEnabled(False)
        self.selecthreshBtn.setGeometry(QtCore.QRect(410, 320, 90, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(48, 115, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(48, 115, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.selecthreshBtn.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.selecthreshBtn.setFont(font)
        self.selecthreshBtn.setMouseTracking(False)
        self.selecthreshBtn.setCheckable(False)
        self.selecthreshBtn.setObjectName("selecthreshBtn")

        self.selectmorph1Btn = QtWidgets.QPushButton(self.pre_process)
        self.selectmorph1Btn.setEnabled(False)
        self.selectmorph1Btn.setGeometry(QtCore.QRect(800, 320, 90, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(48, 115, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(48, 115, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.selectmorph1Btn.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.selectmorph1Btn.setFont(font)
        self.selectmorph1Btn.setMouseTracking(False)
        self.selectmorph1Btn.setCheckable(False)
        self.selectmorph1Btn.setObjectName("selectmorph1Btn")

        self.selectmorph2Btn = QtWidgets.QPushButton(self.pre_process)
        self.selectmorph2Btn.setEnabled(False)
        self.selectmorph2Btn.setGeometry(QtCore.QRect(20, 670, 90, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(48, 115, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(48, 115, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.selectmorph2Btn.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.selectmorph2Btn.setFont(font)
        self.selectmorph2Btn.setMouseTracking(False)
        self.selectmorph2Btn.setCheckable(False)
        self.selectmorph2Btn.setObjectName("selectmorph2Btn")

        self.morph1combox = QtWidgets.QComboBox(self.pre_process)
        self.morph1combox.setEnabled(False)
        self.morph1combox.setGeometry(QtCore.QRect(895-270, 320, 80, 16))
        self.morph1combox.setMaximumSize(QtCore.QSize(150, 600))
        self.morph1combox.setObjectName("morph1combox")
        self.morph1combox.addItem("")
        self.morph1combox.addItem("")
        self.morph1combox.addItem("")
        self.morph1combox.addItem("")
        self.morph1combox.addItem("")

        self.itrmorp1Lbl = QtWidgets.QLabel(self.pre_process)
        self.itrmorp1Lbl.setGeometry(QtCore.QRect(1000-270, 320, 30, 16))
        self.itrmorp1Lbl.setText("itr= ")
        self.itrmorp1Lbl.setObjectName("itrmorp1Lbl")

        self.itrmorp1Box = QtWidgets.QLineEdit(self.pre_process)
        self.itrmorp1Box.setEnabled(False)
        self.itrmorp1Box.setGeometry(QtCore.QRect(1020-270, 320, 30, 16))
        self.itrmorp1Box.setObjectName("itrmorp1Box")
        self.itrmorp1Box.setValidator(QIntValidator())

        self.morph2combox = QtWidgets.QComboBox(self.pre_process)
        self.morph2combox.setEnabled(False)
        self.morph2combox.setGeometry(QtCore.QRect(895+120, 320, 80, 16))
        self.morph2combox.setMaximumSize(QtCore.QSize(150, 600))
        self.morph2combox.setObjectName("morph1combox")
        self.morph2combox.addItem("")
        self.morph2combox.addItem("")
        self.morph2combox.addItem("")
        self.morph2combox.addItem("")
        self.morph2combox.addItem("")

        self.itrmorp2Lbl = QtWidgets.QLabel(self.pre_process)
        self.itrmorp2Lbl.setGeometry(QtCore.QRect(1000+120, 320, 30, 16))
        self.itrmorp2Lbl.setText("itr= ")
        self.itrmorp2Lbl.setObjectName("itrmorp1Lbl")

        self.itrmorp2Box = QtWidgets.QLineEdit(self.pre_process)
        self.itrmorp2Box.setEnabled(False)
        self.itrmorp2Box.setGeometry(QtCore.QRect(1020+120, 320, 30, 16))
        self.itrmorp2Box.setObjectName("itrmorp1Box")
        self.itrmorp2Box.setValidator(QIntValidator())

        self.selecttematchBtn = QtWidgets.QPushButton(self.pre_process)
        self.selecttematchBtn.setEnabled(False)
        self.selecttematchBtn.setGeometry(QtCore.QRect(410, 670, 100, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(48, 115, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(48, 115, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.selecttematchBtn.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.selecttematchBtn.setFont(font)
        self.selecttematchBtn.setMouseTracking(False)
        self.selecttematchBtn.setCheckable(False)
        self.selecttematchBtn.setObjectName("selecttematchBtn")

        self.borderLbl = QtWidgets.QLabel(self.pre_process)
        self.borderLbl.setGeometry(QtCore.QRect(20+170, 670, 40, 16))
        self.borderLbl.setText("border= ")
        self.borderLbl.setObjectName("borderLbl")

        self.borderBox = QtWidgets.QLineEdit(self.pre_process)
        self.borderBox.setEnabled(False)
        self.borderBox.setGeometry(QtCore.QRect(20+220, 670, 30, 16))
        self.borderBox.setObjectName("borderBox")
        self.borderBox.setValidator(QIntValidator())

        self.gapLbl = QtWidgets.QLabel(self.pre_process)
        self.gapLbl.setGeometry(QtCore.QRect(20+300, 670, 30, 16))
        self.gapLbl.setText("gap= ")
        self.gapLbl.setObjectName("gapLbl")

        self.gapBox = QtWidgets.QLineEdit(self.pre_process)
        self.gapBox.setEnabled(False)
        self.gapBox.setGeometry(QtCore.QRect(20+340, 670, 30, 16))
        self.gapBox.setObjectName("gapBox")
        self.gapBox.setValidator(QIntValidator())

        self.segmentLbl = QtWidgets.QLabel(self.pre_process)
        self.segmentLbl.setGeometry(QtCore.QRect(800, 355, 381, 311))
        self.segmentLbl.setFrameShape(QtWidgets.QFrame.Box)
        self.segmentLbl.setText("")
        self.segmentLbl.setObjectName("segmentLbl")

        self.segmentBtn = QtWidgets.QPushButton(self.pre_process)
        self.segmentBtn.setEnabled(False)
        self.segmentBtn.setGeometry(QtCore.QRect(800, 670, 100, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(48, 115, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(48, 115, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.segmentBtn.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.segmentBtn.setFont(font)
        self.segmentBtn.setMouseTracking(False)
        self.segmentBtn.setCheckable(False)
        self.segmentBtn.setObjectName("segmentBtn")

        self.resetBtn = QtWidgets.QPushButton(self.pre_process)
        self.resetBtn.setEnabled(False)
        self.resetBtn.setGeometry(QtCore.QRect(800+275, 670, 100, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(48, 115, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(48, 115, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.resetBtn.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.resetBtn.setFont(font)
        self.resetBtn.setMouseTracking(False)
        self.resetBtn.setCheckable(False)
        self.resetBtn.setObjectName("resetBtn")

        self.origLbl = QtWidgets.QLabel(self.eval_process)
        self.origLbl.setGeometry(QtCore.QRect(20, 5, 381, 311))
        self.origLbl.setFrameShape(QtWidgets.QFrame.Box)
        self.origLbl.setText("")
        self.origLbl.setObjectName("origLbl")
        self.twofivecentLbl = QtWidgets.QLabel(self.eval_process)
        self.twofivecentLbl.setGeometry(QtCore.QRect(410, 5, 381, 311))
        self.twofivecentLbl.setFrameShape(QtWidgets.QFrame.Box)
        self.twofivecentLbl.setText("")
        self.twofivecentLbl.setObjectName("twofivecentLbl")
        self.onepesoLbl = QtWidgets.QLabel(self.eval_process)
        self.onepesoLbl.setGeometry(QtCore.QRect(800, 5, 381, 311))
        self.onepesoLbl.setFrameShape(QtWidgets.QFrame.Box)
        self.onepesoLbl.setText("")
        self.onepesoLbl.setObjectName("onepesoLbl")
        self.fivepesoLbl = QtWidgets.QLabel(self.eval_process)
        self.fivepesoLbl.setGeometry(QtCore.QRect(20, 355, 381, 311))
        self.fivepesoLbl.setFrameShape(QtWidgets.QFrame.Box)
        self.fivepesoLbl.setText("")
        self.fivepesoLbl.setObjectName("fivepesoLbl")
        self.tenpesoLbl = QtWidgets.QLabel(self.eval_process)
        self.tenpesoLbl.setGeometry(QtCore.QRect(410, 355, 381, 311))
        self.tenpesoLbl.setFrameShape(QtWidgets.QFrame.Box)
        self.tenpesoLbl.setText("")
        self.tenpesoLbl.setObjectName("tenpesoLbl")

        self.minrLbl = QtWidgets.QLabel(self.eval_process)
        self.minrLbl.setGeometry(QtCore.QRect(20 + 170, 320, 40, 16))
        self.minrLbl.setText("min_r= ")
        self.minrLbl.setObjectName("minrLbl")

        self.minrBox = QtWidgets.QLineEdit(self.eval_process)
        self.minrBox.setEnabled(False)
        self.minrBox.setGeometry(QtCore.QRect(20 + 220, 320, 30, 16))
        self.minrBox.setObjectName("minrBox")
        self.minrBox.setValidator(QIntValidator())

        self.maxrLbl = QtWidgets.QLabel(self.eval_process)
        self.maxrLbl.setGeometry(QtCore.QRect(20 + 300, 320, 30, 16))
        self.maxrLbl.setText("max_r= ")
        self.maxrLbl.setObjectName("maxrLbl")

        self.maxrBox = QtWidgets.QLineEdit(self.eval_process)
        self.maxrBox.setEnabled(False)
        self.maxrBox.setGeometry(QtCore.QRect(20 + 340, 320, 30, 16))
        self.maxrBox.setObjectName("maxrBox")
        self.maxrBox.setValidator(QIntValidator())

        self.twofivecentBtn = QtWidgets.QPushButton(self.eval_process)
        self.twofivecentBtn.setEnabled(False)
        self.twofivecentBtn.setGeometry(QtCore.QRect(410, 320, 90, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(48, 115, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(48, 115, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.twofivecentBtn.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.twofivecentBtn.setFont(font)
        self.twofivecentBtn.setMouseTracking(False)
        self.twofivecentBtn.setCheckable(False)
        self.twofivecentBtn.setObjectName("twofivecentBtn")

        self.onepesoBtn = QtWidgets.QPushButton(self.eval_process)
        self.onepesoBtn.setEnabled(False)
        self.onepesoBtn.setGeometry(QtCore.QRect(800, 320, 90, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(48, 115, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(48, 115, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.onepesoBtn.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.onepesoBtn.setFont(font)
        self.onepesoBtn.setMouseTracking(False)
        self.onepesoBtn.setCheckable(False)
        self.onepesoBtn.setObjectName("onepesoBtn")

        self.fivepesoBtn = QtWidgets.QPushButton(self.eval_process)
        self.fivepesoBtn.setEnabled(False)
        self.fivepesoBtn.setGeometry(QtCore.QRect(20, 670, 90, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(48, 115, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(48, 115, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.fivepesoBtn.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.fivepesoBtn.setFont(font)
        self.fivepesoBtn.setMouseTracking(False)
        self.fivepesoBtn.setCheckable(False)
        self.fivepesoBtn.setObjectName("fivepesoBtn")

        self.tenpesoBtn = QtWidgets.QPushButton(self.eval_process)
        self.tenpesoBtn.setEnabled(False)
        self.tenpesoBtn.setGeometry(QtCore.QRect(410, 670, 100, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(48, 115, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(48, 115, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.tenpesoBtn.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.tenpesoBtn.setFont(font)
        self.tenpesoBtn.setMouseTracking(False)
        self.tenpesoBtn.setCheckable(False)
        self.tenpesoBtn.setObjectName("tenpesoBtn")

        self.countcoin25 = QtWidgets.QLabel(self.eval_process)
        self.countcoin25.setGeometry(QtCore.QRect(895 - 270, 320, 30, 25))
        self.countcoin25.setMaximumSize(QtCore.QSize(150, 600))
        self.countcoin25.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.countcoin25.setFont(font)
        self.countcoin25.setFrameShape(QtWidgets.QFrame.Box)
        self.countcoin25.setText("")
        self.countcoin25.setAlignment(QtCore.Qt.AlignCenter)
        self.countcoin25.setObjectName("countcoin25")

        self.countcoin01 = QtWidgets.QLabel(self.eval_process)
        self.countcoin01.setGeometry(QtCore.QRect(895 + 120, 320, 30, 25))
        self.countcoin01.setMaximumSize(QtCore.QSize(150, 600))
        self.countcoin01.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.countcoin01.setFont(font)
        self.countcoin01.setFrameShape(QtWidgets.QFrame.Box)
        self.countcoin01.setText("")
        self.countcoin01.setAlignment(QtCore.Qt.AlignCenter)
        self.countcoin01.setObjectName("countcoin01")

        self.countcoin05 = QtWidgets.QLabel(self.eval_process)
        self.countcoin05.setGeometry(QtCore.QRect(20+170, 670, 30, 25))
        self.countcoin05.setMaximumSize(QtCore.QSize(150, 600))
        self.countcoin05.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.countcoin05.setFont(font)
        self.countcoin05.setFrameShape(QtWidgets.QFrame.Box)
        self.countcoin05.setText("")
        self.countcoin05.setAlignment(QtCore.Qt.AlignCenter)
        self.countcoin05.setObjectName("countcoin05")

        self.countcoin10 = QtWidgets.QLabel(self.eval_process)
        self.countcoin10.setGeometry(QtCore.QRect(895 - 270, 670, 30, 25))
        self.countcoin10.setMaximumSize(QtCore.QSize(150, 600))
        self.countcoin10.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.countcoin10.setFont(font)
        self.countcoin10.setFrameShape(QtWidgets.QFrame.Box)
        self.countcoin10.setText("")
        self.countcoin10.setAlignment(QtCore.Qt.AlignCenter)
        self.countcoin10.setObjectName("countcoin10")

        self.reset2Btn = QtWidgets.QPushButton(self.eval_process)
        self.reset2Btn.setEnabled(False)
        self.reset2Btn.setGeometry(QtCore.QRect(800 + 275, 670, 100, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(48, 115, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(48, 115, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.reset2Btn.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.reset2Btn.setFont(font)
        self.reset2Btn.setMouseTracking(False)
        self.reset2Btn.setCheckable(False)
        self.reset2Btn.setObjectName("reset2Btn")

        self.tabWidget.addTab(self.eval_process, "Eval_process")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 1 - Import Original:
        self.selectimageBtn.clicked.connect(self.setImage)
        # 2 - Thresholding:
        self.selecthreshBtn.clicked.connect(self.thresholding)
        # 3 - Morphology 1:
        self.selectmorph1Btn.clicked.connect(self.morph1)
        # 3 - Morphology 2:
        self.selectmorph2Btn.clicked.connect(self.morph2)
        # 4 - Sure Fore Ground:
        self.selecttematchBtn.clicked.connect(self.template_match)
        # 5 - Segment:
        self.segmentBtn.clicked.connect(self.segment)
        # Reset:
        self.resetBtn.clicked.connect(self.reset)
        # 6 - Segment 25 cents:
        self.twofivecentBtn.clicked.connect(self.seg_25)
        # 7 - Segment 1 pesos:
        self.onepesoBtn.clicked.connect(self.seg_01)
        # 8 - Segment 5 pesos:
        self.fivepesoBtn.clicked.connect(self.seg_05)
        # 9 - Segment 10 pesos:
        self.tenpesoBtn.clicked.connect(self.seg_10)
        # Reset:
        self.reset2Btn.clicked.connect(self.reset)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.selectimageBtn.setText(_translate("MainWindow", "Import Image"))
        self.selecthreshBtn.setText(_translate("MainWindow", "Otsu's Thresh"))
        self.morph1combox.setItemText(0, _translate("MainWindow", "None"))
        self.morph1combox.setItemText(1, _translate("MainWindow", "Erosion"))
        self.morph1combox.setItemText(2, _translate("MainWindow", "Dilation"))
        self.morph1combox.setItemText(3, _translate("MainWindow", "Opening"))
        self.morph1combox.setItemText(4, _translate("MainWindow", "Closing"))
        self.itrmorp1Lbl.setText(_translate("MainWindow", "itr= "))
        self.itrmorp1Box.setText(_translate("MainWindow", "1"))
        self.morph2combox.setItemText(0, _translate("MainWindow", "None"))
        self.morph2combox.setItemText(1, _translate("MainWindow", "Erosion"))
        self.morph2combox.setItemText(2, _translate("MainWindow", "Dilation"))
        self.morph2combox.setItemText(3, _translate("MainWindow", "Opening"))
        self.morph2combox.setItemText(4, _translate("MainWindow", "Closing"))
        self.itrmorp2Lbl.setText(_translate("MainWindow", "itr= "))
        self.itrmorp2Box.setText(_translate("MainWindow", "1"))
        self.selectmorph1Btn.setText(_translate("MainWindow", "Morph Trans 1"))
        self.selectmorph2Btn.setText(_translate("MainWindow", "Morph Trans 2"))
        self.selecttematchBtn.setText(_translate("MainWindow", "Sure Foreground"))
        self.borderLbl.setText(_translate("MainWindow", "border= "))
        self.borderBox.setText(_translate("MainWindow", "18"))
        self.gapLbl.setText(_translate("MainWindow", "gap= "))
        self.gapBox.setText(_translate("MainWindow", "5"))
        self.segmentBtn.setText(_translate("MainWindow", "Segment"))
        self.resetBtn.setText(_translate("MainWindow", "Reset"))
        self.twofivecentBtn.setText(_translate("MainWindow", "25 Cents"))
        self.onepesoBtn.setText(_translate("MainWindow", "1 Pesos"))
        self.fivepesoBtn.setText(_translate("MainWindow", "5 Pesos"))
        self.tenpesoBtn.setText(_translate("MainWindow", "10 Pesos"))
        self.minrLbl.setText(_translate("MainWindow", "min_r= "))
        self.minrBox.setText(_translate("MainWindow", "15"))
        self.maxrLbl.setText(_translate("MainWindow", "max_r= "))
        self.maxrBox.setText(_translate("MainWindow", "18"))
        self.reset2Btn.setText(_translate("MainWindow", "Reset"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pre_process), _translate("MainWindow", "Pre-processing"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.eval_process), _translate("MainWindow", "Coin-Evaluation"))
        # self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Coin Counter"))

    def reset(self):
        white = np.zeros((381, 311), np.uint8)
        white = cv2.bitwise_not(white)
        h, w = white.shape
        white_pix = QImage(white.data, w, h, QImage.Format_Grayscale8)
        white_fpix = QPixmap.fromImage(white_pix)
        pixmap = white_fpix.scaled(self.imageLbl.width(), self.imageLbl.height(),
                                QtCore.Qt.KeepAspectRatio)  # Scale pixmap
        self.imageLbl.setPixmap(pixmap)  # Set the pixmap onto the label
        self.imageLbl.setAlignment(QtCore.Qt.AlignCenter)  # Align the label to center
        self.threshLbl.setPixmap(pixmap)  # Set the pixmap onto the label
        self.threshLbl.setAlignment(QtCore.Qt.AlignCenter)  # Align the label to center
        self.morph1Lbl.setPixmap(pixmap)  # Set the pixmap onto the label
        self.morph1Lbl.setAlignment(QtCore.Qt.AlignCenter)  # Align the label to center
        self.morph2Lbl.setPixmap(pixmap)  # Set the pixmap onto the label
        self.morph2Lbl.setAlignment(QtCore.Qt.AlignCenter)  # Align the label to center
        self.temachLbl.setPixmap(pixmap)  # Set the pixmap onto the label
        self.temachLbl.setAlignment(QtCore.Qt.AlignCenter)  # Align the label to center
        self.segmentLbl.setPixmap(pixmap)  # Set the pixmap onto the label
        self.segmentLbl.setAlignment(QtCore.Qt.AlignCenter)  # Align the label to center
        self.twofivecentLbl.setPixmap(pixmap)  # Set the pixmap onto the label
        self.twofivecentLbl.setAlignment(QtCore.Qt.AlignCenter)  # Align the label to center
        self.onepesoLbl.setPixmap(pixmap)  # Set the pixmap onto the label
        self.onepesoLbl.setAlignment(QtCore.Qt.AlignCenter)  # Align the label to center
        self.fivepesoLbl.setPixmap(pixmap)  # Set the pixmap onto the label
        self.fivepesoLbl.setAlignment(QtCore.Qt.AlignCenter)  # Align the label to center
        self.tenpesoLbl.setPixmap(pixmap)  # Set the pixmap onto the label
        self.tenpesoLbl.setAlignment(QtCore.Qt.AlignCenter)  # Align the label to center
        self.origLbl.setPixmap(pixmap)  # Set the pixmap onto the label
        self.origLbl.setAlignment(QtCore.Qt.AlignCenter)  # Align the label to center
        self.selecthreshBtn.setEnabled(False)
        self.selectmorph1Btn.setEnabled(False)
        self.morph1combox.setEnabled(False)
        self.itrmorp1Box.setEnabled(False)
        self.selectmorph2Btn.setEnabled(False)
        self.itrmorp2Box.setEnabled(False)
        self.morph2combox.setEnabled(False)
        self.selecttematchBtn.setEnabled(False)
        self.borderBox.setEnabled(False)
        self.gapBox.setEnabled(False)
        self.segmentBtn.setEnabled(False)
        self.resetBtn.setEnabled(False)
        self.twofivecentBtn.setEnabled(False)
        self.onepesoBtn.setEnabled(False)
        self.fivepesoBtn.setEnabled(False)
        self.tenpesoBtn.setEnabled(False)
        self.minrLbl.setEnabled(False)
        self.minrBox.setEnabled(False)
        self.maxrLbl.setEnabled(False)
        self.maxrBox.setEnabled(False)
        self.countcoin25.setText("")
        self.countcoin01.setText("")
        self.countcoin05.setText("")
        self.countcoin10.setText("")


    def setImage(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "", "Image Files (*.png *.jpg *jpeg *.bmp);;All Files (*)") # Ask for file
        if fileName: # If the user gives a file
            pixmap = QtGui.QPixmap(fileName) # Setup pixmap with the provided image
            pixmap = pixmap.scaled(self.imageLbl.width(), self.imageLbl.height(), QtCore.Qt.KeepAspectRatio) # Scale pixmap
            self.imageLbl.setPixmap(pixmap)  # Set the pixmap onto the label
            self.imageLbl.setAlignment(QtCore.Qt.AlignCenter)  # Align the label to center
            self.origLbl.setPixmap(pixmap)  # Set the pixmap onto the label
            self.origLbl.setAlignment(QtCore.Qt.AlignCenter)  # Align the label to center
        self.input_img = fileName
        im = cv2.imread(fileName)
        im_rgb = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
        self.im_rgb = im_rgb
        self.selecthreshBtn.setEnabled(True)

    def thresholding(self):
        input = self.input_img
        im = cv2.imread(input)
        hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
        th, bw = cv2.threshold(hsv[:, :, 2], 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        self.thresh_img = bw
        h, w = bw.shape
        bw_pix = QImage(bw.data, w, h, QImage.Format_Grayscale8)
        bw_fpix = QPixmap.fromImage(bw_pix)
        pixmap = bw_fpix.scaled(self.threshLbl.width(), self.threshLbl.height(), QtCore.Qt.KeepAspectRatio)  # Scale pixmap
        self.threshLbl.setPixmap(pixmap)  # Set the pixmap onto the label
        self.threshLbl.setAlignment(QtCore.Qt.AlignCenter)  # Align the label to center
        self.selectmorph1Btn.setEnabled(True)
        self.morph1combox.setEnabled(True)
        self.itrmorp1Box.setEnabled(True)

    def morph1(self):
        bw = self.thresh_img
        itr1 = int(self.itrmorp1Box.text())
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
        if str(self.morph1combox.currentText()) == "Erosion":
            img = cv2.erode(bw,kernel,iterations=itr1)
        elif str(self.morph1combox.currentText()) == "Dilation":
            img = cv2.dilate(bw,kernel,iterations=itr1)
        elif str(self.morph1combox.currentText()) == "Opening":
            img = cv2.morphologyEx(bw,cv2.MORPH_OPEN,kernel,iterations=itr1)
        elif str(self.morph1combox.currentText()) == "Closing":
            img = cv2.morphologyEx(bw,cv2.MORPH_CLOSE,kernel,iterations=itr1)
        else:
            img = bw
        img = np.uint8(img)
        self.morphtrns1_img = img
        h, w = img.shape
        bw_pix = QImage(img.data, w, h, QImage.Format_Grayscale8)
        bw_fpix = QPixmap.fromImage(bw_pix)
        pixmap = bw_fpix.scaled(self.morph1Lbl.width(), self.morph1Lbl.height(),
                                QtCore.Qt.KeepAspectRatio)  # Scale pixmap
        self.morph1Lbl.setPixmap(pixmap)  # Set the pixmap onto the label
        self.morph1Lbl.setAlignment(QtCore.Qt.AlignCenter)  # Align the label to center
        self.selectmorph2Btn.setEnabled(True)
        self.itrmorp2Box.setEnabled(True)
        self.morph2combox.setEnabled(True)

    def morph2(self):
        bw = self.morphtrns1_img
        itr1 = int(self.itrmorp2Box.text())
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
        if str(self.morph2combox.currentText()) == "Erosion":
            img = cv2.erode(bw,kernel,iterations=itr1)
        elif str(self.morph2combox.currentText()) == "Dilation":
            img = cv2.dilate(bw,kernel,iterations=itr1)
        elif str(self.morph2combox.currentText()) == "Opening":
            img = cv2.morphologyEx(bw,cv2.MORPH_OPEN,kernel,iterations=itr1)
        elif str(self.morph2combox.currentText()) == "Closing":
            img = cv2.morphologyEx(bw,cv2.MORPH_CLOSE,kernel,iterations=itr1)
        else:
            img = bw
        img = np.uint8(img)
        self.closing_img2 = img
        h, w = img.shape
        bw_pix = QImage(img.data, w, h, QImage.Format_Grayscale8)
        bw_fpix = QPixmap.fromImage(bw_pix)
        pixmap = bw_fpix.scaled(self.morph2Lbl.width(), self.morph2Lbl.height(),
                                QtCore.Qt.KeepAspectRatio)  # Scale pixmap
        self.morph2Lbl.setPixmap(pixmap)  # Set the pixmap onto the label
        self.morph2Lbl.setAlignment(QtCore.Qt.AlignCenter)  # Align the label to center

        self.selecttematchBtn.setEnabled(True)
        self.borderBox.setEnabled(True)
        self.gapBox.setEnabled(True)


    def template_match(self):
        borderSize = int(self.borderBox.text())
        gap = int(self.gapBox.text())

        morph = self.closing_img2
        dist = cv2.distanceTransform(morph, cv2.DIST_L2, cv2.DIST_MASK_PRECISE)
        self.dist = dist
        distborder = cv2.copyMakeBorder(dist, borderSize, borderSize, borderSize, borderSize,
                                        cv2.BORDER_CONSTANT | cv2.BORDER_ISOLATED, 0)
        kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * (borderSize - gap) + 1, 2 * (borderSize - gap) + 1))
        kernel2 = cv2.copyMakeBorder(kernel2, gap, gap, gap, gap,
                                     cv2.BORDER_CONSTANT | cv2.BORDER_ISOLATED, 0)
        distTempl = cv2.distanceTransform(kernel2, cv2.DIST_L2, cv2.DIST_MASK_PRECISE)

        nxcor = cv2.matchTemplate(distborder, distTempl, cv2.TM_CCOEFF_NORMED)
        mn, mx, _, _ = cv2.minMaxLoc(nxcor)
        th, sure_fg = cv2.threshold(nxcor, mx * 0.5, 255, cv2.THRESH_BINARY)
        sure_fg = np.uint8(sure_fg)
        self.sure_fg = sure_fg
        h, w = sure_fg.shape
        peaks_pix = QImage(sure_fg.data, w, h, QImage.Format_Grayscale8)
        peaks_fpix = QPixmap.fromImage(peaks_pix)
        pixmap = peaks_fpix.scaled(self.temachLbl.width(), self.temachLbl.height(), QtCore.Qt.KeepAspectRatio)  # Scale pixmap
        self.temachLbl.setPixmap(pixmap)  # Set the pixmap onto the label
        self.temachLbl.setAlignment(QtCore.Qt.AlignCenter)  # Align the label to center
        self.segmentBtn.setEnabled(True)

    def segment(self):
        sure_fg = self.sure_fg
        dist = self.dist
        _, contours, hierarchy = cv2.findContours(sure_fg, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
        canvass = np.zeros(sure_fg.shape, np.uint8)
        for i in range(len(contours)):
            x, y, w, h = cv2.boundingRect(contours[i])
            _, radius, _, radiusloc = cv2.minMaxLoc(dist[y:y + h, x:x + w], sure_fg[y:y + h, x:x + w])
            cv2.circle(canvass, (int(radiusloc[0] + x), int(radiusloc[1] + y)), int(radius), (255, 255, 255), 2)
        h, w = canvass.shape
        canvass_pix = QImage(canvass.data, w, h, QImage.Format_Grayscale8)
        canvass_fpix = QPixmap.fromImage(canvass_pix)
        pixmap = canvass_fpix.scaled(self.segmentLbl.width(), self.segmentLbl.height(),
                                   QtCore.Qt.KeepAspectRatio)  # Scale pixmap
        self.segmentLbl.setPixmap(pixmap)  # Set the pixmap onto the label
        self.segmentLbl.setAlignment(QtCore.Qt.AlignCenter)  # Align the label to center
        self.resetBtn.setEnabled(True)
        self.reset2Btn.setEnabled(True)
        self.maxrBox.setEnabled(True)
        self.minrBox.setEnabled(True)
        self.twofivecentBtn.setEnabled(True)
        self.onepesoBtn.setEnabled(True)
        self.fivepesoBtn.setEnabled(True)
        self.tenpesoBtn.setEnabled(True)

    def seg_25(self):
        maxr = float(self.maxrBox.text())
        minr = float(self.minrBox.text())
        sure_fg = self.sure_fg
        dist = self.dist
        im = self.im_rgb
        _, contours, hierarchy = cv2.findContours(sure_fg, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
        canvass = np.zeros(sure_fg.shape, np.uint8)
        j = 0
        for i in range(len(contours)):
            x, y, w, h = cv2.boundingRect(contours[i])
            _, radius, _, radiusloc = cv2.minMaxLoc(dist[y:y + h, x:x + w], sure_fg[y:y + h, x:x + w])
            if (radius < maxr and radius > minr):
                cv2.circle(canvass, (int(radiusloc[0] + x), int(radiusloc[1] + y)), int(radius), (255, 255, 255), -1)
                j = j + 1

        result = cv2.bitwise_and(im, im, mask=canvass)
        h, w, c = result.shape
        canvass_pix = QImage(result.data, w, h, 3 * w, QImage.Format_RGB888)
        canvass_fpix = QPixmap.fromImage(canvass_pix)
        pixmap = canvass_fpix.scaled(self.twofivecentLbl.width(), self.twofivecentLbl.height(),
                                     QtCore.Qt.KeepAspectRatio)  # Scale pixmap
        self.twofivecentLbl.setPixmap(pixmap)  # Set the pixmap onto the label
        self.twofivecentLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.countcoin25.setText(str(j))

    def seg_01(self):
        # maxr = int(self.maxrBox.text())
        # minr = int(self.minrBox.text())
        maxr = 21.9
        minr = 18
        sure_fg = self.sure_fg
        dist = self.dist
        im = self.im_rgb
        _, contours, hierarchy = cv2.findContours(sure_fg, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
        canvass = np.zeros(dist.shape, np.uint8)
        canvass2 = np.zeros(dist.shape, np.uint8)
        j = -1
        for i in range(len(contours)):
            x, y, w, h = cv2.boundingRect(contours[i])
            _, radius, _, radiusloc = cv2.minMaxLoc(dist[y:y + h, x:x + w], sure_fg[y:y + h, x:x + w])

            if (radius < maxr and radius > minr):
                cv2.circle(canvass, (int(radiusloc[0] + x), int(radiusloc[1] + y)), int(radius), (255, 255, 255),-1)
                if (h == 18 and w == 16):
                    cv2.circle(canvass2, (int(radiusloc[0] + x), int(radiusloc[1] + y)), int(radius),
                               (255, 255, 255), -1)
                j = j + 1
        canvass = cv2.subtract(canvass, canvass2)

        result = cv2.bitwise_and(im, im, mask=canvass)
        h, w, c = result.shape
        canvass_pix = QImage(result.data, w, h, 3 * w, QImage.Format_RGB888)
        canvass_fpix = QPixmap.fromImage(canvass_pix)
        pixmap = canvass_fpix.scaled(self.onepesoLbl.width(), self.onepesoLbl.height(),
                                     QtCore.Qt.KeepAspectRatio)  # Scale pixmap
        self.onepesoLbl.setPixmap(pixmap)  # Set the pixmap onto the label
        self.onepesoLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.countcoin01.setText(str(j))

    def seg_05(self):
        # maxr = int(self.maxrBox.text())
        # maxr = maxr/10
        # minr = int(self.minrBox.text())
        # minr = minr/10
        maxr = 26
        minr = 21.8
        sure_fg = self.sure_fg
        dist = self.dist
        im = self.im_rgb
        _, contours, hierarchy = cv2.findContours(sure_fg, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
        canvass = np.zeros(sure_fg.shape, np.uint8)
        j=0
        for i in range(len(contours)):
            x, y, w, h = cv2.boundingRect(contours[i])
            _, radius, _, radiusloc = cv2.minMaxLoc(dist[y:y + h, x:x + w], sure_fg[y:y + h, x:x + w])
            canvass2 = np.zeros(sure_fg.shape, np.uint8)
            if (radius < maxr and radius > minr and h != 17):
                cv2.circle(canvass, (int(radiusloc[0] + x), int(radiusloc[1] + y)), int(radius), (255, 255, 255), -1)
                j=j+1
            if (radius < 22 and radius > 18 and h == 18 and w == 16):
                cv2.circle(canvass2, (int(radiusloc[0] + x), int(radiusloc[1] + y)), int(radius), (255, 255, 255), -1)
                j=j+1
            canvass = cv2.add(canvass, canvass2)

        result = cv2.bitwise_and(im, im, mask=canvass)
        h, w, c = result.shape
        canvass_pix = QImage(result.data, w, h, 3 * w, QImage.Format_RGB888)
        canvass_fpix = QPixmap.fromImage(canvass_pix)
        pixmap = canvass_fpix.scaled(self.fivepesoLbl.width(), self.fivepesoLbl.height(),
                                     QtCore.Qt.KeepAspectRatio)  # Scale pixmap
        self.fivepesoLbl.setPixmap(pixmap)  # Set the pixmap onto the label
        self.fivepesoLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.countcoin05.setText(str(j))

    def seg_10(self):
        # maxr = int(self.maxrBox.text())
        # maxr = maxr/10
        # minr = int(self.minrBox.text())
        # minr = minr/10
        maxr = 26
        minr = 21.8
        sure_fg = self.sure_fg
        dist = self.dist
        im = self.im_rgb
        _, contours, hierarchy = cv2.findContours(sure_fg, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
        canvass = np.zeros(im.shape[:2], np.uint8)
        j=0
        thresh = 0.1
        for i in range(len(contours)):
            x, y, w, h = cv2.boundingRect(contours[i])
            _, radius, _, radiusloc = cv2.minMaxLoc(dist[y:y + h, x:x + w], sure_fg[y:y + h, x:x + w])
            if (radius < maxr and radius > minr and h<=17+thresh and h>=17-thresh):
                cv2.circle(canvass, (int(radiusloc[0] + x), int(radiusloc[1] + y)), int(radius), (255, 255, 255), -1)
                j=j+1
        result = cv2.bitwise_and(im,im,mask=canvass)
        h, w, c = result.shape
        canvass_pix = QImage(result.data, w, h, 3*w, QImage.Format_RGB888)
        canvass_fpix = QPixmap.fromImage(canvass_pix)
        pixmap = canvass_fpix.scaled(self.tenpesoLbl.width(), self.tenpesoLbl.height(),
                                     QtCore.Qt.KeepAspectRatio)  # Scale pixmap
        self.tenpesoLbl.setPixmap(pixmap)  # Set the pixmap onto the label
        self.tenpesoLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.countcoin10.setText(str(j))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



