# Form implementation generated from reading ui file 'new_worker_design.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


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
        self.layoutWidget = QtWidgets.QWidget(parent=NewWorker)
        self.layoutWidget.setGeometry(QtCore.QRect(120, 40, 482, 326))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label.setStyleSheet("font: 14pt \"Arial\";\n"
"background-color: white;\n"
"border: 2px solid rgb(164, 201, 255);\n"
"border-radius: 10px;")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_3.setStyleSheet("font: 14pt \"Arial\";\n"
"background-color: white;\n"
"border: 2px solid rgb(164, 201, 255);\n"
"border-radius: 10px;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.label_5 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_5.setStyleSheet("font: 14pt \"Arial\";\n"
"background-color: white;\n"
"border: 2px solid rgb(164, 201, 255);\n"
"border-radius: 10px;")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.label_4 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_4.setStyleSheet("font: 14pt \"Arial\";\n"
"background-color: white;\n"
"border: 2px solid rgb(164, 201, 255);\n"
"border-radius: 10px;")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.name = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.name.setStyleSheet("border-radius: 10px;\n"
"font: 12pt \"Arial\";\n"
"border: 2px solid rgb(164, 201, 255);\n"
"background-color: white;\n"
"")
        self.name.setObjectName("name")
        self.verticalLayout.addWidget(self.name)
        self.name_issue = QtWidgets.QLabel(parent=self.layoutWidget)
        self.name_issue.setStyleSheet("color: red;\n"
"font: 12pt \"Arial\";")
        self.name_issue.setObjectName("name_issue")
        self.verticalLayout.addWidget(self.name_issue)
        self.job_title = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.job_title.setStyleSheet("border-radius: 10px;\n"
"font: 12pt \"Arial\";\n"
"border: 2px solid rgb(164, 201, 255);\n"
"background-color: white;\n"
"")
        self.job_title.setObjectName("job_title")
        self.verticalLayout.addWidget(self.job_title)
        self.title_issue = QtWidgets.QLabel(parent=self.layoutWidget)
        self.title_issue.setStyleSheet("color: red;\n"
"font: 12pt \"Arial\";")
        self.title_issue.setObjectName("title_issue")
        self.verticalLayout.addWidget(self.title_issue)
        self.login = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.login.setStyleSheet("border-radius: 10px;\n"
"font: 12pt \"Arial\";\n"
"border: 2px solid rgb(164, 201, 255);\n"
"background-color: white;\n"
"")
        self.login.setObjectName("login")
        self.verticalLayout.addWidget(self.login)
        self.login_issue = QtWidgets.QLabel(parent=self.layoutWidget)
        self.login_issue.setStyleSheet("color: red;\n"
"font: 12pt \"Arial\";")
        self.login_issue.setObjectName("login_issue")
        self.verticalLayout.addWidget(self.login_issue)
        self.password = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.password.setStyleSheet("border-radius: 10px;\n"
"font: 12pt \"Arial\";\n"
"border: 2px solid rgb(164, 201, 255);\n"
"background-color: white;\n"
"")
        self.password.setObjectName("password")
        self.verticalLayout.addWidget(self.password)
        self.password_issue = QtWidgets.QLabel(parent=self.layoutWidget)
        self.password_issue.setStyleSheet("color: red;\n"
"font: 12pt \"Arial\";")
        self.password_issue.setObjectName("password_issue")
        self.verticalLayout.addWidget(self.password_issue)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.retranslateUi(NewWorker)
        QtCore.QMetaObject.connectSlotsByName(NewWorker)

    def retranslateUi(self, NewWorker):
        _translate = QtCore.QCoreApplication.translate
        NewWorker.setWindowTitle(_translate("NewWorker", "Form"))
        self.register_button.setText(_translate("NewWorker", "Додати"))
        self.back_button.setText(_translate("NewWorker", "Назад"))
        self.label.setText(_translate("NewWorker", "Ім\'я та прізвище працівника"))
        self.label_3.setText(_translate("NewWorker", "Посада"))
        self.label_5.setText(_translate("NewWorker", "Логін"))
        self.label_4.setText(_translate("NewWorker", "Пароль"))
        self.name_issue.setText(_translate("NewWorker", "TextLabel"))
        self.title_issue.setText(_translate("NewWorker", "TextLabel"))
        self.login_issue.setText(_translate("NewWorker", "TextLabel"))
        self.password_issue.setText(_translate("NewWorker", "TextLabel"))