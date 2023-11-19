import sqlite3

__connection = None


# функція підключення до таблиці
def get_connection():
    global __connection
    if __connection is None:
        __connection = sqlite3.connect("agro.db")
    return __connection


# ініціалізація таблиці
def init_db():
    connect = get_connection()
    curs = connect.cursor()

    curs.execute("""
        CREATE TABLE IF NOT EXISTS orenda(
            num          INTEGER PRIMARY KEY AUTOINCREMENT,
            tech_id     INTEGER NOT NULL,
            email       TEXT NOT NULL,
            address       TEXT NOT NULL,
            first        TEXT NOT NULL,
            phone        TEXT NOT NULL,
            days         INTEGER NOT NULL,
            total_price    REAL NOT NULL,
            FOREIGN KEY (tech_id) REFERENCES agro_technics(agro_id)
            FOREIGN KEY (email) REFERENCES users(email)
            FOREIGN KEY (first) REFERENCES users(first)
            );
        """)

    connect.commit()

    curs.execute("""
        CREATE TABLE IF NOT EXISTS users(
            first     TEXT NOT NULL,
            last        TEXT NOT NULL,
            email        TEXT NOT NULL,
            password    TEXT NOT NULL
        );
    """)

    connect.commit()

    curs.execute("""
        CREATE TABLE IF NOT EXISTS agro_technics(
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            agro_id     INTEGER NOT NULL,
            type        TEXT NOT NULL,
            name        TEXT NOT NULL,
            location    TEXT NOT NULL,
            photo       BLOB DEFAULT 1,
            appoint     TEXT NOT NULL,
            charact     TEXT NOT NULL,
            price       INTEGER NOT NULL
        );
    """)

    connect.commit()


