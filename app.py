import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv') 

# Título de la app
st.header('Cuadro de Mando de Anuncios de Coches')

# Crear casillas de verificación
build_histogram = st.checkbox('Construir un histograma')
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_histogram: # si la casilla está seleccionada
    st.write('Mostrando histograma del millaje de los coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if build_scatter: # si la otra casilla está seleccionada
    st.write('Mostrando gráfico de dispersión: Precio vs Millaje')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)