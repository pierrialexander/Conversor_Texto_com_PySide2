# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'conversor_design.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setSizeIncrement(QSize(0, 0))
        MainWindow.setStyleSheet(u"background-color: rgb(208, 210, 211);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_insira = QLabel(self.centralwidget)
        self.label_insira.setObjectName(u"label_insira")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_insira.setFont(font)

        self.gridLayout_2.addWidget(self.label_insira, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.radio_maiusculo = QRadioButton(self.centralwidget)
        self.radio_maiusculo.setObjectName(u"radio_maiusculo")
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(True)
        font1.setWeight(75)
        self.radio_maiusculo.setFont(font1)
        self.radio_maiusculo.setStyleSheet(u"")

        self.gridLayout.addWidget(self.radio_maiusculo, 1, 0, 1, 1)

        self.radio_minusculo = QRadioButton(self.centralwidget)
        self.radio_minusculo.setObjectName(u"radio_minusculo")
        self.radio_minusculo.setFont(font1)

        self.gridLayout.addWidget(self.radio_minusculo, 1, 1, 1, 1)

        self.textEdit_resultado = QTextEdit(self.centralwidget)
        self.textEdit_resultado.setObjectName(u"textEdit_resultado")
        self.textEdit_resultado.setStyleSheet(u"border: 2px solid gray;\n"
"border-radius: 10px;\n"
"padding: 8 8px;\n"
"background: #EEE9E9;\n"
"font: 12pt \"Calibri\";\n"
"")

        self.gridLayout.addWidget(self.textEdit_resultado, 6, 0, 1, 4)

        self.textEdit_origem = QTextEdit(self.centralwidget)
        self.textEdit_origem.setObjectName(u"textEdit_origem")
        self.textEdit_origem.setStyleSheet(u"border: 2px solid gray;\n"
"border-radius: 10px;\n"
"padding: 8 8px;\n"
"background: #EEE9E9;\n"
"font: 12pt \"Calibri\";\n"
"")

        self.gridLayout.addWidget(self.textEdit_origem, 0, 0, 1, 4)

        self.radio_primeira = QRadioButton(self.centralwidget)
        self.radio_primeira.setObjectName(u"radio_primeira")
        self.radio_primeira.setFont(font1)

        self.gridLayout.addWidget(self.radio_primeira, 1, 2, 1, 1)

        self.label_resultado = QLabel(self.centralwidget)
        self.label_resultado.setObjectName(u"label_resultado")
        self.label_resultado.setFont(font)

        self.gridLayout.addWidget(self.label_resultado, 5, 0, 1, 1)

        self.button_converter = QPushButton(self.centralwidget)
        self.button_converter.setObjectName(u"button_converter")
        self.button_converter.setFont(font)
        self.button_converter.setStyleSheet(u"border: 2px solid gray;\n"
"border-radius: 6px;\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"hover: red;\n"
"\n"
"")

        self.gridLayout.addWidget(self.button_converter, 1, 3, 1, 1)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"border: 2px solid gray;\n"
"border-radius: 6px;\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);")

        self.gridLayout.addWidget(self.pushButton, 5, 3, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Conversor de Texto", None))
        self.label_insira.setText(QCoreApplication.translate("MainWindow", u"Insira o Texto Aqui", None))
        self.radio_maiusculo.setText(QCoreApplication.translate("MainWindow", u"MAIUSCULO", None))
        self.radio_minusculo.setText(QCoreApplication.translate("MainWindow", u"minusculo", None))
        self.radio_primeira.setText(QCoreApplication.translate("MainWindow", u"Primeiras Em Maiusculo", None))
        self.label_resultado.setText(QCoreApplication.translate("MainWindow", u"Resultado", None))
        self.button_converter.setText(QCoreApplication.translate("MainWindow", u"Converter", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Limpar", None))
    # retranslateUi