# клас виклику інтерфейсів
class Menu:
    # стартове меню
    @staticmethod
    def reg_menu():
        cmd = input("*****************************\n"
                    "*           ВХІД            *\n"
                    "*  10 - Увійти              *\n"
                    "*  20 - Зареєстуватися      *\n"
                    "*  30 - Вихід               *\n"
                    "*****************************\n"
                    "   Введіть команду:")
        while cmd != "Exit":
            if cmd == "10":
                CreateUser.login()
            elif cmd == "20":
                CreateUser.registr_user()
            elif cmd == "30":
                break
            else:
                print("Команди не існує!")
            cmd = input("*****************************\n"
                        "*           ВХІД            *\n"
                        "*  10 - Увійти              *\n"
                        "*  20 - Зареєстуватися      *\n"
                        "*  30 - Вихід               *\n"
                        "*****************************\n"
                        "   Введіть команду:")
        return

    # головне меню користувача
    @staticmethod
    def main_user():
        cmd = input("   **********************************\n"
                    " *             ГОЛОВНА(U)              *\n"
                    "*  11 - Переглянути доступний транспорт *\n"
                    "*  22 - Взяти в оренду                   *\n"
                    "*  33 - Як користуватись?               *\n"
                    " * 44 - Вихід з програми              *\n"
                    "   *********************************\n"
                    "   Введіть команду:")
        while cmd != "Exit":
            if cmd == "11":
                User.list_agro()
            elif cmd == "22":
                User.orenda()
            elif cmd == "33":
                User.how_to_use()
            elif cmd == "44":
                break
            else:
                print("Команди не існує!")
            cmd = input("   **********************************\n"
                        " *             ГОЛОВНА(U)              *\n"
                        "*  11 - Переглянути доступний транспорт *\n"
                        "*  22 - Взяти в оренду                   *\n"
                        "*  33 - Як користуватись?               *\n"
                        " * 44 - Вихід з програми              *\n"
                        "   *********************************\n"
                        "   Введіть команду:")
        return

    # головне меню адміна
    @staticmethod
    def main_admin():
        cmd = input("************************************\n"
                    "*             ГОЛОВНА(A)           *\n"
                    "*  1 - Добавити транспорт          *\n"
                    "*  2 - Видалити транспорт          *\n"
                    "*  3 - Редагувати транспорт        *\n"
                    "*  4 - Переглянути запити на оренду*\n"
                    "*  5 - Переглянути весь транспорт  *\n"
                    "*  6 - Вихід з програми            *\n"
                    "************************************\n"
                    "   Введіть команду:")
        while cmd != "Exit":
            if cmd == "1":
                Admin.add_tech()
            elif cmd == "2":
                Menu.delete_tech()
            elif cmd == "3":
                Admin.edit_tech()
            elif cmd == "4":
                Admin.orenda_list()
            elif cmd == "5":
                User.list_agro()
            elif cmd == "6":
                break
            else:
                print("Команди не існує!")
            cmd = input("************************************\n"
                        "*             ГОЛОВНА(A)           *\n"
                        "*  1 - Добавити транспорт          *\n"
                        "*  2 - Видалити транспорт          *\n"
                        "*  3 - Редагувати транспорт        *\n"
                        "*  4 - Переглянути запити на оренду*\n"
                        "*  5 - Переглянути весь транспорт  *\n"
                        "*  6 - Вихід з програми            *\n"
                        "************************************\n"
                        "   Введіть команду:")
        return

    # видалення інформації з таблиці
    @staticmethod
    def delete_tech():
        cmd = input("|--------------------------|\n"
                    "|    МЕНЮ ВИДАЛЕННЯ        |\n"
                    "|-1 - Видалити по id       |\n"
                    "|-2 - Видалити по agro_id  |\n"
                    "|-3 - Видалити по name     |\n"
                    "|-4 - Вернутися назад      |\n"
                    "|--------------------------|\n"
                    "  Введіть команду:")
        while cmd != "-4":
            if cmd == "-1":
                Admin.remove_by_id()
            elif cmd == "-2":
                Admin.remove_by_agro_id()
            elif cmd == "-3":
                Admin.remove_by_name()
            elif cmd == "-4":
                break
            else:
                print("--------------------------\n"
                      "Команди не існує!\n"
                      "--------------------------")
            cmd = input("|--------------------------|\n"
                        "|    МЕНЮ ВИДАЛЕННЯ        |\n"
                        "|-1 - Видалити по id       |\n"
                        "|-2 - Видалити по agro_id  |\n"
                        "|-3 - Видалити по name     |\n"
                        "|-4 - Вернутися назад      |\n"
                        "|--------------------------|\n"
                        "  Введіть команду:")
        return


# клас створення нового користувача і запис його в таблицю
class CreateUser:

    def __init__(self, first, last, email, password):
        self.first = first
        self.last = last
        self.email = email
        self.password = password

    # функція запису користувача в таблицю
    def set_new_user(self):
        connect = get_connection()
        curs = connect.cursor()
        try:
            print("--------------------------\n"
                  "Підключення успішне")
            curs.execute(
                'INSERT INTO users (first, last, email, password) VALUES (?,?,?,?)',
                (self.first, self.last, self.email, self.password))
            connect.commit()
            print("Користувач створений успішно\n"
                  "Тепер можете увійти\n"
                  "--------------------------")

        except sqlite3.Error as error:
            print("Помилка при роботі з БД", error)

    # функція реєстрація користувача
    @staticmethod
    def registr_user():
        print("--------------------------\n"
              "       РЕЄСТРАЦІЯ          ")
        first = input("Введіть Імя:")
        last = input("Введіть Прізвище:")
        email = input("Введіть Email:")
        password = input("Введіть Пароль:")

        try:
            new_user = CreateUser(first, last, email, password)
            CreateUser.set_new_user(new_user)

        except sqlite3.Error as error:
            print("Помилка при роботі з БД", error)

    # функція входу в систему
    @staticmethod
    def login():
        email = input("Введіть Email:")
        try:
            connect = get_connection()
            curs = connect.cursor()
            curs.execute('SELECT * FROM users WHERE email = ?', (email,))
            r = curs.fetchone()
            if r is None:
                print("Такого користувача не існує")
            # вхід під адміністратором
            elif email == "admin":
                try:
                    password = input("Введіть Pass:")
                    curs.execute('SELECT password FROM users WHERE password = ?', (password,))
                    r = curs.fetchone()
                    f = r[0]
                    if password == str(f):
                        print("Ви авторизовані як адммін")
                        Menu.main_admin()
                except:
                    print("Пароль невірний")
            # вхід під користувачем
            else:
                try:
                    password = input("Введіть Pass:")
                    curs.execute('SELECT password FROM users WHERE password = ?', (password,))
                    r = curs.fetchone()
                    f = r[0]
                    if password == f:
                        print("Ви авторизовані")
                        Menu.main_user()
                except:
                    print("Пароль невірний")
        except sqlite3.Error as error:
            print("Помилка при роботі з БД", error)


