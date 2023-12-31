from PyQt6 import QtCore, QtGui, QtWidgets
class Ui_NewBook(object):
    def setupUi(self, NewBook):
        NewBook.setObjectName("NewBook")
        NewBook.resize(700, 499)
        NewBook.setStyleSheet("background-color: rgb(255, 255, 240);")
        self.register_button = QtWidgets.QPushButton(parent=NewBook)
        self.register_button.setGeometry(QtCore.QRect(560, 410, 120, 40))
        self.register_button.setStyleSheet("border-radius: 10px;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(164, 201, 255);\n"
"font: 12pt \"Arial\";\n"
"")
        self.register_button.setObjectName("register_button")
        self.back_button = QtWidgets.QPushButton(parent=NewBook)
        self.back_button.setGeometry(QtCore.QRect(40, 410, 90, 40))
        self.back_button.setStyleSheet("border-radius: 10px;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(164, 201, 255);\n"
"font: 12pt \"Arial\";\n"
"")
        self.back_button.setObjectName("back_button")
        self.label_5 = QtWidgets.QLabel(parent=NewBook)
        self.label_5.setGeometry(QtCore.QRect(100, 230, 230, 30))
        self.label_5.setStyleSheet("font: 14pt \"Arial\";\n"
"background-color: white;\n"
"border: 2px solid rgb(164, 201, 255);\n"
"border-radius: 10px;")
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(parent=NewBook)
        self.label.setGeometry(QtCore.QRect(100, 70, 230, 30))
        self.label.setStyleSheet("font: 14pt \"Arial\";\n"
"background-color: white;\n"
"border: 2px solid rgb(164, 201, 255);\n"
"border-radius: 10px;")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(parent=NewBook)
        self.label_4.setGeometry(QtCore.QRect(100, 310, 230, 30))
        self.label_4.setStyleSheet("font: 14pt \"Arial\";\n"
"background-color: white;\n"
"border: 2px solid rgb(164, 201, 255);\n"
"border-radius: 10px;")
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(parent=NewBook)
        self.label_3.setGeometry(QtCore.QRect(100, 150, 230, 30))
        self.label_3.setStyleSheet("font: 14pt \"Arial\";\n"
"background-color: white;\n"
"border: 2px solid rgb(164, 201, 255);\n"
"border-radius: 10px;")
        self.label_3.setObjectName("label_3")
        self.number = QtWidgets.QLineEdit(parent=NewBook)
        self.number.setGeometry(QtCore.QRect(370, 310, 250, 30))
        self.number.setStyleSheet("border-radius: 10px;\n"
"font: 12pt \"Arial\";\n"
"border: 2px solid rgb(164, 201, 255);\n"
"background-color: white;\n"
"")
        self.number.setObjectName("number")
        self.genre = QtWidgets.QLineEdit(parent=NewBook)
        self.genre.setGeometry(QtCore.QRect(370, 230, 250, 30))
        self.genre.setStyleSheet("border-radius: 10px;\n"
"font: 12pt \"Arial\";\n"
"border: 2px solid rgb(164, 201, 255);\n"
"background-color: white;\n"
"")
        self.genre.setObjectName("genre")
        self.title = QtWidgets.QLineEdit(parent=NewBook)
        self.title.setGeometry(QtCore.QRect(370, 150, 250, 30))
        self.title.setStyleSheet("border-radius: 10px;\n"
"font: 12pt \"Arial\";\n"
"border: 2px solid rgb(164, 201, 255);\n"
"background-color: white;\n"
"")
        self.title.setObjectName("title")
        self.name = QtWidgets.QLineEdit(parent=NewBook)
        self.name.setGeometry(QtCore.QRect(370, 70, 250, 30))
        self.name.setStyleSheet("border-radius: 10px;\n"
"font: 12pt \"Arial\";\n"
"border: 2px solid rgb(164, 201, 255);\n"
"background-color: white;\n"
"")
        self.name.setObjectName("name")
        self.name_issue = QtWidgets.QLabel(parent=NewBook)
        self.name_issue.setGeometry(QtCore.QRect(370, 100, 200, 35))
        self.name_issue.setStyleSheet("color: red;\n"
"font: 12pt \"Arial\";")
        self.name_issue.setObjectName("name_issue")
        self.title_issue = QtWidgets.QLabel(parent=NewBook)
        self.title_issue.setGeometry(QtCore.QRect(370, 180, 200, 35))
        self.title_issue.setStyleSheet("color: red;\n"
"font: 12pt \"Arial\";")
        self.title_issue.setObjectName("title_issue")
        self.genre_issue = QtWidgets.QLabel(parent=NewBook)
        self.genre_issue.setGeometry(QtCore.QRect(370, 260, 200, 35))
        self.genre_issue.setStyleSheet("color: red;\n"
"font: 12pt \"Arial\";")
        self.genre_issue.setObjectName("genre_issue")
        self.number_issue = QtWidgets.QLabel(parent=NewBook)
        self.number_issue.setGeometry(QtCore.QRect(370, 340, 200, 35))
        self.number_issue.setStyleSheet("color: red;\n"
"font: 12pt \"Arial\";")
        self.number_issue.setObjectName("number_issue")
        self.retranslateUi(NewBook)
        QtCore.QMetaObject.connectSlotsByName(NewBook)
    def retranslateUi(self, NewBook):
        _translate = QtCore.QCoreApplication.translate
        NewBook.setWindowTitle(_translate("NewBook", "Form"))
        self.register_button.setText(_translate("NewBook", "Додати"))
        self.back_button.setText(_translate("NewBook", "Назад"))
        self.label_5.setText(_translate("NewBook", "Жанр"))
        self.label.setText(_translate("NewBook", "Ім\'я та прізвище автора"))
        self.label_4.setText(_translate("NewBook", "Кількість"))
        self.label_3.setText(_translate("NewBook", "Назва"))
        self.name_issue.setText(_translate("NewBook", "TextLabel"))
        self.title_issue.setText(_translate("NewBook", "TextLabel"))
        self.genre_issue.setText(_translate("NewBook", "TextLabel"))
        self.number_issue.setText(_translate("NewBook", "TextLabel"))
