from functools import partial

from login_design import Ui_Login
from booksearch_design import Ui_Booksearch
from visitors_design import Ui_Visitorssearch
from new_visitor_design import Ui_NewVisitor
from giveBook_design import Ui_giveBook
from new_book_design import Ui_NewBook

from database import (search_by_author, search_by_id, search_worker, search_by_title, get_unique_genres, search_by_genre,
                      search_visitor, give_book_to_visitor, remove_book_from_visitor, searchVisitorById, addVisitor, returnBook,
                      addNewBook)

import sys
from PyQt6 import QtWidgets, QtCore, QtGui

class LoginWindow(QtWidgets.QMainWindow, QtCore.QObject, Ui_Login):

    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.pushButton.clicked.connect(self.buttonClicked)


    def buttonClicked(self):
        login = self.login_input.text()
        password = self.password_input.text()
        worker = search_worker(login, password)

        if worker:
            booksearch = Booksearch()
            widget.addWidget(booksearch)


            widget.setMinimumWidth(1107)
            widget.setMinimumHeight(719)

            screen_width = QtGui.QGuiApplication.primaryScreen().geometry().width()
            screen_height = QtGui.QGuiApplication.primaryScreen().geometry().height()
            widget_width = widget.width()
            widget_height = widget.height()

            widget.move(int((screen_width - widget_width) / 2), int((screen_height - widget_height) / 2))
            widget.setCurrentIndex(widget.currentIndex() + 1)

        else: print('Invalid login or password')

class Booksearch(QtWidgets.QMainWindow, QtCore.QObject, Ui_Booksearch):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.visitors_button.clicked.connect(self.visitorsClicked)
        self.books_button.setCheckable(True)
        self.books_button.setChecked(True)
        self.title_radio.setChecked(True)
        genres = get_unique_genres()
        self.genre_combo.addItems(genres)
        self.genre_combo.currentIndexChanged.connect(self.genre_search)
        self.search_button.clicked.connect(self.search_button_clicked)
        self.add_book_button.clicked.connect(self.addBookClicked)

    def addBookClicked(self):
        self.addBook = AddNewBook()
        self.addBook.show()

    def genre_search(self):
        self.scrollAreaWidgetContents.deleteLater()

        selected_genre = self.genre_combo.currentText()
        books = search_by_genre(self.genre_combo.currentText())


        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 929, 499))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.labels_layout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)

        for i in books:
            book_id, author, title, genre, available = i[0:]

            self.label = QtWidgets.QLabel()
            self.label.setStyleSheet("background-color: rgb(164, 201, 255);"
                                     "border-radius: 10px;"
                                     "padding: 0px;"
                                     "font: 14pt \"Arial\";")
            self.label.setFixedHeight(60)
            self.label.setFixedWidth(self.scrollArea.width() - 40)

            self.label_layout = QtWidgets.QHBoxLayout(self.label)

            label_text = QtWidgets.QLabel(f"Автор: {author}| Назва: {title}| Жанр: {genre}|\n Наявність: {available}")
            self.label_layout.addWidget(label_text)

            self.give_book = QtWidgets.QPushButton(f"Видати")
            self.give_book.setGeometry(QtCore.QRect(750, 70, 111, 41))
            self.give_book.setStyleSheet("border-radius: 10px;\n"
                                         "border-color: rgb(0, 0, 0);\n"
                                         "\n"
                                         "background-color: rgb(255, 242, 239);\n"
                                         "font: 14pt \"Arial\";\n"
                                         "")
            self.give_book.setFixedHeight(40)
            self.give_book.setFixedWidth(150)
            self.give_book.clicked.connect(lambda _, book_id=i: self.giveBookClicked(book_id))
            self.label_layout.addWidget(self.give_book)
            self.labels_layout.addWidget(self.label)
            self.labels_layout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetFixedSize)
    def search_button_clicked(self):
        if self.author_radio.isChecked():
            self.search_by_author()
        elif self.title_radio.isChecked():
            self.search_by_title()

    def visitorsClicked(self):
        visitorsWindow = VisitorsSearch()
        widget.addWidget(visitorsWindow)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        VisitorsSearch().searchButtonClicked()

    def giveBookClicked(self, book_id):
        self.givebook = GiveBook(book_id)
        self.givebook.show()

    def click(self):
        self.layout()
        self.search_by_author()

    def search_by_title(self):
        self.scrollAreaWidgetContents.deleteLater()
        self.title = self.search_input.text()
        books = search_by_title(self.title)

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 929, 499))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.labels_layout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)

        for i in books:
            book_id, author, title, genre, available = i[0:]

            self.label = QtWidgets.QLabel()
            self.label.setStyleSheet("background-color: rgb(164, 201, 255);"
                                     "border-radius: 10px;"
                                     "padding: 0px;"
                                     "font: 14pt \"Arial\";")
            self.label.setFixedHeight(60)
            self.label.setFixedWidth(self.scrollArea.width() - 40)

            self.label_layout = QtWidgets.QHBoxLayout(self.label)

            label_text = QtWidgets.QLabel(f"Автор: {author}| Назва: {title}| Жанр: {genre}|\n Наявність: {available}")
            self.label_layout.addWidget(label_text)

            self.give_book = QtWidgets.QPushButton(f"Видати")
            self.give_book.setGeometry(QtCore.QRect(750, 70, 111, 41))
            self.give_book.setStyleSheet("border-radius: 10px;\n"
                                         "border-color: rgb(0, 0, 0);\n"
                                         "\n"
                                         "background-color: rgb(255, 242, 239);\n"
                                         "font: 14pt \"Arial\";\n"
                                         "")
            self.give_book.setFixedHeight(40)
            self.give_book.setFixedWidth(150)
            self.give_book.clicked.connect(lambda _, book_id=i: self.giveBookClicked(book_id))
            self.label_layout.addWidget(self.give_book)
            self.labels_layout.addWidget(self.label)
            self.labels_layout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetFixedSize)

    def search_by_author(self):
        self.scrollAreaWidgetContents.deleteLater()
        self.author = self.search_input.text()
        books = search_by_author(self.author)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 929, 499))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.labels_layout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)



        for i in books:
            book_id, author, title, genre, available = i[0:]

            self.label = QtWidgets.QLabel()
            self.label.setStyleSheet("background-color: rgb(164, 201, 255);"
                                "border-radius: 10px;"
                                "padding: 0px;"
                                "font: 14pt \"Arial\";")
            self.label.setFixedHeight(60)
            self.label.setFixedWidth(self.scrollArea.width()-40)

            self.label_layout = QtWidgets.QHBoxLayout(self.label)

            label_text = QtWidgets.QLabel(f"Автор: {author}| Назва: {title}| Жанр: {genre}|\n Наявність: {available}")
            self.label_layout.addWidget(label_text)

            self.give_book = QtWidgets.QPushButton(f"Видати")
            self.give_book.setGeometry(QtCore.QRect(750, 70, 111, 41))
            self.give_book.setStyleSheet("border-radius: 10px;\n"
                                         "border-color: rgb(0, 0, 0);\n"
                                         "\n"
                                         "background-color: rgb(255, 242, 239);\n"
                                         "font: 14pt \"Arial\";\n"
                                         "")
            self.give_book.setFixedHeight(40)
            self.give_book.setFixedWidth(150)
            self.give_book.clicked.connect(lambda _, book_id=i: self.giveBookClicked(book_id))
            self.label_layout.addWidget(self.give_book)
            self.labels_layout.addWidget(self.label)
            self.labels_layout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetFixedSize)