# клас навігація для користувача
class User:
    # функція оренди транспорту
    @staticmethod
    def orenda():
        connect = get_connection()
        curs = connect.cursor()
        print("------ОРЕНДА ТРАНСПОРТУ------")
        tech_id = input("Введіть ID Tранспорту:")
        email = input("Введіть Ваш Email:")
        try:
            curs.execute('SELECT first FROM users WHERE email = ?', (email,))
            r = curs.fetchone()
            n = r[0]
            first = n
        except:
            first = "Невідомо"

        address = input("Введіть Домашню Адресу:")
        phone = input("Введіть Номер телефону(формат:033225554):")
        days = input("Введіть кількість днів оренди:")
        curs.execute('SELECT price FROM agro_technics WHERE agro_id = ?', (tech_id,))
        r = curs.fetchone()
        t = r[0]
        total_price = int(t) * int(days)
        print(f"Сума оренди:{total_price}грн.")
        try:
            connect = get_connection()
            curs = connect.cursor()
            print("--------------------------\n"
                  "Підключення успішне")
            curs.execute(
                'INSERT INTO orenda (tech_id, email, address, first, phone, days, total_price) VALUES (?,?,?,?,?,?,?)',
                (tech_id, email, address, first, phone, days, total_price))
            connect.commit()
            print("Запит на оренду створений\n"
                  "--------------------------")

        except sqlite3.Error as error:
            print("Помилка при роботі з БД", error)

    @staticmethod
    # довідка як орендувати транстпорт
    def how_to_use():
        print("Щоб взяти транспорт в оренду потрібно ввести 'ID Транспорту' транспорту.\n"
              "Після чого вказати ваш електронний адрес який ви вказували при реєстрації\n"
              "Коректно написати вашу адресу в вигляді:\n"
              "  <індкес>,<місто/село>,<вулиця>,<будинок>\n"
              "  Наприклад: 83100, Львів, Івана Франка, 321/а\n"
              "Вказати ваш робочий номер телефону\n"
              "Кількість днів оренди\n"
              "Після подачі заявки очікуйте дзвінка від нашого менеджра для підтвердження інформації.\n")

    @staticmethod
    # функція виводу повної інформації з таблиці
    def list_agro():
        try:
            connect = get_connection()
            curs = connect.cursor()
            print("--------------------------\n"
                  "Підключення успішне")
            curs.execute('SELECT * FROM agro_technics')
            data = curs.fetchall()
            print("Кількість транспорту: ", len(data))

            if len(data) == 0:
                print("Немає даних\n"
                      "--------------------------")
            else:
                print("Інформація про кожний:")
                for row in data:
                    print("ID:", row[0])
                    print("ID Трансторту:", row[1])
                    print("Тип:", row[2])
                    print("Марка:", row[3])
                    print("Місто:", row[4])
                    print("Фото:", row[5])
                    print("Призначення:", row[6])
                    print("Характеристики:", row[7])
                    pr = row[8]
                    print("Ціна:", pr, "за 1 день / ", ((pr * 7) - pr), "за 7 днів /", ((pr * 30) - (pr * 7)),
                          "за 30 днів",
                          end="\n\n")
                print("Дані зчитано успішно\n"
                      "--------------------------")
            curs.close()

        except sqlite3.Error as error:
            print("Помилка при роботі з БД", error)


