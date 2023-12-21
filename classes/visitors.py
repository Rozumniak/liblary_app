from functools import partial
from PyQt6 import QtWidgets, QtCore
from design.visitors_design import Ui_Visitorssearch
from database import searchById, returnBook, searchVisitor
class VisitorsSearch(QtWidgets.QMainWindow, QtCore.QObject, Ui_Visitorssearch):
    books_clicked = QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Library App")
        self.setFixedSize(1110, 720)
        self.books_button.clicked.connect(self.booksClicked)
        self.register_button.clicked.connect(self.newUserRegisterClicked)
        self.search_button.clicked.connect(self.searchButtonClicked)
        self.name_issue.hide()
    def showEvent(self, event):
        self.searchButtonClicked()
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key.Key_Enter or event.key() == QtCore.Qt.Key.Key_Return:
            self.searchButtonClicked()
    def newUserRegisterClicked(self):
        from classes.newVisitor import NewVisitor
        self.newVisitor = NewVisitor()
        self.newVisitor.show()
    def booksClicked(self):
        self.books_clicked.emit()
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
                book = searchById(book_id)
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
        self.scrollAreaWidgetContents.deleteLater()
        visitor = searchVisitor(self.name.text())
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 929, 499))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.labels_layout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        name = self.name.text().strip()
        has_errors = False
        if any(char.isdigit() for char in str(name)):
            self.name_issue.show()
            self.name_issue.setText("Поле приймає тільки букви")
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
        if has_errors:
            self.update()
        else:
            if visitor:
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
            else:
                label_text = QtWidgets.QLabel(f"Такого читача не знайдено")
                label_text.setStyleSheet("background-color: red;"
                                         "border-radius: 10px;"
                                         "padding: 0px;"
                                         "font: 14pt \"Arial\";")
                label_text.setFixedHeight(40)
                label_text.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.labels_layout.addWidget(label_text)
                self.labels_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)