class AddNewBook(QtWidgets.QWidget, QtCore.QObject, Ui_NewBook):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.register_button.clicked.connect(self.addNewBook)

    def addNewBook(self):
        name = self.name.text()
        title = self.title.text()
        genre = self.genre.text()
        number = int(self.number.text())
        addBook = addNewBook(name, title, genre, number)
        if addBook:
            self.close()

class GiveBook(QtWidgets.QWidget, QtCore.QObject, Ui_giveBook):
    def __init__(self, book_id):
        super().__init__()
        self.setupUi(self)
        self.search_button.clicked.connect(self.searchVisitor)
        self.book_id = book_id[0]
        self.give_button.clicked.connect(self.giveBook)
        self.backgroundLayout = QtWidgets.QVBoxLayout(self.background)
        self.text_label = QtWidgets.QLabel()


        self.text_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.backgroundLayout.addWidget(self.text_label)

    def searchVisitor(self):
            visitor = searchVisitorById(self.id_field.text())


            if visitor:
                visitor_id, visitor_name, date, books_id = visitor[0:]
                self.text_label.setText(f"Читатьський квиток №: {visitor_id}\n"
                                       f"\n"
                                       f"Имя: {visitor_name}\n"
                                       f"\n"
                                       f"Дата регистрации: {date}")
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
            bookGived = give_book_to_visitor(self.id_field.text(), self.book_id)
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

