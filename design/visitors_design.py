from PyQt6 import QtCore, QtGui, QtWidgets
import os
class Ui_Visitorssearch(object):
    def setupUi(self, Visitorssearch):
        Visitorssearch.setObjectName("Visitorssearch")
        Visitorssearch.resize(1107, 719)
        Visitorssearch.setStyleSheet("background-color: rgb(255, 255, 240);")
        self.centralwidget = QtWidgets.QWidget(parent=Visitorssearch)
        self.centralwidget.setObjectName("centralwidget")
        self.visitors_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.visitors_button.setGeometry(QtCore.QRect(1010, 113, 95, 90))
        self.visitors_button.setStyleSheet("border-radius: 10px;\n"
"border: 2px solid rgb(127, 165, 206);\n"
"background-color: rgb(233, 243, 255);\n"
"font: 13pt \"Arial\";\n"
"padding 5px;\n"
"")
        self.visitors_button.setObjectName("visitors_button")
        self.books_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.books_button.setGeometry(QtCore.QRect(1010, 20, 95, 90))
        self.books_button.setStyleSheet("border-radius: 10px;\n"
"border: 2px solid rgb(127, 165, 206);\n"
"background-color: rgb(164, 201, 255);\n"
"font: 13pt \"Arial\";\n"
"padding 5px;\n"
"")
        self.books_button.setObjectName("books_button")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(70, 180, 931, 501))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 929, 499))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.name = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.name.setGeometry(QtCore.QRect(210, 60, 411, 35))
        self.name.setStyleSheet("border-radius: 10px;\n"
"font: 14pt \"Arial\";\n"
"border: 2px solid rgb(164, 201, 255);\n"
"background-color: white;\n"
"")
        self.name.setObjectName("name")
        self.search_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.search_button.setGeometry(QtCore.QRect(640, 60, 75, 35))
        self.search_button.setStyleSheet("border-radius: 10px;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(164, 201, 255);\n"
"font: 13pt \"Arial\";\n"
"")
        self.search_button.setObjectName("search_button")
        self.register_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.register_button.setGeometry(QtCore.QRect(800, 10, 125, 35))
        self.register_button.setStyleSheet("border-radius: 10px;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(164, 201, 255);\n"
"font: 13pt \"Arial\";\n"
"")
        self.register_button.setObjectName("register_button")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 120, 120))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(os.path.join(os.path.dirname(__file__), "logo.png")))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.name_issue = QtWidgets.QLabel(parent=self.centralwidget)
        self.name_issue.setGeometry(QtCore.QRect(210, 100, 200, 35))
        self.name_issue.setStyleSheet("color: red;\n"
"font: 12pt \"Arial\";")
        self.name_issue.setObjectName("name_issue")
        Visitorssearch.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=Visitorssearch)
        self.statusbar.setObjectName("statusbar")
        Visitorssearch.setStatusBar(self.statusbar)
        self.retranslateUi(Visitorssearch)
        QtCore.QMetaObject.connectSlotsByName(Visitorssearch)
    def retranslateUi(self, Visitorssearch):
        _translate = QtCore.QCoreApplication.translate
        Visitorssearch.setWindowTitle(_translate("Visitorssearch", "MainWindow"))
        self.visitors_button.setText(_translate("Visitorssearch", "Відвідувачі"))
        self.books_button.setText(_translate("Visitorssearch", "Книги"))
        self.name.setPlaceholderText(_translate("Visitorssearch", "Введіть прізвище або ім\'я"))
        self.search_button.setText(_translate("Visitorssearch", "Пошук"))
        self.register_button.setText(_translate("Visitorssearch", "Зареєструвати"))
        self.name_issue.setText(_translate("Visitorssearch", "TextLabel"))
