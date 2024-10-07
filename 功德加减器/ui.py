# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QListView, QPushButton,
    QSizePolicy, QWidget)
import pic

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(406, 261)
        Form.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.pushButton_plus = QPushButton(Form)
        self.pushButton_plus.setObjectName(u"pushButton_plus")
        self.pushButton_plus.setGeometry(QRect(160, 180, 80, 25))
        self.pushButton_minud = QPushButton(Form)
        self.pushButton_minud.setObjectName(u"pushButton_minud")
        self.pushButton_minud.setGeometry(QRect(160, 220, 80, 25))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 90, 111, 41))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.label.setPalette(palette)
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-image: url(:/blue.png);")
        self.listView = QListView(Form)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(-5, 1, 421, 261))
        self.listView.setStyleSheet(u"background-image: url(:/03.png);")
        self.listView.raise_()
        self.pushButton_plus.raise_()
        self.pushButton_minud.raise_()
        self.label.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u529f\u5fb7\u52a0\u51cf\u5668", None))
        self.pushButton_plus.setText(QCoreApplication.translate("Form", u"\u529f\u5fb7+1", None))
        self.pushButton_minud.setText(QCoreApplication.translate("Form", u"\u529f\u5fb7-1", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u529f\u5fb7\u52a0\u51cf\u5668", None))
    # retranslateUi

