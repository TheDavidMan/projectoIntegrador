import pandas as pd
import streamlit as st
import numpy as np
import openpyxl 
import sqlite3
import json

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 1")

st.header("Descripción de la actividad")
st.markdown("""
Esta actividad tiene como objetivo mostrar cómo trabajar con distintas fuentes de datos y crear DataFrames utilizando Pandas.
Exploraremos cómo cargar, manipular y mostrar datos desde diferentes formatos, como diccionarios, listas, CSV, Excel, JSON, URL, SQLite y NumPy.
""")

st.header("Objetivos de aprendizaje")

st.markdown("""
- Aprender a crear DataFrames a partir de diversas fuentes de datos
- Visualizar datos usando Streamlit
- Aplicar Pandas para manipulación de datos en Python
- Conocer las diferentes formas de cargar datos en un DataFrame
""")

st.header("Solución")

st.markdown("""
### 1. DataFrame desde Diccionario
Se crea un DataFrame a partir de un diccionario con información de libros, incluyendo título, autor, año de publicación y género.
""")


st.markdown("""
### 2. DataFrame desde Lista de Diccionarios
Se muestra cómo crear un DataFrame usando una lista de diccionarios con información sobre ciudades, incluyendo nombre, población y país.
""")


st.markdown("""
### 3. DataFrame desde Lista de Listas
Se crea un DataFrame usando una lista de listas con información sobre productos en inventario, incluyendo producto, precio y stock.
""")


st.markdown("""
### 4. DataFrame desde Series
Se utiliza Pandas Series para crear un DataFrame con información de personas, incluyendo nombre, edad y ciudad.
""")


st.markdown("""
### 5. DataFrame desde CSV
Se carga un archivo CSV para mostrar cómo se puede usar Pandas para leer y mostrar datos desde un archivo externo.
""")


st.markdown("""
### 6. DataFrame desde Excel
Se carga un archivo Excel en formato `.xlsx` y se visualiza su contenido en un DataFrame.
""")


st.markdown("""
### 7. DataFrame desde JSON
Se muestra cómo cargar datos desde un archivo JSON y convertirlos en un DataFrame.
""")


st.markdown("""
### 8. DataFrame desde URL
Se cargan datos desde una URL que contiene un archivo CSV y se convierte en un DataFrame.
""")


st.markdown("""
### 9. DataFrame desde SQLite
Se muestra cómo leer datos desde una base de datos SQLite y visualizarlos en un DataFrame.
""")


st.markdown("""
### 10. DataFrame desde NumPy
Se crea un DataFrame usando un array de NumPy y se muestra en la aplicación.
""")



st.header("Solución")


# Título y descripción
st.title("Actividad 1 - Creación de DataFrames")
st.write("Esta actividad tiene como objetivo mostrar cómo crear DataFrames con diferentes fuentes usando Pandas y visualizarlos con Streamlit.")

st.header("📘 DataFrame desde Diccionario")

# Creamos un diccionario con datos de libros
libros = {
    "Título": ["Cien años de soledad", "1984", "El principito", "Fahrenheit 451"],
    "Autor": ["Gabriel García Márquez", "George Orwell", "Antoine de Saint-Exupéry", "Ray Bradbury"],
    "Año de Publicación": [1967, 1949, 1943, 1953],
    "Género": ["Realismo mágico", "Distopía", "Fábula", "Ciencia ficción"]
}

# Convertimos el diccionario en un DataFrame
df_libros = pd.DataFrame(libros)

# Mostramos el DataFrame en la app
st.dataframe(df_libros)
# ----------------------------------
# 2. DataFrame desde Lista de Diccionarios
# ----------------------------------
st.header("Información de Ciudades")
ciudades = [
    {"nombre": "Lima", "población": 9500000, "país": "Perú"},
    {"nombre": "Buenos Aires", "población": 2890000, "país": "Argentina"},
    {"nombre": "Ciudad de México", "población": 9200000, "país": "México"},
    {"nombre": "Bogotá", "población": 7400000, "país": "Colombia"}
]
df_ciudades = pd.DataFrame(ciudades)
st.dataframe(df_ciudades)

