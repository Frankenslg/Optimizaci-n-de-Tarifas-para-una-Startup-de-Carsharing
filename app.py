import pandas as pd
import plotly.express as px
import streamlit as st

# Leer el archivo CSV en un DataFrame
car_data = pd.read_csv('vehicles_us.csv')

# Crear un encabezado para la aplicación
st.header('Cuadro de Mandos: Datos de Venta de Coches en USA')

# Crear un botón para el histograma
hist_button = st.button('Construir histograma')

# Crear un botón para el gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if hist_button:
    # Escribir un mensaje para el histograma
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear el histograma
    fig = px.histogram(car_data, x="odometer")

    # Mostrar el gráfico de histograma de Plotly
    st.plotly_chart(fig, use_container_width=True)

if scatter_button:
    # Escribir un mensaje para el gráfico de dispersión
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # Crear el gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price", title='Relación entre odómetro y precio')

    # Mostrar el gráfico de dispersión de Plotly
    st.plotly_chart(fig, use_container_width=True)
