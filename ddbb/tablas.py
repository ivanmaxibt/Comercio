import sqlite3

conn_usuarios = sqlite3.connect("Usuarios.db")
cursor_usuarios = conn_usuarios.cursor()

# Crear la tabla Usuarios
cursor_usuarios.execute('''
    CREATE TABLE Usuarios (
        IDUsuario INTEGER PRIMARY KEY,
        Nombre TEXT,
        CorreoElectronico TEXT,
        Contrasena TEXT,
        Rol TEXT
    )
''')

# Insertar los registros de ejemplo (como una lista de tuplas)
registros = [
    (101, 'Ana García', 'ana@example.com', '********', 'Cliente'),
    (102, 'Juan Pérez', 'juan@example.com', '********', 'Administrador'),
    (103, 'María López', 'maria@example.com', '********', 'Cliente'),
    (104, 'Carlos Rodríguez', 'carlos@example.com', '********', 'Cliente'),
    (105, 'Laura Martínez', 'laura@example.com', '********', 'Cliente'),
    (106, 'Pedro Sánchez', 'pedro@example.com', '********', 'Cliente'),
    (107, 'Sofía Fernández', 'sofia@example.com', '********', 'Cliente'),
    (108, 'Diego Ramírez', 'diego@example.com', '********', 'Cliente'),
    (109, 'Valentina Torres', 'valentina@example.com', '********', 'Cliente'),
    (110, 'Martín González', 'martin@example.com', '********', 'Cliente')
]

cursor_usuarios.executemany('''
    INSERT INTO Usuarios (IDUsuario, Nombre, CorreoElectronico, Contrasena, Rol)
    VALUES (?, ?, ?, ?, ?)
''', registros)
conn_usuarios.commit()
conn_usuarios.close()

conn_productos = sqlite3.connect("Productos.db")
cursor_productos = conn_productos.cursor()

# Crear la tabla Productos
cursor_productos.execute('''
    CREATE TABLE Productos (
        IDProducto INT PRIMARY KEY,
        NombreProducto NVARCHAR(100),
        Descripcion NVARCHAR(255),
        Precio MONEY,
        Categoria NVARCHAR(50)
    )
''')

# Insertar los registros de ejemplo (como una lista de tuplas)
registros_productos = [
    (201, 'Laptop HP', 'Portátil con procesador i5', 800.00, 'Electrónica'),
    (202, 'Camiseta Nike', 'Camiseta deportiva', 30.00, 'Ropa'),
    (203, 'Auriculares Sony', 'Cancelación de ruido', 150.00, 'Electrónica'),
    (204, 'Zapatos de cuero', 'Elegantes y cómodos', 100.00, 'Calzado'),
    (205, 'Libro "Cien años de soledad"', 'Novela clásica', 20.00, 'Libros'),
    (206, 'Reloj Casio', 'Resistente al agua', 50.00, 'Accesorios'),
    (207, 'Mochila Adidas', 'Espaciosa y duradera', 40.00, 'Bolsos'),
    (208, 'Bicicleta urbana', 'Ideal para la ciudad', 300.00, 'Deportes'),
    (209, 'Cámara Canon', 'DSLR con lente intercambiable', 600.00, 'Fotografía'),
    (210, 'Pelota de fútbol', 'Tamaño oficial', 25.00, 'Deportes')
]

cursor_productos.executemany('''
    INSERT INTO Productos (IDProducto, NombreProducto, Descripcion, Precio, Categoria)
    VALUES (?, ?, ?, ?, ?)
''', registros_productos)

conn_productos.commit()
conn_productos.close()

conn_pedidos = sqlite3.connect("Pedidos.db")
cursor_pedidos = conn_pedidos.cursor()

# Crear la tabla Pedidos
cursor_pedidos.execute('''
    CREATE TABLE Pedidos (
        IDPedido INTEGER PRIMARY KEY,
        FechaPedido DATE,
        IDUsuario INT,
        Productos NVARCHAR(10000),
        EstadoPedido NVARCHAR(50)
    )
''')

# Insertar los registros de ejemplo (como una lista de tuplas)
registros_pedidos = [
    (301, '2024-06-01', 101, '201, 203', 'Pendiente'),
    (302, '2024-06-02', 102, '205, 207', 'Enviado'),
    (303, '2024-06-03', 103, '202, 204', 'Entregado'),
    (304, '2024-06-04', 104, '206, 208', 'Pendiente'),
    (305, '2024-06-05', 105, '209, 210', 'Enviado'),
    (306, '2024-06-06', 106, '201, 203, 205', 'Pendiente'),
    (307, '2024-06-07', 107, '204, 206', 'Entregado'),
    (308, '2024-06-08', 108, '207, 209', 'Pendiente'),
    (309, '2024-06-09', 109, '202, 210', 'Enviado'),
    (310, '2024-06-10', 110, '203, 205', 'Entregado')
]

cursor_pedidos.executemany('''
    INSERT INTO Pedidos (IDPedido, FechaPedido, IDUsuario, Productos, EstadoPedido)
    VALUES (?, ?, ?, ?, ?)
''', registros_pedidos)

conn_pedidos.commit()
conn_pedidos.close()