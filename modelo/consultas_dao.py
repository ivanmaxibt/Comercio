from .conneciondb import ConeccionDB

def crear_tabla():
    conn = ConeccionDB()

    sql = '''
            CREATE TABLE IF NOT EXISTS Genero(
            ID INTEGER NOT NULL, 
            Nombre VARCHAR(50),
            PRIMARY KEY (ID AUTOINCREMENT)
            );

            CREATE TABLE IF NOT EXISTS Peliculas(
            ID INTEGER NOT NULL, 
            Nombre VARCHAR(150),
            Duacion VARCHAR(4),
            Genero INTEGER,
            PRIMARY KEY (ID AUTOINCREMENT),
            FOREIGN KEY (Genero) References Genero(ID)
            );
            '''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()

    except:
        pass

def listar_generos():
    conn = ConeccionDB()
    listar_generos = []
    sql = """
            SELECT * FROM Genero
         """
    
    try:
        conn.cursor.execute(sql)
        listar_generos = conn.cursor.fetchall()
        conn.cerrar_con()

        return listar_generos
    except:
        pass

def listar_peliculas():
    conn = ConeccionDB()
    listar_peliculas = []
    sql = """
            SELECT * FROM Peliculas as p
            inner join Genero as g
            on p.Genero = g.ID;
         """
    
    try:
        conn.cursor.execute(sql)
        listar_peliculas = conn.cursor.fetchall()
        conn.cerrar_con()

        return listar_peliculas
    except:
        pass


class Peliculas:
    def __init__(self, nombre,duracion, genero):
        self.id_peliculas = None
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero

    def __str__(self):
        return f'Pelicula[{self.nombre},{self.duracion}, {self.genero}]'

def guardar_peli(pelicula):
    conn = ConeccionDB()

    sql = f"""
            INSERT INTO Peliculas (Nombre,Duacion,Genero)
            VALUES('{pelicula.nombre}','{pelicula.duracion}',{pelicula.genero});
            """
    
    conn.cursor.execute(sql)
    conn.cerrar_con()


def editar_peli(pelicula, id):
    conn = ConeccionDB()

    sql = f"""
            UPDATE Peliculas
            SET Nombre = '{pelicula.nombre}', Duacion = '{pelicula.duracion}',Genero = {pelicula.genero}
            WHERE ID = {id};
            """
    
    conn.cursor.execute(sql)
    conn.cerrar_con()


def borrar_peli(id):
    conn = ConeccionDB()

    sql = f"""
            DELETE FROM Peliculas
            WHERE ID = {id};
            """
    
    conn.cursor.execute(sql)
    conn.cerrar_con()