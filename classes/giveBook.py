from PyQt6 import QtWidgets, QtCore
from design.giveBook_design import Ui_giveBook
from database import searchVisitorById, giveBookToVisitor

class GiveBook(QtWidgets.QWidget, QtCore.QObject, Ui_giveBook):
    def __init__(self, book_id):
        super().__init__()
        self.setupUi(self)
        self.search_button.clicked.connect(self.searchVisitor)
        self.book_id = book_id[0]
        self.give_button.clicked.connect(self.giveBook)
        self.backgroundLayout = QtWidgets.QVBoxLayout(self.background)
        self.text_label = QtWidgets.QLabel()
        self.id_issue.hide()


        self.text_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.backgroundLayout.addWidget(self.text_label)
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key.Key_Enter or event.key() == QtCore.Qt.Key.Key_Return:
            self.searchVisitor()
    def searchVisitor(self):
            visitor = searchVisitorById(self.id_field.text())
            id = self.id_field.text().strip()
            has_errors = False

            if id == '':
                self.id_issue.show()
                self.id_issue.setText("Поле пусте")
                self.id_field.setStyleSheet("border-radius: 10px;\n"
                                        "font: 12pt \"Arial\";\n"
                                        "border: 2px solid red;\n"
                                        "background-color: white;\n"
                                        "")
                has_errors = True

            elif any(char.isalpha() for char in str(id)):
                self.id_issue.show()
                self.id_issue.setText("Введіть цифри")
                self.id_field.setStyleSheet("border-radius: 10px;\n"
                                             "font: 12pt \"Arial\";\n"
                                             "border: 2px solid red;\n"
                                             "background-color: white;\n"
                                             "")
                has_errors = True
            else:
                self.id_issue.hide()
                self.id_field.setStyleSheet("border-radius: 10px;\n"
                                        "font: 12pt \"Arial\";\n"
                                        "border: 2px solid rgb(164, 201, 255);\n"
                                        "background-color: white;\n"
                                        "")

            if has_errors:
                self.update()
            else:
                if visitor:
                    visitor_id, visitor_name, date, books_id = visitor[0:]
                    if books_id != None and books_id != 0:
                        self.text_label.setText(f"Читатьський квиток №: {visitor_id}\n"
                                               f"\n"
                                               f"Ім'я: {visitor_name}\n"
                                               f"\n"
                                               f"Дата реєстрації: {date}\n"
                                                f"\n"
                                                f"Книжок на руках: {len(str(books_id).split(','))}")
                        self.text_label.setStyleSheet("background-color: rgb(164, 201, 255);"
                                                      "border-radius: 10px;"
                                                      "padding: 3px;"
                                                      "font: 14pt \"Arial\";")
                    else:
                        self.text_label.setText(f"Читатьський квиток №: {visitor_id}\n"
                                                f"\n"
                                                f"Ім'я: {visitor_name}\n"
                                                f"\n"
                                                f"Дата реєстрації: {date}\n"
                                                f"\n"
                                                f"Книжок на руках: 0")
                        self.text_label.setStyleSheet("background-color: rgb(164, 201, 255);"
                                                      "border-radius: 10px;"
                                                      "padding: 3px;"
                                                      "font: 14pt \"Arial\";")
                else:
                    self.text_label.setText("Читача не знайдено")
                    self.text_label.setStyleSheet("background-color: rgb(164, 201, 255);"
                                                  "border-radius: 10px;"
                                                  "padding: 3px;"
                                                  "font: 14pt \"Arial\";")


                self.backgroundLayout.update()



    def giveBook(self):
        visitor = searchVisitorById(self.id_field.text())
        if visitor:
            bookGived = giveBookToVisitor(self.id_field.text(), self.book_id)
            if bookGived:
                self.text_label.setText("Книгу видано")
                self.text_label.setStyleSheet("background-color: rgb(164, 201, 255);"
                                              "border-radius: 10px;"
                                              "padding: 3px;"
                                              "font: 14pt \"Arial\";")
                self.backgroundLayout.update()
            else:
                self.text_label.setText("Книгу не видано")
                self.text_label.setStyleSheet("background-color: rgb(164, 201, 255);"
                                              "border-radius: 10px;"
                                              "padding: 3px;"
                                              "font: 14pt \"Arial\";")
                self.backgroundLayout.update()
        else:
            self.text_label.setText("Читача не знайдено")
            self.text_label.setStyleSheet("background-color: rgb(164, 201, 255);"
                                          "border-radius: 10px;"
                                          "padding: 3px;"
                                          "font: 14pt \"Arial\";")
            self.backgroundLayout.update()
