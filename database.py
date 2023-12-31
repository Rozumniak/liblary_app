import sqlite3
connection_library = sqlite3.connect('library.db')
cursor = connection_library.cursor()
# cursor.execute('''DROP TABLE books''')
cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    author TEXT NOT NULL,
                    book_title TEXT NOT NULL,
                    genre TEXT NOT NULL,
                    available INTEGER)''')
# books_list = [
#     ('Тарас Шевченко', 'Кобзар', 'Поезія', 5),
#     ('Тарас Шевченко', 'Гайдамаки', 'Історична література', 8),
#     ('Тарас Шевченко', 'Заповіт', 'Політична література', 3),
#     #Леся Українка
#     ('Леся Українка', 'Лірика', 'Поезія', 3),
#     ('Леся Українка', 'Сонети', 'Поезія', 6),
#     ('Леся Українка', 'Відлуння', 'Поезія', 2),
#     # Іван Франко
#     ('Іван Франко', 'Зібрані твори у 50-ти томах', 'Збірка', 3),
#     ('Іван Франко', 'Лірика Івана Франка', 'Поезія', 2),
#     ('Іван Франко', 'Записки смертника', 'Філософська проза', 4),
#     # Михайло Коцюбинський
#     ('Михайло Коцюбинський', 'Intermezzo', 'Роман', 3),
#     ('Михайло Коцюбинський', 'Дорогою ціною', 'Роман', 4),
#     ('Михайло Коцюбинський', 'На крилах пісень', 'Роман', 1),
#     # Остап Вишня
#     ('Остап Вишня', 'Зібрані твори', 'Гумореска', 7),
#     ('Остап Вишня', 'Анекдоти', 'Гумореска', 4),
#     ('Остап Вишня', 'Веселий Львів', 'Гумореска', 3),
#     # Василь Стефаник
#     ('Василь Стефаник', 'На порозі', 'Психологічна проза', 6),
#     ('Василь Стефаник', 'Камінний хрест', 'Психологічна проза', 4),
#     ('Василь Стефаник', 'Сльози матері', 'Психологічна проза', 3),
#     # Панас Мирний
#     ('Панас Мирний', 'Новели', 'Новелa', 6),
#     ('Панас Мирний', 'Злагода', 'Новелa', 4),
#     ('Панас Мирний', 'Без кайданів', 'Новелa', 2),
#     # Ліна Костенко
#     ('Ліна Костенко', 'Записки української фронтовички', 'Поезія', 3),
#     ('Ліна Костенко', 'Земля в огні', 'Поезія', 2),
#     ('Ліна Костенко', 'Дорога моїх сновидінь', 'Поезія', 1),
#     # Юрій Андрухович
#     ('Юрій Андрухович', 'Пerverzion', 'Сучасна проза', 4),
#     ('Юрій Андрухович', 'Рекреації', 'Сучасна проза', 5),
#     ('Юрій Андрухович', 'Лексикон інтимних міст', 'Сучасна проза', 3),
#     # Сергій Жадан
#     ('Сергій Жадан', 'Ворошиловград', 'Поезія', 4),
#     ('Сергій Жадан', 'Месопотамія', 'Поезія', 5),
#     ('Сергій Жадан', 'Поезія', 'Поезія', 2),
#     # Олесь Гончар
#     ('Олесь Гончар', 'Картина світу', 'Роман', 2),
#     ('Олесь Гончар', 'Собор', 'Роман', 7),
#     ('Олесь Гончар', 'Безодня', 'Роман', 5),
#     # Юрій Іздрик
#     ('Юрій Іздрик', 'Місто', 'Проза', 3),
#     ('Юрій Іздрик', 'Країна мрій', 'Проза', 4),
#     ('Юрій Іздрик', 'Різдвяні історії', 'Проза', 4),
#     # Василь Симоненко
#     ('Василь Симоненко', 'Вибрані твори', 'Поезія', 3),
#     ('Василь Симоненко', 'Вечірній світ', 'Поезія', 3),
#     ('Василь Симоненко', 'Слово про батьківщину', 'Поезія', 3),
#     # Олександр Олесь
#     ('Олександр Олесь', 'Княгиня Ольга', 'Лірична драма', 3),
#     ('Олександр Олесь', 'Лірика Олександра Олеся', 'Лірична драма', 3),
#     ('Олександр Олесь', 'Серце Вкраїни', 'Лірична драма', 4),
#     # Павло Загребельний
#     ('Павло Загребельний', 'Соняшний промінь', 'Лірика', 2),
#     ('Павло Загребельний', 'Голоси душі', 'Лірика', 4),
#     ('Павло Загребельний', 'Листи до друзів', 'Лірика', 2),
#     # Леонід Первомайський
#     ('Леонід Первомайський', 'Весняні зірки', 'Поезія', 5),
#     ('Леонід Первомайський', 'Слово і діло', 'Поезія', 4),
#     ('Леонід Первомайський', 'Пісні Л.Первомайський', 'Поезія', 3),
#     # Василь Шкляр
#     ('Василь Шкляр', 'Лірики В.Шкляра', 'Лірика', 4),
#     ('Василь Шкляр', 'Вірші В.Шкляр', 'Лірика', 3),
#     ('Василь Шкляр', 'Вечірні спогади', 'Лірика', 1),
#     # Олександр Копиленко
#     ('Олександр Копиленко', 'Звуки і мить', 'Поезія', 6),
#     ('Олександр Копиленко', 'Вірші О.Копиленко', 'Поезія', 5),
#     ('Олександр Копиленко', 'Живе слово', 'Поезія', 5),
#     # Марко Вовчок
#     ('Марко Вовчок', 'Лірика М.Вовчок', 'Лірика', 5),
#     ('Марко Вовчок', 'Сонети', 'Лірика', 5),
#     ('Марко Вовчок', 'Зорі', 'Лірика', 7),
#     # Микола Куліш
#     ('Микола Куліш', 'Чорна рада', 'Історична література', 9),
#     ('Микола Куліш', 'На греблі"', 'Історична література', 5),
#     ('Микола Куліш', 'Семен Кожем*яка', 'Історична література', 7),
#
# ]
#
# cursor.executemany('INSERT OR IGNORE INTO books (author, book_title, genre, available) VALUES (?, ?, ?, ?)', books_list)
#
# connection_library.commit()
def searchByAuthor(author):
    author = author.capitalize()
    cursor.execute('SELECT * FROM books WHERE author LIKE ?', ('%' + author + '%',))
    books = cursor.fetchall()
    return books
def searchById(id):
    cursor.execute('SELECT * FROM books WHERE book_id = ?', (id,))
    book = cursor.fetchall()
    return book
def searchByTitle(title):
    title = title.capitalize()
    cursor.execute('SELECT * FROM books WHERE book_title LIKE ?', ('%' + title + '%',))
    books = cursor.fetchall() or False
    return books
def searchByGenre(genre):
    cursor.execute('SELECT * FROM books WHERE genre = ?', (genre,))
    books = cursor.fetchall()
    return books
def getUniqueGenres():
    cursor.execute('SELECT DISTINCT genre FROM books')
    genres = [genre[0] for genre in cursor.fetchall()]
    return genres
def addNewBook(name, title, genre, number):
    name = name.capitalize()
    title = title.capitalize()
    genre = genre.capitalize()
    cursor.execute('INSERT INTO books (author, book_title, genre, available) VALUES (?,?,?,?)', (name, title, genre, number,))
    connection_library.commit()
    return True
# cursor.execute('''DROP TABLE workers''')
cursor.execute('''CREATE TABLE IF NOT EXISTS workers (
                    worker_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    worker_name TEXT NOT NULL,
                    job_title TEXT NOT NULL,
                    login TEXT NOT NULL,
                    password TEXT NOT NULL)''')

# workers_list = [
#     ('Admin', 'Admin', 'admin', 'admin'),
#     ('Розумняк Руслан', 'Бібліотекар', 'ruslan', 'ruslan'),
#     ('test', 'test', 'test', 'test')
# ]
# cursor.executemany('INSERT OR IGNORE INTO workers (worker_name, job_title, login, password) VALUES (?, ?, ?, ?)', workers_list)
# connection_library.commit()
def searchWorker(login, password):
    login = login.lower()
    cursor.execute('SELECT * FROM workers WHERE login = ? AND password = ?',(login, password))
    worker = cursor.fetchall() or False
    return worker
def addNewWorker(name, title, login, password):
    name = name.capitalize()
    title = title.capitalize()
    login = login.lower()
    cursor.execute('INSERT INTO workers (worker_name, job_title, login, password) VALUES (?,?,?,?)',
                   (name, title, login, password,))
    connection_library.commit()
    newWorker = searchWorker(login, password)
    return newWorker
# cursor.execute('''DROP TABLE visitors''')
cursor.execute('''CREATE TABLE IF NOT EXISTS visitors (
                    visitor_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    visitor_name TEXT NOT NULL,
                    date TEXT NOT NULL,
                    books_id INTEGER NULL)''')
# visitors_list = [
#     ('Розумняк Руслан', '10.11.2022', 1,2,3),
#     ('Розумняк Антон', '10.11.2022', 0),
#     ('Розумняк Сергей', '10.11.2022', 1,2,3,4),
# ]
# cursor.executemany('INSERT OR IGNORE INTO visitors (visitor_name, date, books_id) VALUES (?, ?, ?)', visitors_list)
# connection_library.commit()
def searchVisitor(name):
    name = name.capitalize()
    cursor.execute('SELECT * FROM visitors WHERE visitor_name LIKE ?',('%' + name + '%',))
    visitor = cursor.fetchall() or False
    return visitor
def searchVisitorById(id):
    cursor.execute('SELECT * FROM visitors WHERE visitor_id = ?', (id,))
    visitor = cursor.fetchone() or False
    return visitor
def addVisitor(secondName, firstName, date):
    secondName = secondName.capitalize()
    firstName = firstName.capitalize()
    name = secondName + " " + firstName
    null_book_id = 0
    cursor.execute('INSERT INTO visitors (visitor_name, date, books_id) VALUES (?,?,?)',(name, date, null_book_id,))
    visitor = connection_library.commit() or False
    return visitor
def giveBookToVisitor(visitor_id, book_id):
    givenBook = searchById(book_id)
    if givenBook[0][4] != 0:
        cursor.execute('SELECT books_id FROM visitors WHERE visitor_id = ?', (visitor_id,))
        current_books = cursor.fetchone()
        if current_books[0] !=0:
            current_books_list = [str(current_books[0])]  # Перероблює у список одним елементом
            if str(book_id) not in current_books_list:
                current_books_list.append(str(book_id))
                updated_books = ','.join(current_books_list)
                cursor.execute('UPDATE visitors SET books_id = ? WHERE visitor_id = ?', (updated_books, visitor_id))
                connection_library.commit()
                book = searchById(book_id)
                book_count = book[0][4] - 1
                cursor.execute('UPDATE books SET available = ? WHERE book_id = ?', (book_count, book_id))
                connection_library.commit()
                print(searchById(book_id))
                return True
            else:
                return False  # Книга вже записана на юзері
        elif current_books[0] == 0:
            cursor.execute('UPDATE visitors SET books_id = ? WHERE visitor_id = ?', (book_id, visitor_id))
            connection_library.commit()
            book = searchById(book_id)
            book_count = book[0][4] - 1
            cursor.execute('UPDATE books SET available = ? WHERE book_id = ?', (book_count, book_id))
            connection_library.commit()
            print(searchById(book_id))
            return True
# Метод для поверненя книг
def returnBook(visitor_id, book_id):
    cursor.execute('SELECT books_id FROM visitors WHERE visitor_id = ?', (visitor_id,))
    current_books = cursor.fetchone()
    cursor.execute('SELECT * FROM visitors WHERE visitor_id = ?', (visitor_id,))
    current_visitor = cursor.fetchone()
    book = searchById(book_id)
    book_count = book[0][4] + 1
    cursor.execute('UPDATE books SET available = ? WHERE book_id = ?', (book_count, book_id))
    connection_library.commit()
    if current_books and current_books[0] != 0:
        current_books_list = str(current_books[0]).split(',')
        # Записуємо у БД кількість книг
        if str(book_id) in current_books_list:
            current_books_list.remove(str(book_id))
            updated_books = ','.join(current_books_list)
            cursor.execute('UPDATE visitors SET books_id = ? WHERE visitor_id = ?', (updated_books, visitor_id))
            connection_library.commit()
            # Якщо немає більше книг, записуємо число 0 у БД
            if not current_books_list:
                cursor.execute('UPDATE visitors SET books_id = ? WHERE visitor_id = ?', (0, visitor_id))
                connection_library.commit()
            return True and current_visitor  # Книга повернута
        else:
            return False  # Такої книги на відвідувачі нема
    else:
        return False  # Такого відвідувача немає







