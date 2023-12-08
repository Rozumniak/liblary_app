﻿#Надіюсь написано не зовсім по конченому 
import sqlite3


connection_authors = sqlite3.connect('authors.db')
cursor_authors = connection_authors.cursor()


cursor_authors.execute('''CREATE TABLE IF NOT EXISTS authors (
                        author_id INTEGER PRIMARY KEY,
                        author_name TEXT)''')


authors_data = [
    (1, 'Тарас Шевченко'),
    (2, 'Леся Українка'),
    (3, 'Іван Франко'),
    (4, 'Михайло Коцюбинський'),
    (5, 'Остап Вишня'),
    (6, 'Василь Стефаник'),
    (7, 'Панас Мирний'),
    (8, 'Ліна Костенко'),
    (9, 'Юрій Андрухович'),
    (10, 'Сергій Жадан'),
    (11, 'Олесь Гончар'),
    (12, 'Юрій Іздрик'),
    (13, 'Василь Симоненко'),
    (14, 'Олександр Олесь'),
    (15, 'Павло Загребельний'),
    (16, 'Леонід Первомайський'),
    (17, 'Василь Шкляр'),
    (18, 'Олександр Копиленко'),
    (19, 'Марко Вовчок'),
    (20, 'Микола Куліш'),
    
]

cursor_authors.executemany('INSERT INTO authors VALUES (?, ?)', authors_data)
connection_authors.commit()


connection_books = sqlite3.connect('books.db')
cursor_books = connection_books.cursor()


cursor_books.execute('''CREATE TABLE IF NOT EXISTS books (
                        book_id INTEGER PRIMARY KEY,
                        author_id INTEGER,
                        book_title TEXT)''')


books_data = [
    # Тарас Шевченко
    (1, 1, 'Кобзар'),
    (2, 1, 'Гайдамаки'),
    (3, 1, 'Заповіт'),
    # Леся Українка
    (4, 2, 'Лірика Лесі Українки'),
    (5, 2, 'Сонети'),
    (6, 2, 'Відлуння'),
    # Іван Франко
    (7, 3, 'Зібрані твори у 50-ти томах'),
    (8, 3, 'Лірика Івана Франка'),
    (9, 3, 'Записки смертника'),
    #Михайло Коцюбинський
    (10, 4, 'Intermezzo'),
    (11, 4, 'Дорогою ціною'),
    (12, 4, 'На крилах пісень'),
    #Остап Вишня
    (13, 5, 'Зібрані твори'),
    (14, 5, 'Анекдоти'),
    (15, 5, 'Веселий Львів'),
    #Василь Стефаник
    (16, 6, 'На порозі'),
    (17, 6, 'Камінний хрест'),
    (18, 6, 'Сльози матері'),
    #Панас Мирний
    (19, 7, 'Новели'),
    (20, 7, 'Злагода'),
    (21, 7, 'Без кайданів'),
    #Ліна Костенко
    (22, 8, 'Записки української фронтовички'),
    (23, 8, 'Земля в огні'),
    (24, 8, 'Дорога моїх сновидінь'),
    #Юрій Андрухович
    (25, 9, 'Пerverzion'),
    (26, 9, 'Рекреації'),
    (27, 9, 'Лексикон інтимних міст'),
    #Сергій Жадан
    (28, 10, 'Ворошиловград'),
    (29, 10, 'Месопотамія'),
    (30, 10, 'Поезія'),
    #Олесь Гончар
    (31, 11, 'Картина світу'),
    (32, 11, 'Собор'),
    (33, 11, 'Безодня'),
    #Юрій Іздрик
    (34, 12, 'Місто'),
    (35, 12, 'Країна мрій'),
    (36, 12, 'Різдвяні історії'),
    #Василь Симоненко
    (37, 13, 'Вибрані твори'),
    (38, 13, 'Вечірній світ'),
    (39, 13, 'Слово про батьківщину'),
    #Олександр Олесь
    (40, 14, 'Княгиня Ольга'),
    (41, 14, 'Лірика Олександра Олеся'),
    (42, 14, 'Серце Вкраїни'),
    #Павло Загребельний
    (43, 15, 'Соняшний промінь'),
    (44, 15, 'Голоси душі'),
    (45, 15, 'Листи до друзів'),
    #Леонід Первомайський
    (46, 16, 'Весняні зірки'),
    (47, 16, 'Слово і діло'),
    (48, 16, 'Пісні Л.Первомайський'),
    #Василь Шкляр
    (49, 17, 'Лірики В.Шкляра'),
    (50, 17, 'Вірші В.Шкляр'),
    (51, 17, 'Вечірні спогади'),
    #Олександр Копиленко
    (52, 18, 'Звуки і мить'),
    (53, 18, 'Вірші О.Копиленко'),
    (54, 18, 'Живе слово'),
    #Марко Вовчок
    (55, 19, 'Лірика М.Вовчок'),
    (56, 19, 'Сонети'),
    (57, 19, 'Зорі'),
    #Микола Куліш
    (58, 20, 'Чорна рада'),
    (59, 20, 'На греблі"'),
    (60, 20, 'Семен Кожем*яка'),
]

