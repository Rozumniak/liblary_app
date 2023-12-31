from PyQt6 import QtCore, QtGui, QtWidgets
import os
class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(380, 600)
        Login.setStyleSheet("background-color: rgb(255, 255, 240);")
        self.login_input = QtWidgets.QLineEdit(parent=Login)
        self.login_input.setGeometry(QtCore.QRect(180, 240, 130, 40))
        self.login_input.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.login_input.setStyleSheet("border-radius: 10px;\n"
                                       "border: 2px solid rgb(164, 201, 255);\n"
                                       "background-color: white;\n"
                                       "padding: 10px;")
        self.login_input.setInputMask("")
        self.login_input.setText("")
        self.login_input.setObjectName("login_input")

        self.password_input = QtWidgets.QLineEdit(parent=Login)
        self.password_input.setGeometry(QtCore.QRect(180, 330, 130, 40))
        self.password_input.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.password_input.setStyleSheet("border-radius: 10px;\n"
                                          "border: 2px solid rgb(164, 201, 255);\n"
                                          "background-color: white;\n"
                                          "padding: 10px;")
        self.password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password_input.setObjectName("password_input")

        self.password_issue = QtWidgets.QLabel(parent=Login)
        self.password_issue.setGeometry(QtCore.QRect(180, 370, 200, 35))
        self.password_issue.setStyleSheet("color: red;\n"
"font: 12pt \"Arial\";")
        self.pushButton = QtWidgets.QPushButton(parent=Login)
        self.pushButton.setGeometry(QtCore.QRect(115, 480, 150, 42))
        self.pushButton.setStyleSheet("border-radius: 10px;\n"
"font: 87 14pt \"Arial\";\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(164, 201, 255);\n"
"padding: 10px;\n"
"width: 130px;")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(parent=Login)
        self.label.setGeometry(QtCore.QRect(105, 40, 170, 170))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(os.path.join(os.path.dirname(__file__), "logo.png")))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.login_issue = QtWidgets.QLabel(parent=Login)
        self.login_issue.setGeometry(QtCore.QRect(180, 280, 200, 35))
        self.login_issue.setStyleSheet("color: red;\n"
"font: 12pt \"Arial\";")
        self.login_issue.setObjectName("login_issue")
        self.password_label = QtWidgets.QLabel(parent=Login)
        self.password_label.setGeometry(QtCore.QRect(60, 330, 110, 42))
        self.password_label.setStyleSheet("font: 87 14pt \"Arial\";\n"
"padding: 10px;\n"
"width: 130px;")
        self.password_label.setObjectName("password_label")
        self.login_label = QtWidgets.QLabel(parent=Login)
        self.login_label.setGeometry(QtCore.QRect(60, 240, 95, 42))
        self.login_label.setStyleSheet("font: 87 14pt \"Arial\";\n"
"padding: 10px;\n"
"width: 130px;")
        self.login_label.setObjectName("login_label")
        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)
    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Form"))
        self.password_issue.setText(_translate("Login", "TextLabel"))
        self.pushButton.setText(_translate("Login", "Вхід"))
        self.login_issue.setText(_translate("Login", "TextLabel"))
        self.password_label.setText(_translate("Login", "Пароль"))
        self.login_label.setText(_translate("Login", "Логін"))
