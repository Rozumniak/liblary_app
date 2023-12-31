from PyQt6 import QtCore, QtGui, QtWidgets
import os
class Ui_Booksearch(object):
    def setupUi(self, Booksearch):
        Booksearch.setObjectName("Booksearch")
        Booksearch.resize(1110, 720)
        Booksearch.setStyleSheet("background-color: rgb(255, 255, 240);")
        self.books_button = QtWidgets.QPushButton(parent=Booksearch)
        self.books_button.setGeometry(QtCore.QRect(1010, 20, 95, 90))
        self.books_button.setStyleSheet("border-radius: 10px;\n"
"border: 2px solid rgb(127, 165, 206);\n"
"background-color: rgb(233, 243, 255);\n"
"font: 12pt \"Arial\";\n"
"padding 5px;\n"
"")
        self.books_button.setObjectName("books_button")
        self.layoutWidget = QtWidgets.QWidget(parent=Booksearch)
        self.layoutWidget.setGeometry(QtCore.QRect(210, 111, 481, 88))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_3.setStyleSheet("font: 14pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.title_radio = QtWidgets.QRadioButton(parent=self.layoutWidget)
        self.title_radio.setStyleSheet("font: 14pt \"Arial\";")
        self.title_radio.setObjectName("title_radio")
        self.gridLayout.addWidget(self.title_radio, 1, 0, 1, 1)
        self.genre_combo = QtWidgets.QComboBox(parent=self.layoutWidget)
        self.genre_combo.setStyleSheet("border-radius: 10px;\n"
"font: 14pt \"Arial\";\n"
"border: 2px solid rgb(164, 201, 255);\n"
"background-color: white;")
        self.genre_combo.setObjectName("genre_combo")
        self.gridLayout.addWidget(self.genre_combo, 1, 1, 2, 1)
        self.author_radio = QtWidgets.QRadioButton(parent=self.layoutWidget)
        self.author_radio.setStyleSheet("font: 14pt \"Arial\";")
        self.author_radio.setObjectName("author_radio")
        self.gridLayout.addWidget(self.author_radio, 2, 0, 1, 1)
        self.search_input = QtWidgets.QLineEdit(parent=Booksearch)
        self.search_input.setGeometry(QtCore.QRect(190, 40, 510, 35))
        self.search_input.setStyleSheet("border-radius: 10px;\n"
"font: 14pt \"Arial\";\n"
"border: 2px solid rgb(164, 201, 255);\n"
"background-color: white;\n"
"")
        self.search_input.setObjectName("search_input")
        self.search_button = QtWidgets.QPushButton(parent=Booksearch)
        self.search_button.setGeometry(QtCore.QRect(720, 36, 75, 35))
        self.search_button.setStyleSheet("border-radius: 10px;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(164, 201, 255);\n"
"font: 13pt \"Arial\";\n"
"")
        self.search_button.setObjectName("search_button")
        self.add_book_button = QtWidgets.QPushButton(parent=Booksearch)
        self.add_book_button.setGeometry(QtCore.QRect(850, 36, 110, 35))
        self.add_book_button.setStyleSheet("border-radius: 10px;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(164, 201, 255);\n"
"font: 13pt \"Arial\";\n"
"")
        self.add_book_button.setObjectName("add_book_button")
        self.label_4 = QtWidgets.QLabel(parent=Booksearch)
        self.label_4.setGeometry(QtCore.QRect(390, 81, 120, 21))
        self.label_4.setStyleSheet("font: 14pt \"Arial\";")
        self.label_4.setObjectName("label_4")
        self.scrollArea = QtWidgets.QScrollArea(parent=Booksearch)
        self.scrollArea.setGeometry(QtCore.QRect(70, 211, 931, 501))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 929, 499))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.visitors_button = QtWidgets.QPushButton(parent=Booksearch)
        self.visitors_button.setGeometry(QtCore.QRect(1010, 113, 95, 90))
        self.visitors_button.setStyleSheet("border-radius: 10px;\n"
"border: 2px solid rgb(127, 165, 206);\n"
"background-color: rgb(164, 201, 255);\n"
"font: 13pt \"Arial\";\n"
"padding 5px;\n"
"")
        self.visitors_button.setObjectName("visitors_button")
        self.label = QtWidgets.QLabel(parent=Booksearch)
        self.label.setGeometry(QtCore.QRect(30, 30, 120, 120))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(os.path.join(os.path.dirname(__file__), "logo.png")))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.retranslateUi(Booksearch)
        QtCore.QMetaObject.connectSlotsByName(Booksearch)
    def retranslateUi(self, Booksearch):
        _translate = QtCore.QCoreApplication.translate
        Booksearch.setWindowTitle(_translate("Booksearch", "Form"))
        self.books_button.setText(_translate("Booksearch", "Книги"))
        self.label_3.setText(_translate("Booksearch", "Жанри"))
        self.title_radio.setText(_translate("Booksearch", "Назва"))
        self.author_radio.setText(_translate("Booksearch", "Автор"))
        self.search_input.setPlaceholderText(_translate("Booksearch", "Спочатку оберіть критерій пошуку"))
        self.search_button.setText(_translate("Booksearch", "Пошук"))
        self.add_book_button.setText(_translate("Booksearch", "Додати книгу"))
        self.label_4.setText(_translate("Booksearch", "Шукати по:"))
        self.visitors_button.setText(_translate("Booksearch", "Відвідувачі"))
