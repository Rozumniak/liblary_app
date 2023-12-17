
from PyQt6 import QtWidgets, QtCore
from design.login_design import Ui_Login
from database import searchWorker

class LoginWindow(QtWidgets.QWidget, QtCore.QObject, Ui_Login):
    login_successful = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(380, 600)
        self.pushButton.clicked.connect(self.buttonClicked)
        self.login_issue.hide()
        self.password_issue.hide()
        self.login_input.setFocus()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key.Key_Enter or event.key() == QtCore.Qt.Key.Key_Return:
            self.buttonClicked()

    def buttonClicked(self):
        from classes.newWorker import NewWorker
        login = self.login_input.text().strip()
        password = self.password_input.text().strip()
        worker = searchWorker(login, password)
        has_errors = False

        if login == '':
            self.login_issue.show()
            self.login_issue.setText("Поле пусте")
            self.login_input.setStyleSheet("border-radius: 10px;\n"
                                    "font: 12pt \"Arial\";\n"
                                    "border: 2px solid red;\n"
                                    "background-color: white;\n"
                                    "")
            has_errors = True
        else:
            self.login_issue.hide()
            self.login_input.setStyleSheet("border-radius: 10px;\n"
                                     "font: 12pt \"Arial\";\n"
                                     "border: 2px solid rgb(164, 201, 255);\n"
                                     "background-color: white;\n"
                                     "")

        if password == '':
            self.password_issue.show()
            self.password_issue.setText("Поле пусте")
            self.password_input.setStyleSheet("border-radius: 10px;\n"
                                    "font: 12pt \"Arial\";\n"
                                    "border: 2px solid red;\n"
                                    "background-color: white;\n"
                                    "")
            self.password_issue.move(190, self.password_issue.y())
            has_errors = True
        else:
            self.password_issue.hide()
            self.password_input.setStyleSheet("border-radius: 10px;\n"
                                     "font: 12pt \"Arial\";\n"
                                     "border: 2px solid rgb(164, 201, 255);\n"
                                     "background-color: white;\n"
                                     "")

        if has_errors:
            self.update()
        else:
            if worker == False:
                self.login_input.setStyleSheet("border-radius: 10px;\n"
                                               "font: 12pt \"Arial\";\n"
                                               "border: 2px solid red;\n"
                                               "background-color: white;\n"
                                               "")
                self.password_issue.show()
                self.password_issue.setText("Логін чи пароль введено невірно")
                self.password_issue.setFixedWidth(self.password_issue.width() + 45)
                self.password_issue.move(80, self.password_issue.y())
                self.password_input.setStyleSheet("border-radius: 10px;\n"
                                                  "font: 12pt \"Arial\";\n"
                                                  "border: 2px solid red;\n"
                                                  "background-color: white;\n"
                                                  "")

            elif worker[0][3] == 'admin' and worker[0][4] == 'admin':


                self.newWorker = NewWorker()
                self.newWorker.show()
            elif worker:
                self.login_successful.emit()
                self.hide()