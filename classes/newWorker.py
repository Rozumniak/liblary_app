from PyQt6 import QtWidgets, QtCore
from design.new_worker_design import Ui_NewWorker
from database import addNewWorker
class NewWorker(QtWidgets.QWidget, QtCore.QObject, Ui_NewWorker):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.register_button.clicked.connect(self.newWorkerRegister)
        self.back_button.clicked.connect(self.backButtonClicked)
        self.name_issue.hide()
        self.title_issue.hide()
        self.login_issue.hide()
        self.password_issue.hide()
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key.Key_Enter or event.key() == QtCore.Qt.Key.Key_Return:
            self.newWorkerRegister()
    def newWorkerRegister(self):
        name_text = self.name.text().strip()
        title_text = self.job_title.text().strip()
        login_text = self.login.text().strip()
        password_text = self.password.text().strip()
        has_errors = False
        if name_text == '':
            self.name_issue.show()
            self.name_issue.setText("Поле пусте")
            self.name.setStyleSheet("border-radius: 10px;\n"
                                     "font: 12pt \"Arial\";\n"
                                     "border: 2px solid red;\n"
                                     "background-color: white;\n"
                                     "")
            has_errors = True
        elif name_text.isdigit():
            self.name_issue.show()
            self.name_issue.setText("Введені цифри")
            self.name.setStyleSheet("border-radius: 10px;\n"
                                    "font: 12pt \"Arial\";\n"
                                    "border: 2px solid red;\n"
                                    "background-color: white;\n"
                                    "")
            has_errors = True
        else:
            self.name_issue.hide()
            self.name.setStyleSheet("border-radius: 10px;\n"
                                     "font: 12pt \"Arial\";\n"
                                     "border: 2px solid rgb(164, 201, 255);\n"
                                     "background-color: white;\n"
                                     "")

        if title_text == '':
            self.title_issue.show()
            self.title_issue.setText("Поле пусте")
            self.job_title.setStyleSheet("border-radius: 10px;\n"
                                    "font: 12pt \"Arial\";\n"
                                    "border: 2px solid red;\n"
                                    "background-color: white;\n"
                                    "")
            has_errors = True
        elif title_text.isdigit():
            self.title_issue.show()
            self.title_issue.setText("Введені цифри")
            self.job_title.setStyleSheet("border-radius: 10px;\n"
                                    "font: 12pt \"Arial\";\n"
                                    "border: 2px solid red;\n"
                                    "background-color: white;\n"
                                    "")
            has_errors = True
        else:
            self.title_issue.hide()
            self.job_title.setStyleSheet("border-radius: 10px;\n"
                                     "font: 12pt \"Arial\";\n"
                                     "border: 2px solid rgb(164, 201, 255);\n"
                                     "background-color: white;\n"
                                     "")

        if login_text == '':
            self.login_issue.show()
            self.login_issue.setText("Поле пусте")
            self.login.setStyleSheet("border-radius: 10px;\n"
                                    "font: 12pt \"Arial\";\n"
                                    "border: 2px solid red;\n"
                                    "background-color: white;\n"
                                    "")
            has_errors = True
        else:
            self.login_issue.hide()
            self.login.setStyleSheet("border-radius: 10px;\n"
                                     "font: 12pt \"Arial\";\n"
                                     "border: 2px solid rgb(164, 201, 255);\n"
                                     "background-color: white;\n"
                                     "")

        if password_text == '':
            self.password_issue.show()
            self.password_issue.setText("Поле пусте")
            self.password.setStyleSheet("border-radius: 10px;\n"
                                    "font: 12pt \"Arial\";\n"
                                    "border: 2px solid red;\n"
                                    "background-color: white;\n"
                                    "")
            has_errors = True
        else:
            self.password_issue.hide()
            self.password.setStyleSheet("border-radius: 10px;\n"
                                     "font: 12pt \"Arial\";\n"
                                     "border: 2px solid rgb(164, 201, 255);\n"
                                     "background-color: white;\n"
                                     "")

        if has_errors:
            self.update()
        else:
            workerAdded = addNewWorker(name_text, title_text, login_text, password_text)
            msg_box = QtWidgets.QMessageBox()
            if workerAdded:
                msg_box.setText(f"Додано нового працівника\n"
                                f"Логін: {workerAdded[0][3]}\n"
                                f"Пароль: {workerAdded[0][4]}")
                msg_box.setWindowTitle("Інфо")
                msg_box.exec()
            else:
                msg_box.setText("Не додано нового працівника")
                msg_box.setWindowTitle("Інфо")
                msg_box.exec()
    def backButtonClicked(self):
        self.close()