# клас навігація для адміністратора
class Admin:

    def __init__(self, agro_id, type, name, location, photo, appoint, charact, price):
        self.agro_id = agro_id
        self.type = type
        self.name = name
        self.location = location
        self.photo = photo
        self.appoint = appoint
        self.charact = charact
        self.price = price

    def set_new(self):
        try:
            connect = get_connection()
            curs = connect.cursor()
            print("--------------------------\n"
                  "Підключення успішне")
            curs.execute(
                'INSERT INTO agro_technics (agro_id, type, name, location, photo, appoint, charact, price) VALUES (?,'
                '?,?,?,?,?,?,?)',
                (self.agro_id, self.type, self.name, self.location, self.photo, self.appoint, self.charact, self.price))
            connect.commit()
            print("Дані записані успішно\n"
                  "--------------------------")

        except sqlite3.Error as error:
            print("Помилка при роботі з БД", error)

    @staticmethod
    # дадавання новий даних в таблицю
    def add_tech():
        print("--------------------------\n"
              "СТВОРЕННЯ НОВОГО ТРАНСПОРТУ")
        agro_id = input("Введіть agro_id:")
        type = input("Введіть type:")
        name = input("Введіть name:")
        location = input("Введіть location:")
        photo = input("Введіть Photo:")
        appoint = input("Введіть appoint:")
        charact = input("Введіть charact:")
        price = input("Введіть price:")
        try:
            new_tech = Admin(agro_id, type, name, location, photo, appoint, charact, price)
            Admin.set_new(new_tech)

        except sqlite3.Error as error:
            print("Помилка при роботі з БД", error)

    # видалення даних по id
    @staticmethod
    def remove_by_id():
        id = int(input("Введіть id по якому хочете видалити транспорт: "))
        try:
            connect = get_connection()
            curs = connect.cursor()
            print("Підключення успішне")
            curs.execute('SELECT id FROM agro_technics WHERE id = ?', (id,))
            data = curs.fetchall()
            if not data:
                print("Техніка з таким id не знайдена")
            else:
                curs.execute(
                    'DELETE FROM agro_technics WHERE id = ?', (id,))
                connect.commit()
                print("Дані видалено успішно")

        except sqlite3.Error as error:
            print("Помилка при роботі з БД", error)

    # видалення даних по agro_id
    @staticmethod
    def remove_by_agro_id():
        agro_id = int(input("Введіть agro_id по якому хочете видалити транспорт:"))
        try:
            connect = get_connection()
            curs = connect.cursor()
            print("Підключення успішне")
            curs.execute('SELECT agro_id FROM agro_technics WHERE agro_id = ?', (agro_id,))
            data = curs.fetchall()
            if not data:
                print("Техніка з таким agro_id не знайдена")
            else:
                curs.execute(
                    'DELETE FROM agro_technics WHERE agro_id = ?', (agro_id,))
                connect.commit()
                print("Дані видалено успішно")

        except sqlite3.Error as error:
            print("Помилка при роботі з БД", error)

    # видалення даних по name
    @staticmethod
    def remove_by_name():
        name = input("Введіть name по якому хочете видалити транспорт: ")
        try:
            connect = get_connection()
            curs = connect.cursor()
            print("Підключення успішне")
            curs.execute('SELECT name FROM agro_technics WHERE name = ?', (name,))
            data = curs.fetchall()
            if not data:
                print("Техніка з таким name не знайдена")
            else:
                curs.execute(
                    'DELETE FROM agro_technics WHERE name = ?', (name,))
                connect.commit()
                print("Дані видалено успішно")

        except sqlite3.Error as error:
            print("Помилка при роботі з БД", error)

    # реданування даних в таблиці
    @staticmethod
    def edit_tech():
        try:
            id = int(input("Введіть id транспорту в якому хочете змінити дані: "))
            connect = get_connection()
            curs = connect.cursor()
            print("Підключення успішне")
            cmd = input("+++++++++++++++++++++++++++++++++\n"
                        "+           РЕДАГУВАННЯ         +\n"
                        "+  +1 - Змінити agro_id         +\n"
                        "+  +2 - Змінити name            +\n"
                        "+  +3 - Змінити price           +\n"
                        "+  +4 - Переглянути вибраний    +\n"
                        "+  +5 - Назад                   +\n"
                        "+++++++++++++++++++++++++++++++++\n"
                        "   Введіть команду:")
            while cmd != "Exit":
                if cmd == "+1":
                    new_agro_id = int(input("Введіть нове agro_id: "))
                    curs.execute('UPDATE agro_technics SET agro_id == ? WHERE id ==?', (new_agro_id, id))
                    break
                elif cmd == "+2":
                    new_name = input("Введіть нове name: ")
                    curs.execute('UPDATE agro_technics SET name == ? WHERE id ==?', (new_name, id))
                    break
                elif cmd == "+3":
                    new_price = int(input("Введіть нове price: "))
                    curs.execute('UPDATE agro_technics SET price == ? WHERE id ==?', (new_price, id))
                    break
                elif cmd == "+4":
                    curs.execute('SELECT * FROM agro_technics WHERE id = ?', (id,))
                    r = curs.fetchall()
                    for row in r:
                        print("ID:", row[0])
                        print("ID Трансторту:", row[1])
                        print("Тип:", row[2])
                        print("Марка:", row[3])
                        print("Місто:", row[4])
                        print("Фото:", row[5])
                        print("Призначення:", row[6])
                        print("Характеристики:", row[7])
                        pr = row[8]
                        print("Ціна:", pr, "за 1 день / ", ((pr * 7) - pr), "за 7 днів /", ((pr * 30) - (pr * 7)),
                              "за 30 днів",
                              end="\n\n")
                    print("Дані зчитано успішно\n"
                          "--------------------------")
                    print(r)
                elif cmd == "+5":
                    break
                else:
                    print("Команди не існує!")
                cmd = input("+++++++++++++++++++++++++++++++++\n"
                            "+           РЕДАГУВАННЯ         +\n"
                            "+  +1 - Змінити agro_id         +\n"
                            "+  +2 - Змінити name            +\n"
                            "+  +3 - Змінити price           +\n"
                            "+  +4 - Переглянути вибраний    +\n"
                            "+  +5 - Назад                   +\n"
                            "+++++++++++++++++++++++++++++++++\n"
                            "   Введіть команду:")

            # curs.execute('UPDATE agro_technics SET id == ? WHERE id ==?', (rid, id))
            connect.commit()
            print("Дані змінено успішно")

        except sqlite3.Error as error:
            print("Помилка при роботі з БД", error)

    # функція виводу інформації про запити на оренду
    @staticmethod
    def orenda_list():
        try:
            connect = get_connection()
            curs = connect.cursor()
            print("--------------------------\n"
                  "Підключення успішне")
            curs.execute('SELECT * FROM orenda')
            data = curs.fetchall()
            print("Кількість запитів: ", len(data))

            if len(data) == 0:
                print("Немає запитів на оренду\n"
                      "--------------------------")
            else:
                print("Запити на оренду:")
                for row in data:
                    print("Номер:", row[0])
                    print("ID Трансторту який орендується:", row[1])
                    print("Email користувача:", row[2])
                    print("Адресса користувача:", row[3])
                    print("Ім'я:", row[4])
                    print("Номер телефону:", row[5])
                    print("Кількість днів оренди:", row[6])
                    print("Сума оренди:", row[7], end="\n\n")
                print("Дані зчитано успішно\n"
                      "--------------------------")
            curs.close()

        except sqlite3.Error as error:
            print("Помилка при роботі з БД", error)


if __name__ == '__main__':
    init_db()
    Menu.reg_menu()
