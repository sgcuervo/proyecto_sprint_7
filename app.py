# Importamos librerias
import streamlit as st
import pandas as pd
import plotly.express as px

# Header
st.header("Analisis sobre la venta de automoviles en Estados Unidos")

# Importamos nuestro archivo csv
car_data = pd.read_csv("vehicles_us.csv")

# Definimos variables de entorno para cada grafico a utilizar
if "show_hist" not in st.session_state: # Histograma
    st.session_state.show_hist = False

if "show_scatter" not in st.session_state: # Grafico de dispersion
    st.session_state.show_scatter = False
    
if "show_box" not in st.session_state: # Diagrama de caja
    st.session_state.show_box = False
    

# Histograma
st.title("Histograma 'Odometro'")
st.write("Oprime el siguiente boton para generar un histograma que muestre la distribucion de kilometraje de los vehiculos")
hist_button = st.button("Mostrar/Ocultar histograma")

if hist_button:
    st.session_state.show_hist = not st.session_state.show_hist # Activamos nuestra variable de entorno al oprimir hist_button
    
# Creamos nuestro histograma
if st.session_state.show_hist:
    hist = px.histogram(car_data, x="odometer") 
    st.plotly_chart(hist, use_container_width=True)
    
    # Descripcion del grafico
    hist_check = st.checkbox("Mostrar informacion sobre el histograma")
    if hist_check:
        st.write("""
                  Distribución del kilometraje (Histograma):
                  Este gráfico muestra cómo se distribuyen los vehículos según su kilometraje. Permite identificar si la mayoría de los autos tienen poco uso o si predominan los vehículos con alto recorrido. 
                  Además, ayuda a detectar posibles valores atípicos y a entender la estructura general del mercado en términos de desgaste.
                  """)

# Grafico de dispersion
st.title("Grafico de dispersion (Precio vs kilometraje y condicion)")
st.write("Has click en el siguiente boton para generar un grafico de dispersion que nos muestre como cambia el costo de un vehiculo segun su uso y condicion")
scatter_button = st.button("Mostrar/Ocultar grafico de dispersion")

if scatter_button:
    st.session_state.show_scatter = not st.session_state.show_scatter # El boton activa nuestra variable de entorno
    
if st.session_state.show_scatter:
    sct = px.scatter(car_data, x="odometer", y="price", color="condition") # Creamos nuestro grafico de dispersion
    st.plotly_chart(sct, use_container_width=True)
    
    # Descripcion de nuestro grafico
    sct_check =st.checkbox("Mostrar informacion sobre el grafico de dispersion") 
    if sct_check:
        st.write("""
                 Relación entre kilometraje y precio (Grafico de dispersion):
                 Este gráfico analiza la relación entre el kilometraje y el precio de los vehículos, diferenciando por condición.
                 El uso de colores permite identificar cómo la condición del vehículo influye en esta relación
                 """
                 ) 

# Diagrama de caja
st.title("Diagrama de caja (Condicion vs precio)")
st.write("Has click en el siguiente boton para generar un diagrama de caja que nos muestre la distribucion de precios segun la condicion del vehiculo")
box_button = st.button("Mostrar/Ocultar diagrama de caja")

if box_button:
    st.session_state.show_box = not st.session_state.show_box # Agregamos la variable de entorno al hacer click en nuestro boton
    
if st.session_state.show_box:
    box = px.box(car_data, x="condition", y="price") # Creamos nuestro diagrama de caja
    st.plotly_chart(box, use_container_width=True)
    
    # Informacion sobre el diagrama de caja
    box_check =st.checkbox("Mostrar informacion sobre el diagrama de caja")
    if box_check:
        st.write("""
                 Comparación de precios según condición (Diagrama de caja):
                 Este gráfico compara la distribución de precios entre las distintas categorías de condición del vehículo. 
                 Permite observar diferencias en la mediana, la dispersión y la presencia de valores atípicos. 
                 Se aprecia que las categorías con mejor estado presentan precios medianos más elevados, lo que confirma que la condición es un factor relevante en la determinación del valor de mercado.
                 """
                 )




