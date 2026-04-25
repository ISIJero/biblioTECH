import sqlite3


# Clase que gestiona la conexión con la base de datos
class DataBaseManagment:
    def __init__(self, db_name="biblioteca_db.db"):
        self.db_name = db_name
        self.con = None
        self.cur = None

    # El método __enter__ se activa al iniciar un bloque with
    def __enter__(self):
        self.con = sqlite3.connect(self.db_name)
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()
        return self

    # El método __exit__ se activa al finalizar un bloque with
    def __exit__(self, exc_type, exc, tb):
        if exc_type is not None:
            # Si la consulta falla hace un rollback
            self.con.rollback()
        else:
            # Si la consulta tiene éxito hace un commit
            self.con.commit()

        # Cierra la conexión con la base de datos después de utilizarla
        self.con.close()

    # Función que se utiliza para UPDATES, INSERTS o CREATES
    def execute_query(self, query, param=()):
        self.cur.execute(query, param)
        return self.cur

    # Función que se utiliza para SELECTS
    def extract_data(self, query, param=()):
        self.cur.execute(query, param)
        return self.cur.fetchall()


if __name__ == "__main__":

    data = list()

    with DataBaseManagment() as DBM:

        DBM.execute_query(
            "INSERT INTO libros (nombre, autor, materia, isbn, cod, estado) VALUES ('El Cuerpo Humano', 'Mengano', 'Cs. Naturales', '426-753-456', 7564436, 1)"
        )
