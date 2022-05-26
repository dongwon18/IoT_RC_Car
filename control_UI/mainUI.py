# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUI.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide2.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPlainTextEdit, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.logText = QPlainTextEdit(self.centralwidget)
        self.logText.setObjectName(u"logText")
        self.logText.setGeometry(QRect(20, 50, 461, 281))
        self.startButton = QPushButton(self.centralwidget)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setGeometry(QRect(790, 350, 93, 28))
        self.stopButton = QPushButton(self.centralwidget)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setGeometry(QRect(690, 350, 93, 28))
        self.goButton = QPushButton(self.centralwidget)
        self.goButton.setObjectName(u"goButton")
        self.goButton.setGeometry(QRect(250, 340, 93, 28))
        self.midButton = QPushButton(self.centralwidget)
        self.midButton.setObjectName(u"midButton")
        self.midButton.setGeometry(QRect(250, 380, 93, 28))
        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setGeometry(QRect(250, 410, 93, 28))
        self.rightButton = QPushButton(self.centralwidget)
        self.rightButton.setObjectName(u"rightButton")
        self.rightButton.setGeometry(QRect(350, 380, 93, 28))
        self.leftButton = QPushButton(self.centralwidget)
        self.leftButton.setObjectName(u"leftButton")
        self.leftButton.setGeometry(QRect(150, 380, 93, 28))
        self.sensingText = QPlainTextEdit(self.centralwidget)
        self.sensingText.setObjectName(u"sensingText")
        self.sensingText.setGeometry(QRect(490, 50, 600, 281))
        font = QFont()
        font.setFamilies([u"Consolas"])
        self.sensingText.setFont(font)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 101, 21))
        self.temp_label = QLabel(self.centralwidget)
        self.temp_label.setObjectName(u"temp_label")
        self.temp_label.setGeometry(QRect(690,400, 200, 21))
        self.humi_label = QLabel(self.centralwidget)
        self.humi_label.setObjectName(u"humi_label")
        self.humi_label.setGeometry(QRect(690,450, 200, 21))
        self.status_text = QLabel(self.centralwidget)
        self.status_text.setObjectName(u"status_text")
        self.status_text.setGeometry(QRect(690, 500, 100, 21))
        label_font = QFont()
        label_font.setBold(True)
        self.status_text.setFont(label_font)
        self.direction_text = QLabel(self.centralwidget)
        self.direction_text.setObjectName(u"direction_text")
        self.direction_text.setGeometry(QRect(800, 500, 100, 21))
        self.direction_text.setFont(label_font)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 934, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.startButton.clicked.connect(MainWindow.start)
        self.stopButton.clicked.connect(MainWindow.stop)
        self.goButton.clicked.connect(MainWindow.go)
        self.rightButton.clicked.connect(MainWindow.right)
        self.midButton.clicked.connect(MainWindow.mid)
        self.backButton.clicked.connect(MainWindow.back)
        self.leftButton.clicked.connect(MainWindow.left)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.stopButton.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.goButton.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.midButton.setText(QCoreApplication.translate("MainWindow", u"Mid", None))
        self.backButton.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.rightButton.setText(QCoreApplication.translate("MainWindow", u"Right", None))
        self.leftButton.setText(QCoreApplication.translate("MainWindow", u"Left", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"command Table", None))
        self.temp_label.setText(QCoreApplication.translate("MainWindow", u"temperature: C", None))
        self.humi_label.setText(QCoreApplication.translate("MainWindow", u"humidity: %", None))
        self.status_text.setText(QCoreApplication.translate("MainWindow", u"Ready", None))
        self.direction_text.setText(QCoreApplication.translate("MainWindow", u"Ready", None))


    # retranslateUi

