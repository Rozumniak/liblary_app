from PyQt6 import QtWidgets, QtCore
from design.new_book_design import Ui_NewBook
from database import addNewBook
class AddNewBook(QtWidgets.QWidget, QtCore.QObject, Ui_NewBook):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.register_button.clicked.connect(self.addNewBook)
        self.back_button.clicked.connect(self.backButtonClicked)
        self.name_issue.hide()
        self.title_issue.hide()
        self.genre_issue.hide()
        self.number_issue.hide()
    def backButtonClicked(self):
        self.close()
    def addNewBook(self):
        name = self.name.text().strip()
        title = self.title.text().strip()
        genre = self.genre.text().strip()
        number = self.number.text().strip()
        has_errors = False
        if name == '':
            self.name_issue.show()
            self.name_issue.setText("Поле пусте")
            self.name.setStyleSheet("border-radius: 10px;\n"
                                          "font: 12pt \"Arial\";\n"
                                          "border: 2px solid red;\n"
                                          "background-color: white;\n"
                                          "")
            has_errors = True
        elif any(char.isdigit() for char in str(name)):
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

        if title == '':
            self.title_issue.show()
            self.title_issue.setText("Поле пусте")
            self.title.setStyleSheet("border-radius: 10px;\n"
                                         "font: 12pt \"Arial\";\n"
                                         "border: 2px solid red;\n"
                                         "background-color: white;\n"
                                         "")
            has_errors = True
        elif any(char.isdigit() for char in str(title)):
            self.title_issue.show()
            self.title_issue.setText("Введені цифри")
            self.title.setStyleSheet("border-radius: 10px;\n"
                                         "font: 12pt \"Arial\";\n"
                                         "border: 2px solid red;\n"
                                         "background-color: white;\n"
                                         "")
            has_errors = True
        else:
            self.title_issue.hide()
            self.title.setStyleSheet("border-radius: 10px;\n"
                                         "font: 12pt \"Arial\";\n"
                                         "border: 2px solid rgb(164, 201, 255);\n"
                                         "background-color: white;\n"
                                         "")

        if genre == '':
            self.genre_issue.show()
            self.genre_issue.setText("Поле пусте")
            self.genre.setStyleSheet("border-radius: 10px;\n"
                                          "font: 12pt \"Arial\";\n"
                                          "border: 2px solid red;\n"
                                          "background-color: white;\n"
                                          "")
            has_errors = True
        elif any(char.isdigit() for char in str(genre)):
            self.genre_issue.show()
            self.genre_issue.setText("Введені цифри")
            self.genre.setStyleSheet("border-radius: 10px;\n"
                                          "font: 12pt \"Arial\";\n"
                                          "border: 2px solid red;\n"
                                          "background-color: white;\n"
                                          "")
            has_errors = True
        else:
            self.genre_issue.hide()
            self.genre.setStyleSheet("border-radius: 10px;\n"
                                          "font: 12pt \"Arial\";\n"
                                          "border: 2px solid rgb(164, 201, 255);\n"
                                          "background-color: white;\n"
                                          "")

        if number == '':
            self.number_issue.show()
            self.number_issue.setText("Поле пусте")
            self.number.setStyleSheet("border-radius: 10px;\n"
                                          "font: 12pt \"Arial\";\n"
                                          "border: 2px solid red;\n"
                                          "background-color: white;\n"
                                          "")
            has_errors = True
        elif any(char.isalpha() for char in str(number)):
            self.number_issue.show()
            self.number_issue.setText("Введені букви")
            self.number.setStyleSheet("border-radius: 10px;\n"
                                          "font: 12pt \"Arial\";\n"
                                          "border: 2px solid red;\n"
                                          "background-color: white;\n"
                                          "")
            has_errors = True
        else:
            self.number_issue.hide()
            self.number.setStyleSheet("border-radius: 10px;\n"
                                          "font: 12pt \"Arial\";\n"
                                          "border: 2px solid rgb(164, 201, 255);\n"
                                          "background-color: white;\n"
                                          "")
        if has_errors:
            self.update()
        else:
            addBook = addNewBook(name, title, genre, int(self.number.text()))
            if addBook:
                self.close()
            else:
                msg_box = QtWidgets.QMessageBox()
                msg_box.setText("Книгу не додано")
                msg_box.setWindowTitle("Інфо")
                msg_box.exec()