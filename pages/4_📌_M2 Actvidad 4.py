import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 4")

st.header("Descripción de la actividad")
st.markdown("""
Esta actividad es una introducción práctica al uso de Python con DataFrames utilizando pandas y Streamlit.
Exploraremos cómo seleccionar, filtrar y modificar datos usando métodos como `.loc` y `.iloc`.
""")

# Objetivos
st.header("Objetivos de aprendizaje")
st.markdown("""
- Comprender cómo manipular datos con pandas.
- Aplicar los métodos `.loc` y `.iloc` para acceder a datos.
- Realizar filtros condicionales en DataFrames.
- Modificar valores dentro de un DataFrame de forma interactiva.
""")

# Solución
st.header("Solución")
st.markdown("""
En esta sección interactuaremos con un DataFrame que contiene información de personas.
Aprenderás cómo acceder a sus datos, filtrarlos y modificarlos dinámicamente desde la interfaz.
""")

# Crear datos para el DataFrame
informacion = {
    'Nombre': ['Ana', 'Bob', 'Clara', 'David', 'Emma'],
    'Edad': [25, 30, 22, 35, 28],
    'Ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Valencia', 'Bilbao'],
    'Puntuación': [85, 90, 88, 92, 87]
}

# Crear el DataFrame
df_datos = pd.DataFrame(informacion, index=['a', 'b', 'c', 'd', 'e'])

# Título y descripción
st.title("Interacción con DataFrame usando .loc y .iloc")
st.write("Aquí puedes seleccionar, filtrar y modificar datos de un DataFrame de manera interactiva.")

# Visualizar el DataFrame original
st.subheader("📊 Visualiza el DataFrame Original")
st.dataframe(df_datos)

# Uso de .loc
st.subheader("🔍 Selección con .loc")
indice = st.text_input("Introduce el índice de la fila (ej. 'a', 'b'):", value='a')
columnas = st.multiselect("Elige las columnas:", df_datos.columns.tolist(), default=['Nombre', 'Edad'])

if indice in df_datos.index:
    st.write("Resultado de df.loc[indice, columnas]:")
    st.write(df_datos.loc[indice, columnas])
else:
    st.warning("El índice proporcionado no está en el DataFrame.")

# Uso de .iloc
st.subheader("🔎 Selección con .iloc")
pos_fila = st.number_input("Número de fila (de 0 a 4):", min_value=0, max_value=4, step=1)
pos_columnas = st.multiselect("Elige las posiciones de las columnas (0:Nombre, 1:Edad, 2:Ciudad, 3:Puntuación):", [0, 1, 2, 3], default=[0, 1])

try:
    st.write("Resultado de df.iloc[pos_fila, pos_columnas]:")
    st.write(df_datos.iloc[pos_fila, pos_columnas])
except Exception as e:
    st.error(f"Hubo un error al usar .iloc: {e}")

# Filtrado con condición
st.subheader("📌 Filtrado por condición con .loc")
edad_minima = st.slider("Edad mínima:", min_value=0, max_value=100, value=25)
df_filtrado = df_datos.loc[df_datos['Edad'] >= edad_minima]
st.write(f"Filas donde la Edad es >= {edad_minima}")
st.dataframe(df_filtrado)

# Modificar datos
st.subheader("✏ Modificar datos en el DataFrame")
fila_modificar = st.selectbox("Selecciona la fila a modificar (por índice):", df_datos.index)
columna_modificar = st.selectbox("Selecciona la columna a modificar:", df_datos.columns)
nuevo_valor = st.text_input(f"Introduce el nuevo valor para {columna_modificar} en la fila {fila_modificar}:")

if st.button("Actualizar valor"):
    try:
        df_datos.loc[fila_modificar, columna_modificar] = type(df_datos.loc[fila_modificar, columna_modificar])(nuevo_valor)
        st.success(f"Valor actualizado: {fila_modificar}, {columna_modificar} = {nuevo_valor}")
    except Exception as e:
        st.error(f"No se pudo actualizar el valor: {e}")

    # Mostrar DataFrame actualizado
    st.subheader("📋 DataFrame actualizado")
    st.dataframe(df_datos)