# ----------------------------------
# 3. DataFrame desde Lista de Listas
# ----------------------------------
st.header("Productos en Inventario")
productos = [
    ["Mouse", 25.99, 150],
    ["Teclado", 45.00, 80],
    ["Monitor", 200.00, 30],
    ["USB", 10.50, 200]
]
df_productos = pd.DataFrame(productos, columns=["Producto", "Precio", "Stock"])
st.dataframe(df_productos)

# ----------------------------------
# 4. DataFrame desde Series
# ----------------------------------
st.header("Datos de Personas")
nombres = pd.Series(["Lucía", "Marcos", "Elena", "Tomás"])
edades = pd.Series([25, 30, 22, 28])
ciudades = pd.Series(["Lima", "Quito", "Bogotá", "Santiago"])
df_personas = pd.DataFrame({
    "Nombre": nombres,
    "Edad": edades,
    "Ciudad": ciudades
})
st.dataframe(df_personas)

# ----------------------------------
# 5. DataFrame desde CSV
# ----------------------------------
st.header("Datos desde CSV")
df_csv = pd.read_csv("data.csv")
st.dataframe(df_csv)

# ----------------------------------
# 6. DataFrame desde Excel
# ----------------------------------
st.header("Datos desde Excel")
df_excel = pd.read_excel("https://raw.githubusercontent.com/TheDavidMan/projectoIntegrador/main/data.xlsx", engine="openpyxl")
st.dataframe(df_excel)

# ----------------------------------
# 7. DataFrame desde JSON
# ----------------------------------
st.header("Datos de Usuarios desde JSON")
df_json = pd.read_json("data.json")
st.dataframe(df_json)

# ----------------------------------
# 8. DataFrame desde URL
# ----------------------------------
st.header("Datos desde URL")
url = "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv"
df_url = pd.read_csv(url)
st.dataframe(df_url)

# ----------------------------------
# 9. DataFrame desde SQLite
# ----------------------------------
st.header("Datos desde SQLite")

conn = sqlite3.connect("estudiantes.db")
cursor = conn.cursor()

# 2. Eliminar la tabla si existe (opcional, para que se cree de nuevo en cada ejecución)
cursor.execute("DROP TABLE IF EXISTS estudiantes")

# 3. Crear la tabla 'estudiantes' si no existe
cursor.execute("""
    CREATE TABLE estudiantes (
        nombre TEXT,
        calificacion REAL
    )
""")

# 4. Insertar datos en la tabla
cursor.execute("INSERT INTO estudiantes (nombre, calificacion) VALUES (?, ?)", ("Ana", 8.5))
cursor.execute("INSERT INTO estudiantes (nombre, calificacion) VALUES (?, ?)", ("Luis", 7.9))
cursor.execute("INSERT INTO estudiantes (nombre, calificacion) VALUES (?, ?)", ("Marta", 9.2))
cursor.execute("INSERT INTO estudiantes (nombre, calificacion) VALUES (?, ?)", ("Sofía", 9.0))
cursor.execute("INSERT INTO estudiantes (nombre, calificacion) VALUES (?, ?)", ("Andrés", 8.3))
cursor.execute("INSERT INTO estudiantes (nombre, calificacion) VALUES (?, ?)", ("Valentina", 9.5))

# 5. Hacer commit para guardar los cambios
conn.commit()

# 6. Usar Pandas para ejecutar una consulta SQL y cargar los resultados en un DataFrame
df = pd.read_sql("SELECT * FROM estudiantes", conn)

# 7. Cerrar la conexión (si ya no la necesitas más)
conn.close()

# 8. Mostrar el título y los datos en Streamlit
st.title("Datos desde SQLite")
st.dataframe(df)  # Muestra los datos en una tabla interactiva



# ----------------------------------
# 10. DataFrame desde NumPy
# ----------------------------------
st.header("Datos desde NumPy")
array = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
df_numpy = pd.DataFrame(array, columns=["Columna 1", "Columna 2", "Columna 3"])
st.dataframe(df_numpy)



