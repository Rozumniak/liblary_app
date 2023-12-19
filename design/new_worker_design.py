from PyQt6 import QtCore, QtGui, QtWidgets
class Ui_NewWorker(object):
    def setupUi(self, NewWorker):
        NewWorker.setObjectName("NewWorker")
        NewWorker.resize(700, 499)
        NewWorker.setStyleSheet("background-color: rgb(255, 255, 240);")
        self.register_button = QtWidgets.QPushButton(parent=NewWorker)
        self.register_button.setGeometry(QtCore.QRect(560, 410, 120, 40))
        self.register_button.setStyleSheet("border-radius: 10px;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(164, 201, 255);\n"
"font: 12pt \"Arial\";\n"
"")
        self.register_button.setObjectName("register_button")
        self.back_button = QtWidgets.QPushButton(parent=NewWorker)
        self.back_button.setGeometry(QtCore.QRect(40, 410, 90, 40))
        self.back_button.setStyleSheet("border-radius: 10px;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(164, 201, 255);\n"
"font: 12pt \"Arial\";\n"
"")
        self.back_button.setObjectName("back_button")
        self.label_3 = QtWidgets.QLabel(parent=NewWorker)
        self.label_3.setGeometry(QtCore.QRect(90, 140, 250, 26))
        self.label_3.setStyleSheet("font: 14pt \"Arial\";\n"
"background-color: white;\n"
"border: 2px solid rgb(164, 201, 255);\n"
"border-radius: 10px;")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(parent=NewWorker)
        self.label_5.setGeometry(QtCore.QRect(90, 220, 250, 26))
        self.label_5.setStyleSheet("font: 14pt \"Arial\";\n"
"background-color: white;\n"
"border: 2px solid rgb(164, 201, 255);\n"
"border-radius: 10px;")
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(parent=NewWorker)
        self.label.setGeometry(QtCore.QRect(90, 60, 250, 26))
        self.label.setStyleSheet("font: 14pt \"Arial\";\n"
"background-color: white;\n"
"border: 2px solid rgb(164, 201, 255);\n"
"border-radius: 10px;")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(parent=NewWorker)
        self.label_4.setGeometry(QtCore.QRect(90, 310, 250, 26))
        self.label_4.setStyleSheet("font: 14pt \"Arial\";\n"
"background-color: white;\n"
"border: 2px solid rgb(164, 201, 255);\n"
"border-radius: 10px;")
        self.label_4.setObjectName("label_4")
        self.name_issue = QtWidgets.QLabel(parent=NewWorker)
        self.name_issue.setGeometry(QtCore.QRect(360, 85, 250, 46))
        self.name_issue.setStyleSheet("color: red;\n"
"font: 12pt \"Arial\";")
        self.name_issue.setObjectName("name_issue")
        self.password_issue = QtWidgets.QLabel(parent=NewWorker)
        self.password_issue.setGeometry(QtCore.QRect(360, 334, 250, 46))
        self.password_issue.setStyleSheet("color: red;\n"
"font: 12pt \"Arial\";")
        self.password_issue.setObjectName("password_issue")
        self.name = QtWidgets.QLineEdit(parent=NewWorker)
        self.name.setGeometry(QtCore.QRect(360, 60, 250, 26))
        self.name.setStyleSheet("border-radius: 10px;\n"
"font: 12pt \"Arial\";\n"
"border: 2px solid rgb(164, 201, 255);\n"
"background-color: white;\n"
"")
        self.name.setObjectName("name")
        self.title_issue = QtWidgets.QLabel(parent=NewWorker)
        self.title_issue.setGeometry(QtCore.QRect(360, 165, 250, 46))
        self.title_issue.setStyleSheet("color: red;\n"
"font: 12pt \"Arial\";")
        self.title_issue.setObjectName("title_issue")
        self.login_issue = QtWidgets.QLabel(parent=NewWorker)
        self.login_issue.setGeometry(QtCore.QRect(360, 245, 250, 46))
        self.login_issue.setStyleSheet("color: red;\n"
"font: 12pt \"Arial\";")
        self.login_issue.setObjectName("login_issue")
        self.password = QtWidgets.QLineEdit(parent=NewWorker)
        self.password.setGeometry(QtCore.QRect(360, 310, 250, 26))
        self.password.setStyleSheet("border-radius: 10px;\n"
"font: 12pt \"Arial\";\n"
"border: 2px solid rgb(164, 201, 255);\n"
"background-color: white;\n"
"")
        self.password.setObjectName("password")
        self.login = QtWidgets.QLineEdit(parent=NewWorker)
        self.login.setGeometry(QtCore.QRect(360, 220, 250, 26))
        self.login.setStyleSheet("border-radius: 10px;\n"
"font: 12pt \"Arial\";\n"
"border: 2px solid rgb(164, 201, 255);\n"
"background-color: white;\n"
"")
        self.login.setObjectName("login")
        self.job_title = QtWidgets.QLineEdit(parent=NewWorker)
        self.job_title.setGeometry(QtCore.QRect(360, 140, 250, 26))
        self.job_title.setStyleSheet("border-radius: 10px;\n"
"font: 12pt \"Arial\";\n"
"border: 2px solid rgb(164, 201, 255);\n"
"background-color: white;\n"
"")
        self.job_title.setObjectName("job_title")
        self.retranslateUi(NewWorker)
        QtCore.QMetaObject.connectSlotsByName(NewWorker)
    def retranslateUi(self, NewWorker):
        _translate = QtCore.QCoreApplication.translate
        NewWorker.setWindowTitle(_translate("NewWorker", "Form"))
        self.register_button.setText(_translate("NewWorker", "Додати"))
        self.back_button.setText(_translate("NewWorker", "Назад"))
        self.label_3.setText(_translate("NewWorker", "Посада"))
        self.label_5.setText(_translate("NewWorker", "Логін"))
        self.label.setText(_translate("NewWorker", "Ім\'я та прізвище працівника"))
        self.label_4.setText(_translate("NewWorker", "Пароль"))
        self.name_issue.setText(_translate("NewWorker", "TextLabel"))
        self.password_issue.setText(_translate("NewWorker", "TextLabel"))
        self.title_issue.setText(_translate("NewWorker", "TextLabel"))
        self.login_issue.setText(_translate("NewWorker", "TextLabel"))
