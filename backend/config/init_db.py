from .db_connection import DataBaseManagment

dbm = DataBaseManagment()


def create_db():

    querys = [
        """CREATE TABLE IF NOT EXISTS libros (id INTEGER PRIMARY KEY, nombre TEXT, autor TEXT, materia TEXT, isbn TEXT, cod INTEGER, estado INTEGER);""",
        """CREATE TABLE IF NOT EXISTS personas (id INTEGER PRIMARY KEY, nombre TEXT, curso TEXT, rol INTEGER);""",
        """CREATE TABLE IF NOT EXISTS prestamos (idLibro INTEGER, idPersona INTEGER, fecha_retiro TEXT, fecha_entrega TEXT, estado INTEGER, FOREIGN KEY (idLibro) REFERENCES libros (id), FOREIGN KEY (idPersona) REFERENCES personas (id));""",
    ]

    with dbm:
        for query in querys:
            dbm.execute_query(query=query)


if __name__ == "__main__":

    create_db()
