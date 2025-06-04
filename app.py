import streamlit as st
import pandas as pd
import plotly.express as px

# Leer el archivo CSV
df = pd.read_csv("vehicles_us.csv")

# Encabezado principal
st.header("Análisis de Anuncios de Vehículos en Venta")

# Casilla para mostrar histograma del odómetro
build_histogram = st.checkbox("Mostrar histograma del odómetro")

if build_histogram:
    st.write("Distribución del kilometraje (odómetro):")
    fig = px.histogram(df, x="odometer")
    st.plotly_chart(fig)

# Casilla para mostrar gráfico de dispersión
build_scatter = st.checkbox("Mostrar gráfico de dispersión (odómetro vs precio)")

if build_scatter:
    st.write("Relación entre kilometraje y precio:")
    fig = px.scatter(df, x="odometer", y="price", color="condition")
    st.plotly_chart(fig)

