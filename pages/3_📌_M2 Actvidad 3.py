import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 3")

st.header("Descripción de la actividad")
st.markdown("""
En esta actividad, trabajaremos con filtros dinámicos aplicados a un conjunto de datos que simula información
de personas residentes en distintas ciudades de Colombia. Usaremos Streamlit para construir una interfaz interactiva
que permita filtrar los datos según varios criterios.
""")

# ---------- Objetivos ----------
st.header("Objetivos de aprendizaje")
st.markdown("""
- Aplicar filtros dinámicos a un DataFrame.
- Comprender cómo usar widgets de Streamlit para controlar los datos.
- Visualizar los efectos de los filtros en tiempo real.
""")

# ---------- Datos ficticios ----------
st.header("Solución")
st.markdown("A continuación, se crea un DataFrame con información de ejemplo para aplicar los filtros:")

# Crear un DataFrame ficticio
informacion = {
    'Nombre': ['Ana', 'Bob', 'Clara', 'David', 'Emma'],
    'Edad': [25, 30, 22, 35, 28],
    'Municipio': ['Barranquilla', 'Santa Marta', 'Cartagena', 'Bogotá', 'Medellín'],
    'Ingreso_mensual': [1500000, 2500000, 3000000, 4500000, 1800000],
    'Ocupacion': ['Estudiante', 'Comerciante', 'Ingeniero', 'Docente', 'Emprendedor'],
    'Tipo_vivienda': ['Alquiler', 'Propia', 'Alquiler', 'Propia', 'Alquiler'],
    'Acceso_internet': [True, False, True, True, False],
    'Fecha_nacimiento': pd.to_datetime(['1999-01-01', '1985-06-15', '2000-02-28', '1990-11-11', '1997-07-24'])
}

df_nuevo = pd.DataFrame(informacion)

# Título
st.title("Aplicación de Filtros Dinámicos")

# Filtro por rango de edad
st.sidebar.subheader("1. Filtro por rango de edad")
activar_edad = st.sidebar.checkbox("Filtrar por rango de edad")
if activar_edad:
    min_edad = st.sidebar.slider("Edad mínima", 15, 75, 20)
    max_edad = st.sidebar.slider("Edad máxima", 15, 75, 40)
    df_nuevo = df_nuevo[df_nuevo['Edad'].between(min_edad, max_edad)]
    st.write("Datos filtrados por edad:", df_nuevo)

# Filtro por municipios específicos
st.sidebar.subheader("2. Filtro por municipios")
activar_municipios = st.sidebar.checkbox("Filtrar por municipios")
if activar_municipios:
    municipios_seleccionados = st.sidebar.multiselect(
        "Selecciona los municipios:", 
        ['Barranquilla', 'Santa Marta', 'Cartagena', 'Bogotá', 'Medellín', 'Tunja', 'Manizales', 'Cali', 'Quibdó', 'Buenaventura', 'Villavicencio', 'Yopal', 'Leticia', 'Puerto Inírida'],
        default=['Barranquilla', 'Santa Marta']
    )
    df_nuevo = df_nuevo[df_nuevo['Municipio'].isin(municipios_seleccionados)]
    st.write("Datos filtrados por municipio:", df_nuevo)

# Filtro por ingreso mensual mínimo
st.sidebar.subheader("3. Filtro por ingreso mensual mínimo")
activar_ingreso = st.sidebar.checkbox("Filtrar por ingreso mensual mínimo")
if activar_ingreso:
    ingreso_minimo = st.sidebar.slider("Ingreso mínimo (COP)", 800000, 12000000, 1500000)
    df_nuevo = df_nuevo[df_nuevo['Ingreso_mensual'] > ingreso_minimo]
    st.write("Datos filtrados por ingreso mensual mínimo:", df_nuevo)

# Filtro por ocupación
st.sidebar.subheader("4. Filtro por ocupación")
activar_ocupacion = st.sidebar.checkbox("Filtrar por ocupación")
if activar_ocupacion:
    ocupaciones_seleccionadas = st.sidebar.multiselect(
        "Selecciona las ocupaciones:", 
        ['Estudiante', 'Docente', 'Comerciante', 'Agricultor', 'Ingeniero', 'Médico', 'Desempleado', 'Pensionado', 'Emprendedor', 'Obrero'],
        default=['Estudiante', 'Docente']
    )
    df_nuevo = df_nuevo[df_nuevo['Ocupacion'].isin(ocupaciones_seleccionadas)]
    st.write("Datos filtrados por ocupación:", df_nuevo)

# Mostrar el DataFrame resultante
st.subheader("📊 DataFrame filtrado")
st.write(df_nuevo)

#-----------------------------------
#-----------------------------------
#-----------------------------------
#-----------------------------------
#-----------------------------------
<<<<<<< HEAD
"LINK DEL COLAB CON LOS 50 EJERCICIOS"
=======
LINK DEL COLAB CON LOS 50 EJERCICIOS
>>>>>>> dce2ea3699bfe09d71b97e139c6f421b5230f3fc
"https://colab.research.google.com/drive/1qGRiJMgOvMzQ5G10lA32hPXuch8n3CxT?usp=sharing"
#-----------------------------------
#-----------------------------------
#-----------------------------------
#-----------------------------------
#-----------------------------------
