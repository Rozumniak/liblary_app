from design.new_visitor_design import Ui_NewVisitor
from PyQt6 import QtWidgets, QtCore
from database import addVisitor
class NewVisitor(QtWidgets.QWidget, QtCore.QObject, Ui_NewVisitor):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Додати відвідувача")
        self.back_button.clicked.connect(self.backClicked)
        self.register_button.clicked.connect(self.registerClicked)
        self.secondName_issue.hide()
        self.firstName_issue.hide()
    def backClicked(self):
        self.close()
    def registerClicked(self):
        secondName = self.secondName.text().strip()
        firstName = self.firstName.text().strip()
        has_errors = False
        if secondName == '':
            self.secondName_issue.show()
            self.secondName_issue.setText("Поле пусте")
            self.secondName.setStyleSheet("border-radius: 10px;\n"
                                    "font: 12pt \"Arial\";\n"
                                    "border: 2px solid red;\n"
                                    "background-color: white;\n"
                                    "")
            has_errors = True
        elif any(char.isdigit() for char in str(secondName)):
            self.secondName_issue.show()
            self.secondName_issue.setText("Введені цифри")
            self.secondName.setStyleSheet("border-radius: 10px;\n"
                                    "font: 12pt \"Arial\";\n"
                                    "border: 2px solid red;\n"
                                    "background-color: white;\n"
                                    "")
            has_errors = True
        else:
            self.secondName_issue.hide()
            self.secondName.setStyleSheet("border-radius: 10px;\n"
                                    "font: 12pt \"Arial\";\n"
                                    "border: 2px solid rgb(164, 201, 255);\n"
                                    "background-color: white;\n"
                                    "")

        if firstName == '':
            self.firstName_issue.show()
            self.firstName_issue.setText("Поле пусте")
            self.firstName.setStyleSheet("border-radius: 10px;\n"
                                         "font: 12pt \"Arial\";\n"
                                         "border: 2px solid red;\n"
                                         "background-color: white;\n"
                                         "")
            has_errors = True
        elif any(char.isdigit() for char in str(firstName)):
            self.firstName_issue.show()
            self.firstName_issue.setText("Введені цифри")
            self.firstName.setStyleSheet("border-radius: 10px;\n"
                                         "font: 12pt \"Arial\";\n"
                                         "border: 2px solid red;\n"
                                         "background-color: white;\n"
                                         "")
            has_errors = True
        else:
            self.firstName_issue.hide()
            self.firstName.setStyleSheet("border-radius: 10px;\n"
                                         "font: 12pt \"Arial\";\n"
                                         "border: 2px solid rgb(164, 201, 255);\n"
                                         "background-color: white;\n"
                                         "")
        if has_errors:
            self.update()
        else:
            from classes.visitors import VisitorsSearch
            addVisitor(self.secondName.text(), self.firstName.text(), self.dateEdit.text())
            VisitorsSearch().searchButtonClicked()
            self.close()