cursor_books.executemany('INSERT INTO books VALUES (?, ?, ?)', books_data)
connection_books.commit()


#Частина з пошуком книг за автором

# З'єднання з базою даних авторів
connection_authors = sqlite3.connect('authors.db')
cursor_authors = connection_authors.cursor()

# З'єднання з базою даних книг
connection_books = sqlite3.connect('books.db')
cursor_books = connection_books.cursor()

# пошуку книг за автором
def search_books_by_author(author_name):
    cursor_authors.execute('SELECT author_id FROM authors WHERE author_name = ?', (author_name,))
    author_id = cursor_authors.fetchone()[0]

    cursor_books.execute('SELECT book_title FROM books WHERE author_id = ?', (author_id,))
    books = cursor_books.fetchall()

    return books




#Частина з інтеграцією кнопок.Використав Tkinter,якщо треба то заміни на щось інше
import tkinter as tk

def on_button_click():
    author_name = entry.get()
    books = search_books_by_author(author_name)

    # Дії зі списком книг (наприклад, вивід у вікно програми)
    for book in books:
        label = tk.Label(root, text=book[0])
        label.pack()

root = tk.Tk()
label = tk.Label(root, text="Введіть ім'я автора:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Пошук", command=on_button_click)
button.pack()

root.mainloop()

import sqlite3


#Частина про нас
# База даних користувачів
connection_users = sqlite3.connect('users.db')
cursor_users = connection_users.cursor()


cursor_users.execute('''CREATE TABLE IF NOT EXISTS users (
                        user_id INTEGER PRIMARY KEY,
                        username TEXT)''')


users_data = [
    (1, 'Аліна Хохич'),
    (2, 'Дмитро Євтушенко'),
    (3, 'Ілля Крутько'),
    (4, 'Руслан Розумняк'),
    (5, 'Сергій Бабенко'),
]

cursor_users.executemany('INSERT INTO users VALUES (?, ?)', users_data)
connection_users.commit()


#Частина про читачів(пуста база даних)
import sqlite3


connection_readers = sqlite3.connect('readers.db')
cursor_readers = connection_readers.cursor()


cursor_readers.execute('''CREATE TABLE IF NOT EXISTS readers (
                            reader_id INTEGER PRIMARY KEY,
                            reader_name TEXT,
                            reader_email TEXT,
                            reader_phone TEXT)''')

connection_readers.commit()


# Автори та книги

import sqlite3


connection = sqlite3.connect('library.db')
cursor = connection.cursor()

# Створення таблиці авторів
cursor.execute('''CREATE TABLE IF NOT EXISTS authors (
                    author_id INTEGER PRIMARY KEY,
                    author_name TEXT)''')

