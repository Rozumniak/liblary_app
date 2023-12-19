from PyQt6 import QtCore, QtGui, QtWidgets
class Ui_giveBook(object):
    def setupUi(self, giveBook):
        giveBook.setObjectName("giveBook")
        giveBook.resize(700, 500)
        giveBook.setStyleSheet("background-color: rgb(255, 255, 240);")
        self.search_button = QtWidgets.QPushButton(parent=giveBook)
        self.search_button.setGeometry(QtCore.QRect(318, 30, 75, 30))
        self.search_button.setStyleSheet("border-radius: 10px;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(164, 201, 255);\n"
"font: 12pt \"Arial\";\n"
"")
        self.search_button.setObjectName("search_button")
        self.id_field = QtWidgets.QLineEdit(parent=giveBook)
        self.id_field.setGeometry(QtCore.QRect(110, 30, 171, 30))
        self.id_field.setStyleSheet("border-radius: 10px;\n"
"font: 10pt \"Arial\";\n"
"border: 2px solid rgb(164, 201, 255);\n"
"background-color: white;\n"
"")
        self.id_field.setText("")
        self.id_field.setObjectName("id_field")
        self.background = QtWidgets.QLabel(parent=giveBook)
        self.background.setGeometry(QtCore.QRect(90, 100, 531, 311))
        self.background.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"font: 14pt \"Arial\";\n"
"text-align: center;")
        self.background.setText("")
        self.background.setObjectName("background")
        self.give_button = QtWidgets.QPushButton(parent=giveBook)
        self.give_button.setGeometry(QtCore.QRect(570, 450, 75, 30))
        self.give_button.setStyleSheet("border-radius: 10px;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(164, 201, 255);\n"
"font: 12pt \"Arial\";\n"
"")
        self.give_button.setObjectName("give_button")
        self.id_issue = QtWidgets.QLabel(parent=giveBook)
        self.id_issue.setGeometry(QtCore.QRect(110, 60, 200, 35))
        self.id_issue.setStyleSheet("color: red;\n"
"font: 12pt \"Arial\";")
        self.id_issue.setObjectName("id_issue")
        self.retranslateUi(giveBook)
        QtCore.QMetaObject.connectSlotsByName(giveBook)
    def retranslateUi(self, giveBook):
        _translate = QtCore.QCoreApplication.translate
        giveBook.setWindowTitle(_translate("giveBook", "Form"))
        self.search_button.setText(_translate("giveBook", "Пошук"))
        self.id_field.setPlaceholderText(_translate("giveBook", "Номер читатьського квитка"))
        self.give_button.setText(_translate("giveBook", "Видати"))
        self.id_issue.setText(_translate("giveBook", "TextLabel"))
