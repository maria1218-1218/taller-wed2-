import sqlite3

conexion = sqlite3.connect('web2.sqlite3')
cursor = conexion.cursor()

cursor.execute("""
DROP TABLE IF EXISTS productos;
""")

cursor.execute("""
CREATE TABLE if NOT EXISTS productos (
  id INTEGER PRIMARY KEY,
  categoria TEXT NOT NULL,
  marca TEXT NOT NULL,
  nombre TEXT NOT NULL,
  descripcion TEXT NOT NULL,
  precio INTEGER NOT NULL
);
""")

datos = [
  (101, 'Celular', 'Apple', 'iPhone 15', '128GB+6GB RAM, Pantalla 6.1p, Chip A16 Bionic,   cable Tipo C, Cámara 28MP', 4599000),
  (104, 'Celular', 'Samsung', 'Galaxy S23', '256GB+8GB RAM, Pantalla 6p, Chip SM8550       Octacore, cámaras 50MP+10MP+12MP', 3499000),
  (201, 'Portátil', 'Apple', 'Macbook Pro M2', 'Chip Apple M2 Pro 10cores/16gpu, 16GB      RAM, 512GB SSD, Pantalla 15.6', 15749900),
  (203, 'Portátil', 'Asus', 'Laptop ROG Zephyrus', 'Cpu Ryzen 7 6900HS, 24GB RAM, 2TB      SSD, Gráficos RTX-3060 6GB, Pantalla 15.6p', 8199000),
  (207, 'Portátil', 'HP', 'Laptop 14-fq1021la', 'Cpu AMD Ryzen 5, 12GB RAM, 256GB SSD,     Pantalla 14p, Wifi, Lan, 2 USB-C, HDMI', 1799000),
  (208, 'Portátil', 'Lenovo', 'Todo en uno', 'Cpu AMD Ryzen 7-5700U, 2TB SSD, 8GB RAM,     Pantalla 23.8", Wifi, Lan, 2 USB-C, HDMI', 4599000),
  (301, 'Tablet', 'Apple', 'iPad 10gen', 'Pantalla 10.9", USB, Wifi', 2799000),
  (302, 'Tablet', 'Amazon', 'Kindle Oasis 10gen', '32Gb, Pantalla 7p, USB-C, Wifi',        1390000),
  (304, 'Tablet', 'Huawei', 'MatePad SE 10.1"', '128GB, Pantalla 10.1p 2K, USB-C, Wifi',   931000)
  ]

cursor.executemany("""
INSERT INTO productos VALUES (?, ?, ?, ?, ?, ?);
""", datos)

conexion.commit()
conexion.close()