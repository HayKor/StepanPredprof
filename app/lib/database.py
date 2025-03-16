#
# Файл, содеражщий в себе исходный код всех операций с БД
# База данных используется в формате SQLite со встроенное в python библиотекой sqilte3
# База данных хранит в себе информацию в долгострочной перспективе на локальном устройстве
#

import sqlite3 as sql


# переменная для хранения пути до файла БД в формате .db
FILE: str = "data.db"


def createDatabase() -> None:
    """
    Функция создания новой таблицы в базе данных _._._

    База данных хранит в себе информацию:

    - 1
    - 2
    - 3

    """

    db = sql.connect(FILE)
    cursor = db.cursor()
    # matrix data
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS matrixs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT NOT NULL
        )
    """
    )
    # Coords data & prices
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS coords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender TEXT NOT NULL,
            listener TEXT NOT NULL,
            prices TEXT NOT NULL
        )
    """
    )
    # сохраняем и закрываем
    db.commit()
    db.close()


def addMatrix(data):
    db = sql.connect(FILE)
    cursor = db.cursor()

    cursor.execute(
        f"""
        INSERT INTO martrixs(data) VALUES('{data}')
    """
    )

    db.commit()
    db.close()

    return "Success"


def addCoords(sender, listener, price):
    db = sql.connect(FILE)
    cursor = db.cursor()

    cursor.execute(
        f"""
        INSERT INTO coords(sender, listener, price) VALUES('{sender}', '{listener}', '{price}')
    """
    )

    db.commit()
    db.close()

    return "Success"


# запуск тестирующей части (при неоходимости)
if __name__ == "__main__":
    createDatabase()
