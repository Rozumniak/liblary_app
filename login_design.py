# Form implementation generated from reading ui file 'login_design.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(379, 600)
        Login.setStyleSheet("background-color: rgb(255, 255, 240);")
        self.centralwidget = QtWidgets.QWidget(parent=Login)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(115, 30, 170, 170))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Designer-removebg-preview.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 470, 150, 42))
        self.pushButton.setStyleSheet("border-radius: 10px;\n"
"font: 87 14pt \"Arial\";\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(164, 201, 255);\n"
"padding: 10px;\n"
"width: 130px;")
        self.pushButton.setObjectName("pushButton")
        self.login_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.login_label.setGeometry(QtCore.QRect(70, 230, 95, 42))
        self.login_label.setStyleSheet("font: 87 14pt \"Arial\";\n"
"padding: 10px;\n"
"width: 130px;")
        self.login_label.setObjectName("login_label")
        self.password_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(70, 320, 95, 42))
        self.password_label.setStyleSheet("font: 87 14pt \"Arial\";\n"
"padding: 10px;\n"
"width: 130px;")
        self.password_label.setObjectName("password_label")
        self.login_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.login_input.setGeometry(QtCore.QRect(190, 230, 130, 40))
        self.login_input.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.login_input.setStyleSheet("border-radius: 10px;\n"
"border: 2px solid rgb(164, 201, 255);\n"
"background-color: white;\n"
"padding: 10px;")
        self.login_input.setInputMask("")
        self.login_input.setText("")
        self.login_input.setObjectName("login_input")
        self.password_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.password_input.setGeometry(QtCore.QRect(190, 320, 130, 40))
        self.password_input.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.password_input.setStyleSheet("border-radius: 10px;\n"
"border: 2px solid rgb(164, 201, 255);\n"
"background-color: white;\n"
"padding: 10px;")
        self.password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password_input.setObjectName("password_input")
        self.login_issue = QtWidgets.QLabel(parent=self.centralwidget)
        self.login_issue.setGeometry(QtCore.QRect(190, 270, 200, 35))
        self.login_issue.setStyleSheet("color: red;\n"
"font: 12pt \"Arial\";")
        self.login_issue.setObjectName("login_issue")
        self.password_issue = QtWidgets.QLabel(parent=self.centralwidget)
        self.password_issue.setGeometry(QtCore.QRect(190, 360, 200, 35))
        self.password_issue.setStyleSheet("color: red;\n"
"font: 12pt \"Arial\";")
        self.password_issue.setObjectName("password_issue")
        Login.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=Login)
        self.statusbar.setObjectName("statusbar")
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "MainWindow"))
        self.pushButton.setText(_translate("Login", "Вхід"))
        self.login_label.setText(_translate("Login", "Логін"))
        self.password_label.setText(_translate("Login", "Пароль"))
        self.login_issue.setText(_translate("Login", "TextLabel"))
        self.password_issue.setText(_translate("Login", "TextLabel"))
