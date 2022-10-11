import sqlite3


def crear_base():
    con = sqlite3.connect("database.db")
    return con


def crear_tabla(con):
    cursor = con.cursor()
    sql = "CREATE TABLE perros(id integer PRIMARY KEY, nombre text)"
    cursor.execute(sql)
    con.commit()


con = crear_base()
crear_tabla(con)

# segundo commit


def insertar(con, mi_id, nombre):
    cursor = con.cursor()
    mi_id = int(mi_id)
    data = (mi_id, nombre)
    sql = "INSERT INTO perros(id, nombre) VALUES (?, ?);"
    cursor.execute(sql, data)
    con.commit()


con = crear_base()
insertar(con, 4, "perrito")
