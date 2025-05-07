import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 2")

st.header("Descripción de la actividad")
st.markdown("""
En esta actividad exploraremos un conjunto de datos de estudiantes colombianos utilizando la biblioteca Pandas.
A través de este ejercicio, aprenderemos a cargar archivos CSV, visualizar datos, aplicar filtros y generar estadísticas
descriptivas de manera interactiva con Streamlit.
""")

# ------------------------------
# Objetivos de aprendizaje
# ------------------------------
st.header("Objetivos de aprendizaje")
st.markdown("""
- Aprender a leer archivos CSV con pandas  
- Visualizar y explorar datos tabulares  
- Aplicar filtros dinámicos a columnas numéricas  
- Obtener estadísticas básicas de un conjunto de datos  
""")

# ------------------------------
# Solución
# ------------------------------
st.header("Solución")

# Se crea el archivo con los datos de estudiantes
df = pd.read_csv("estudiantes_colombia.csv")

st.title("📊 Exploración de Datos de Estudiantes")

# Ver las primeras 5 filas
st.subheader("🔹 Primeras 5 filas del dataset")
st.dataframe(df.head())

# Ver las últimas 5 filas
st.subheader("🔹 Últimas 5 filas del dataset")
st.dataframe(df.tail())

# Estadísticas descriptivas en el adata estudiantes
st.subheader("Estadísticas descriptivas")
st.write(df.describe())

# Selección de columnas específicas
st.subheader("🔹 Selección de columnas: nombre, edad, promedio")
columnas_seleccionadas = ["nombre", "edad", "promedio"]
st.dataframe(df[columnas_seleccionadas])

df = pd.read_csv("estudiantes_colombia.csv")

# Se realiza el menu interactivo para que el usuario pueda elegir entre las opciones

opcion = st.selectbox("¿Qué quieres explorar?", 
                    ["Estadísticas", "Filtrar por promedio"])

if opcion == "Estadísticas":
    st.subheader("Estadísticas descriptivas del dataset")
    st.write(df.describe())

elif opcion == "Filtrar por promedio":

    # Se crea un filtro para que el usuario pueda seleccionar el promedio mínimo

    promedio_min = st.selectbox("Selecciona el promedio mínimo:", [i/2 for i in range(10)])  
    st.subheader(f"Estudiantes con promedio mayor a {promedio_min}")
    
    filtro = df[df['promedio'] >= promedio_min]
    st.write(filtro)