# Створення таблиці книг
cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                    book_id INTEGER PRIMARY KEY,
                    author_id INTEGER,
                    book_title TEXT,
                    genre TEXT,
                    available INTEGER)''')

# Список авторів з книгами та їх жанрами
authors_books = [
    (1, 'Тарас Шевченко', 'Кобзар', 'Поезія', 5),
    (1, 'Тарас Шевченко', 'Гайдамаки', 'Історична література', 8),
    (1, 'Тарас Шевченко', 'Заповіт', 'Політична література', 3),
    (2, 'Леся Українка', 'Лірика', 'Поезія', 3),
    (2, 'Леся Українка', 'Сонети', 'Поезія', 6),
    (2, 'Леся Українка', 'Відлуння', 'Поезія', 2),
     
    # Іван Франко
    (3 ,'Іван Франко' ,'Зібрані твори у 50-ти томах','Збірка',3),
    (3,'Іван Франко' , 'Лірика Івана Франка','Поезія',2),
    (3,'Іван Франко' , 'Записки смертника','Філософська проза',4),
    #Михайло Коцюбинський
    (4, 'Михайло Коцюбинський', 'Intermezzo','Роман',3),
    (4,'Михайло Коцюбинський' , 'Дорогою ціною','Роман',4),
    (4, 'Михайло Коцюбинський', 'На крилах пісень','Роман',1),
    #Остап Вишня
    (5, 'Остап Вишня', 'Зібрані твори','Гумореска',7),
    (5,'Остап Вишня' , 'Анекдоти','Гумореска',4),
    (5, 'Остап Вишня', 'Веселий Львів','Гумореска',3),
    #Василь Стефаник
    (6, 'Василь Стефаник', 'На порозі','Психологічна проза',6),
    (6, 'Василь Стефаник', 'Камінний хрест','Психологічна проза',4),
    (6, 'Василь Стефаник', 'Сльози матері','Психологічна проза',3),
    #Панас Мирний
    (7, 'Панас Мирний', 'Новели','Новелa',6),
    (7,'Панас Мирний' , 'Злагода','Новелa',4),
    (7,'Панас Мирний' , 'Без кайданів','Новелa',2),
    #Ліна Костенко
    (8, 'Ліна Костенко', 'Записки української фронтовички','Поезія',3),
    (8, 'Ліна Костенко', 'Земля в огні','Поезія',2),
    (8, 'Ліна Костенко', 'Дорога моїх сновидінь','Поезія',1),
    #Юрій Андрухович
    (9, 'Юрій Андрухович', 'Пerverzion','Сучасна проза',4),
    (9, 'Юрій Андрухович', 'Рекреації','Сучасна проза',5),
    (9, 'Юрій Андрухович', 'Лексикон інтимних міст','Сучасна проза',3),
    #Сергій Жадан
    (10, 'Сергій Жадан', 'Ворошиловград','Поезія',4),
    (10, 'Сергій Жадан', 'Месопотамія','Поезія',5),
    (10, 'Сергій Жадан', 'Поезія','Поезія',2),
    #Олесь Гончар
    (11,'Олесь Гончар', 'Картина світу','Роман',2),
    (11,'Олесь Гончар' , 'Собор','Роман',7),
    (11,'Олесь Гончар' , 'Безодня','Роман',5),
    #Юрій Іздрик
    (12,'Юрій Іздрик' , 'Місто','Проза',3),
    (12,'Юрій Іздрик' , 'Країна мрій','Проза',4),
    (12,'Юрій Іздрик' , 'Різдвяні історії','Проза',4),
    #Василь Симоненко
    (13,'Василь Симоненко' , 'Вибрані твори','Поезія',3),
    (13,'Василь Симоненко' , 'Вечірній світ','Поезія',3),
    (13, 'Василь Симоненко', 'Слово про батьківщину','Поезія',3),
    #Олександр Олесь
    (14, 'Олександр Олесь', 'Княгиня Ольга','Лірична драма',3),
    (14,'Олександр Олесь' , 'Лірика Олександра Олеся','Лірична драма',3),
    (14,'Олександр Олесь' , 'Серце Вкраїни','Лірична драма',4),
    #Павло Загребельний
    (15, 'Павло Загребельний', 'Соняшний промінь','Лірика',2),
    (15, 'Павло Загребельний', 'Голоси душі','Лірика',4),
    (15, 'Павло Загребельний', 'Листи до друзів','Лірика',2),
    #Леонід Первомайський
    (16, 'Леонід Первомайський', 'Весняні зірки','Поезія',5),
    (16, 'Леонід Первомайський', 'Слово і діло','Поезія',4),
    (16, 'Леонід Первомайський', 'Пісні Л.Первомайський','Поезія',3),
    #Василь Шкляр
    (17, 'Василь Шкляр', 'Лірики В.Шкляра','Лірика',4),
    (17, 'Василь Шкляр', 'Вірші В.Шкляр','Лірика',3),
    (17, 'Василь Шкляр', 'Вечірні спогади','Лірика',1),
    #Олександр Копиленко
    (18, 'Олександр Копиленко', 'Звуки і мить','Поезія',6),
    (18, 'Олександр Копиленко', 'Вірші О.Копиленко','Поезія',5),
    (18, 'Олександр Копиленко', 'Живе слово','Поезія',5),
    #Марко Вовчок
    (19,  'Марко Вовчок', 'Лірика М.Вовчок','Лірика',5),
    (19, 'Марко Вовчок', 'Сонети','Лірика',5),
    (19, 'Марко Вовчок', 'Зорі','Лірика',7),
    #Микола Куліш
    (20, 'Микола Куліш', 'Чорна рада','Історична література',9),
    (20, 'Микола Куліш', 'На греблі"','Історична література',5),
    (20, 'Микола Куліш', 'Семен Кожем*яка','Історична література',7),
    
]


cursor.executemany('INSERT INTO authors (author_id, author_name) VALUES (?, ?)', [(author[0], author[1]) for author in authors_books])
cursor.executemany('INSERT INTO books (author_id, book_title, genre, available) VALUES (?, ?, ?, ?)', authors_books)


connection.commit()


connection.close()



#Функція пошуку за жанром
import sqlite3

def search_books_by_genre(genre):
    connection = sqlite3.connect('library.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM books WHERE genre=?', (genre,))
    books = cursor.fetchall()

    connection.close()
    return books