class VisitorsSearch(QtWidgets.QMainWindow, QtCore.QObject, Ui_Visitorssearch):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.books_button.clicked.connect(self.booksClicked)
        self.register_button.clicked.connect(self.registerClicked)
        self.search_button.clicked.connect(self.searchButtonClicked)
        # self.searchButtonClicked()
        widget.currentChanged.connect(self.searchButtonClicked)

        # self.scrollAreaWidgetContents.deleteLater()
        # self.scrollAreaWidgetContents = QtWidgets.QWidget()
        # self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 929, 499))
        # self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        # self.scrollArea.setWidget(self.scrollAreaWidgetContents)

    def registerClicked(self):
        self.newVisitor = NewVisitor()
        self.newVisitor.show()

    def booksClicked(self):
        booksWindow = Booksearch()
        widget.addWidget(booksWindow)
        widget.setCurrentIndex(widget.currentIndex() - 1)

    def labelClicked(self, visitor):
        visitor_id, visitor_name, date, books_id = visitor[0:]
        if books_id != None and books_id !=0:
            self.scrollAreaWidgetContents.deleteLater()
            self.scrollAreaWidgetContents = QtWidgets.QWidget()
            self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 929, 499))
            self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
            self.scrollArea.setWidget(self.scrollAreaWidgetContents)

            self.labels_layout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
            books_layout = QtWidgets.QVBoxLayout()

            label_text = QtWidgets.QLabel(
                    f"Номер квитка: {visitor_id}|"
                    f" Ім'я: {visitor_name}| Дата реєстрації: {date}| Кількість книжок на руках: {len(str(books_id).split(','))}|"
                    f"")
            label_text.setStyleSheet("background-color: rgb(164, 201, 255);"
                                         "border-radius: 10px;"
                                         "padding: 3px;"
                                         "font: 14pt \"Arial\";")
            label_text.setFixedHeight(60)
            label_text.setFixedWidth(self.scrollArea.width() - 40)

            self.labels_layout.addWidget(label_text)
            books_id_split = str(books_id).split(',')
            for book_id in books_id_split:
                book = search_by_id(book_id)
                for book_tuple in book:
                    book_id, author, title, genre, available = book_tuple

                    self.label = QtWidgets.QLabel()
                    self.label.setStyleSheet("background-color: rgb(233, 243, 255);"
                                                      "border-radius: 10px;"
                                                      "padding: 3px;"
                                                      "font: 14pt \"Arial\";")
                    self.label.setFixedHeight(60)
                    self.label.setFixedWidth(self.scrollArea.width() - 40)

                    self.label_layout = QtWidgets.QHBoxLayout(self.label)

                    label_text_book = QtWidgets.QLabel(
                            f"Книга: {title} | Автор: {author} | Жанр: {genre}")
                    self.label_layout.addWidget(label_text_book)
                    self.give_book = QtWidgets.QPushButton(f"Здати")
                    self.give_book.setGeometry(QtCore.QRect(750, 70, 111, 41))
                    self.give_book.setStyleSheet("border-radius: 10px;\n"
                                                 "border-color: rgb(0, 0, 0);\n"
                                                 "\n"
                                                 "background-color: rgb(255, 242, 239);\n"
                                                 "font: 14pt \"Arial\";\n"
                                                 "")
                    self.give_book.setFixedHeight(40)
                    self.give_book.setFixedWidth(150)
                    self.give_book.clicked.connect(partial(self.returnBookClicked, visitor_id=visitor_id, book_id=book_id, visitor = visitor))
                    self.label_layout.addWidget(self.give_book)
                    books_layout.addWidget(self.label)


            self.labels_layout.addLayout(books_layout)
            self.labels_layout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetFixedSize)
        else: None

    def returnBookClicked(self, visitor_id, book_id, visitor):
        returnBook(visitor_id, book_id)
        self.searchButtonClicked()



    def searchButtonClicked(self):
        print('click')
        self.scrollAreaWidgetContents.deleteLater()
        visitor = search_visitor(self.name.text())
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 929, 499))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.labels_layout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)

        for i in visitor:
            visitor_id, visitor_name, date, books_id = i[0:]
            if books_id != None and books_id != 0:
                self.label_text = QtWidgets.QLabel(
                        f"Номер квитка: {visitor_id} |"
                        f"Ім'я: {visitor_name}| Дата реєстрації: {date}| Кількість книжок на руках: {len(str(books_id).split(','))}|"
                        f"")
                self.label_text.setStyleSheet("background-color: rgb(164, 201, 255);"
                                         "border-radius: 10px;"
                                         "padding: 3px;"
                                         "font: 14pt \"Arial\";")
                self.label_text.setFixedHeight(60)
                self.label_text.setFixedWidth(self.scrollArea.width() - 40)
            else:
                self.label_text = QtWidgets.QLabel(
                    f"Номер квитка: {visitor_id} |"
                    f"Ім'я: {visitor_name} | Дата реєстрації: {date}| Кількість книжок на руках: 0|")
                self.label_text.setStyleSheet("background-color: rgb(164, 201, 255);"
                                             "border-radius: 10px;"
                                             "padding: 3px;"
                                             "font: 14pt \"Arial\";")
                self.label_text.setFixedHeight(60)
                self.label_text.setFixedWidth(self.scrollArea.width() - 40)

            self.label_text.mousePressEvent = lambda event, visitor = i: self.labelClicked(visitor)
            self.labels_layout.addWidget(self.label_text)
            self.labels_layout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetFixedSize)

class NewVisitor(QtWidgets.QWidget, QtCore.QObject, Ui_NewVisitor):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.back_button.clicked.connect(self.backClicked)
        self.register_button.clicked.connect(self.registerClicked)

    def backClicked(self):
        self.close()

    def registerClicked(self):
        addVisitor(self.secondName.text(), self.firstName.text(), self.dateEdit.text())
        VisitorsSearch().searchButtonClicked()
        self.close()


app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()

loginWindow = LoginWindow()

widget.setFixedWidth(380)
widget.setFixedHeight(600)

screen_width = QtGui.QGuiApplication.primaryScreen().geometry().width()
screen_height = QtGui.QGuiApplication.primaryScreen().geometry().height()
widget_width = widget.width()
widget_height = widget.height()


widget.move(int((screen_width-widget_width)/2), int((screen_height-widget_height)/2))


widget.addWidget(loginWindow)
widget.show()

app.exec()
