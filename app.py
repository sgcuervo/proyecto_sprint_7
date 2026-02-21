import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Analisis sobre la venta de automoviles en Estados Unidos")

car_data = pd.read_csv("~/GITS/Tripleten/proyecto_sprint_7/vehicles_us.csv")

st.title("Histograma 'Odometro'")
st.write("Oprime el siguiente boton para generar un histograma que muestre la distribucion de kilometraje de los vehiculos")
hist_button = st.button("Generar")

if hist_button:
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

    hist_check = st.checkbox("¿Que estoy viendo?")
    
    if hist_check:
    st.write("informacion")

