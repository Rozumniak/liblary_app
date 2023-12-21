from classes.loginWindow import LoginWindow
from classes.bookSearch import Booksearch
from classes.visitors import VisitorsSearch
from PyQt6 import QtWidgets, QtGui
import os
class MainApplication(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Library App")
        self.setStyleSheet("background-color: rgb(255, 255, 240);")
        self.setFixedSize(380, 600)
        self.login_window = LoginWindow()
        self.book_search = Booksearch()
        self.visitors = VisitorsSearch()
        self.login_window.login_successful.connect(self.show_book_search)
        self.book_search.visitors_clicked.connect(self.show_visitor_search)
        self.visitors.books_clicked.connect(self.show_book_search)
        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.addWidget(self.login_window)
        self.book_search.hide()
        self.visitors.hide()
    def show_book_search(self):
        self.book_search.show()
        self.visitors.close()
        self.close()
    def show_visitor_search(self):
        self.visitors.show()
        self.book_search.close()
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(os.path.join(os.path.dirname(__file__), "logo.ico")))
    main_app = MainApplication()
    screen_width = QtGui.QGuiApplication.primaryScreen().geometry().width()
    screen_height = QtGui.QGuiApplication.primaryScreen().geometry().height()
    widget_width = main_app.width()
    widget_height = main_app.height()
    main_app.move(int((screen_width - widget_width) / 2), int((screen_height - widget_height) / 2))
    main_app.show()
    sys.exit(app.exec())