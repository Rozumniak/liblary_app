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
        self.layoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 230, 251, 232))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.login_label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.login_label.setStyleSheet("font: 87 14pt \"Arial\";\n"
"padding: 10px;\n"
"width: 130px;")
        self.login_label.setObjectName("login_label")
        self.gridLayout.addWidget(self.login_label, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 38, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 0, 2, 1)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 1, 2, 1)
        self.login_input = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.login_input.setStyleSheet("border-radius: 10px;\n"
"border: 2px solid rgb(164, 201, 255);\n"
"background-color: white;\n"
"padding: 10px;")
        self.login_input.setInputMask("")
        self.login_input.setText("")
        self.login_input.setObjectName("login_input")
        self.gridLayout.addWidget(self.login_input, 0, 2, 2, 2)
        self.password_label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.password_label.setStyleSheet("font: 87 14pt \"Arial\";\n"
"padding: 10px;\n"
"width: 130px;")
        self.password_label.setObjectName("password_label")
        self.gridLayout.addWidget(self.password_label, 3, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem3, 3, 1, 1, 1)
        self.password_input = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.password_input.setStyleSheet("border-radius: 10px;\n"
"border: 2px solid rgb(164, 201, 255);\n"
"background-color: white;\n"
"padding: 10px;")
        self.password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password_input.setObjectName("password_input")
        self.gridLayout.addWidget(self.password_input, 3, 2, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 108, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.pushButton = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.pushButton.setStyleSheet("border-radius: 10px;\n"
"font: 87 14pt \"Arial\";\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(164, 201, 255);\n"
"padding: 10px;\n"
"width: 130px;")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout)
        Login.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=Login)
        self.statusbar.setObjectName("statusbar")
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "MainWindow"))
        self.login_label.setText(_translate("Login", "Логін"))
        self.password_label.setText(_translate("Login", "Пароль"))
        self.pushButton.setText(_translate("Login", "Вхід"))