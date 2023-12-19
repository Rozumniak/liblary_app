from PyQt6 import QtCore, QtGui, QtWidgets
class Ui_NewVisitor(object):
    def setupUi(self, NewVisitor):
        NewVisitor.setObjectName("NewVisitor")
        NewVisitor.resize(700, 499)
        NewVisitor.setStyleSheet("background-color: rgb(255, 255, 240);")
        self.register_button = QtWidgets.QPushButton(parent=NewVisitor)
        self.register_button.setGeometry(QtCore.QRect(560, 410, 120, 40))
        self.register_button.setStyleSheet("border-radius: 10px;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(164, 201, 255);\n"
"font: 12pt \"Arial\";\n"
"")
        self.register_button.setObjectName("register_button")
        self.back_button = QtWidgets.QPushButton(parent=NewVisitor)
        self.back_button.setGeometry(QtCore.QRect(40, 410, 90, 40))
        self.back_button.setStyleSheet("border-radius: 10px;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(164, 201, 255);\n"
"font: 12pt \"Arial\";\n"
"")
        self.back_button.setObjectName("back_button")
        self.label_4 = QtWidgets.QLabel(parent=NewVisitor)
        self.label_4.setGeometry(QtCore.QRect(130, 300, 155, 30))
        self.label_4.setStyleSheet("font: 14pt \"Arial\";\n"
"background-color: white;\n"
"border: 2px solid rgb(164, 201, 255);\n"
"border-radius: 10px;")
        self.label_4.setObjectName("label_4")
        self.dateEdit = QtWidgets.QDateEdit(parent=NewVisitor)
        self.dateEdit.setGeometry(QtCore.QRect(360, 300, 166, 24))
        self.dateEdit.setStyleSheet("border-radius: 10px;\n"
"font: 12pt \"Arial\";\n"
"border: 2px solid rgb(164, 201, 255);\n"
"background-color: white;\n"
"")
        self.dateEdit.setObjectName("dateEdit")
        self.secondName = QtWidgets.QLineEdit(parent=NewVisitor)
        self.secondName.setGeometry(QtCore.QRect(360, 100, 166, 24))
        self.secondName.setStyleSheet("border-radius: 10px;\n"
"font: 12pt \"Arial\";\n"
"border: 2px solid rgb(164, 201, 255);\n"
"background-color: white;\n"
"")
        self.secondName.setObjectName("secondName")
        self.label = QtWidgets.QLabel(parent=NewVisitor)
        self.label.setGeometry(QtCore.QRect(130, 100, 155, 30))
        self.label.setStyleSheet("font: 14pt \"Arial\";\n"
"background-color: white;\n"
"border: 2px solid rgb(164, 201, 255);\n"
"border-radius: 10px;")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(parent=NewVisitor)
        self.label_3.setGeometry(QtCore.QRect(130, 200, 155, 30))
        self.label_3.setStyleSheet("font: 14pt \"Arial\";\n"
"background-color: white;\n"
"border: 2px solid rgb(164, 201, 255);\n"
"border-radius: 10px;\n"
"")
        self.label_3.setObjectName("label_3")
        self.firstName = QtWidgets.QLineEdit(parent=NewVisitor)
        self.firstName.setGeometry(QtCore.QRect(360, 200, 166, 24))
        self.firstName.setStyleSheet("border-radius: 10px;\n"
"font: 12pt \"Arial\";\n"
"border: 2px solid rgb(164, 201, 255);\n"
"background-color: white;\n"
"")
        self.firstName.setObjectName("firstName")
        self.secondName_issue = QtWidgets.QLabel(parent=NewVisitor)
        self.secondName_issue.setGeometry(QtCore.QRect(360, 130, 200, 35))
        self.secondName_issue.setStyleSheet("color: red;\n"
"font: 12pt \"Arial\";")
        self.secondName_issue.setObjectName("secondName_issue")
        self.firstName_issue = QtWidgets.QLabel(parent=NewVisitor)
        self.firstName_issue.setGeometry(QtCore.QRect(360, 230, 200, 35))
        self.firstName_issue.setStyleSheet("color: red;\n"
"font: 12pt \"Arial\";")
        self.firstName_issue.setObjectName("firstName_issue")
        self.retranslateUi(NewVisitor)
        QtCore.QMetaObject.connectSlotsByName(NewVisitor)
    def retranslateUi(self, NewVisitor):
        _translate = QtCore.QCoreApplication.translate
        NewVisitor.setWindowTitle(_translate("NewVisitor", "Form"))
        self.register_button.setText(_translate("NewVisitor", "Зареєструвати"))
        self.back_button.setText(_translate("NewVisitor", "Назад"))
        self.label_4.setText(_translate("NewVisitor", "Дата реєстрації:"))
        self.label.setText(_translate("NewVisitor", "Прізвище:"))
        self.label_3.setText(_translate("NewVisitor", "Ім\'я:"))
        self.secondName_issue.setText(_translate("NewVisitor", "TextLabel"))
        self.firstName_issue.setText(_translate("NewVisitor", "TextLabel"))
