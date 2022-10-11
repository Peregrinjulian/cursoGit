import sqlite3


def crear_database():
    con = sqlite3.connect("database.db")
    return con


def crear_tabla(con):
    cursor = con.cursor()
    sql = "CREATE TABLE gatos(id integer PRIMARY KEY, nombre text)"
    cursor.execute(sql)
    con.commit()


con = crear_base()
crear_tabla(con)

# segundo commit
# borre lo de abajo
