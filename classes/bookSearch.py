from PyQt6 import QtWidgets, QtCore
from design.booksearch_design import Ui_Booksearch
from database import getUniqueGenres, searchByGenre, searchByTitle, searchByAuthor
class Booksearch(QtWidgets.QWidget, QtCore.QObject, Ui_Booksearch):
    visitors_clicked = QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Library App")
        self.setFixedSize(1110, 720)
        self.visitors_button.clicked.connect(self.visitorsClicked)
        self.books_button.setCheckable(True)
        self.books_button.setChecked(True)
        self.title_radio.setChecked(True)
        genres = getUniqueGenres()
        self.genre_combo.addItems(genres)
        self.genre_combo.currentIndexChanged.connect(self.genreSearch)
        self.search_button.clicked.connect(self.searchButtonClicked)
        self.add_book_button.clicked.connect(self.addBookClicked)
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key.Key_Enter or event.key() == QtCore.Qt.Key.Key_Return:
            self.searchButtonClicked()
    def addBookClicked(self):
        from classes.addNewBook import AddNewBook
        self.addBook = AddNewBook()
        self.addBook.show()
    def genreSearch(self):
        self.scrollAreaWidgetContents.deleteLater()
        selected_genre = self.genre_combo.currentText()
        books = searchByGenre(self.genre_combo.currentText())
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
    def searchButtonClicked(self):
        if self.author_radio.isChecked():
            self.searchByAuthor()
        elif self.title_radio.isChecked():
            self.searchByTitle()
    def visitorsClicked(self):
        self.visitors_clicked.emit()
    def giveBookClicked(self, book_id):
        from classes.giveBook import GiveBook
        self.givebook = GiveBook(book_id)
        self.givebook.show()
    def searchByTitle(self):
        self.scrollAreaWidgetContents.deleteLater()
        self.title = self.search_input.text()
        books = searchByTitle(self.title)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 929, 499))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.labels_layout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        if books:
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
        else:
            label_text = QtWidgets.QLabel(f"Таку книгу не знайдено")
            label_text.setStyleSheet("background-color: red;"
                                         "border-radius: 10px;"
                                         "padding: 0px;"
                                         "font: 14pt \"Arial\";")
            label_text.setFixedHeight(40)
            label_text.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.labels_layout.addWidget(label_text)
            self.labels_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
    def searchByAuthor(self):
        self.scrollAreaWidgetContents.deleteLater()
        self.author = self.search_input.text()
        books = searchByAuthor(self.author)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 929, 499))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.labels_layout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        if books:
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
        else:
            label_text = QtWidgets.QLabel(f"Таку книгу не знайдено")
            label_text.setStyleSheet("background-color: red;"
                                         "border-radius: 10px;"
                                         "padding: 0px;"
                                         "font: 14pt \"Arial\";")
            label_text.setFixedHeight(40)
            label_text.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.labels_layout.addWidget(label_text)
            self.labels_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)