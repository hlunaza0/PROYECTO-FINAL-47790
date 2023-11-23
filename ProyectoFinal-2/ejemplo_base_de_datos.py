import sqlite3

conn = sqlite3.connect("mi_base_de_datos.sqlite3")

cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS user
              (Identificacion INTEGER PRIMARY KEY, Nombre TEXT, Edad INTEGER)''')

cursor.execute("INSERT INTO user (nombre, edad) VALUES ('Carlos',32)")
cursor.execute("INSERT INTO user (nombre, edad) VALUES ('Julia',32)")
cursor.execute("INSERT INTO user (nombre, edad) VALUES ('Adan',32)")

conn.commit()

tabla = "user"
cursor.execute(f"SELECT * FROM {tabla}")

filas = cursor.fetchall()
for fila in filas:
    print(fila)

conn.close()
