# Debe direccionar VS Code a la carpeta con los archivos:
# 1.- Archivo
# 2.- Abrir carpeta. Debe dar click en la carpeta que contiene los archivos de interés
#3.- A la izquierda, en el explorador deberá poder visualizar todos los archivos
#------------------------------------------------------------------------------------------------

# CÓDIGO STREAMLIT
# Ir a:   Ver/Terminal
# Crea un ambiente virtual (puedes usar otro nombre en lugar de 'venv'): coloca este código
#   python -m venv venv

#---------------------------------------------------------------------------------------
# Luego de crear el ambiente virtual, lo activas
#   .\venv\Scripts\activate   # En Windows
#---------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------
# Cuando vuelva a iniciar sesión, debe volver a activar el ambiente virtual, ya no lo debe crear.
# En este caso debes abrir la carpeta con los archivos del caso.
#---------------------------------------------------------------------------------------------


# Instala la versión específica de scikit-learn
#   pip install scikit-learn==1.2.2
# Instala otras dependencias, incluyendo Streamlit
#  pip install streamlit pandas joblib
#-------------------------------------------------------------------------------------------------
# Desde la segunda vez: hacer:
# Si da error, debes ir a PowerShell de Window y:
#      Get-ExecutionPolicy                           Si es Restricted; ejecuta
#      Set-ExecutionPolicy RemoteSigned              Colocar Sí
# En consola de VSC:  .\venv\Scripts\activate


import streamlit as st
import pandas as pd
from joblib import load

# Cargar el modelo entrenado con dataset de casas
regressor = load('Modelopipeline.joblib')

# Inicializar variables
size = bedrooms = bathrooms = distance = 0.0
selected_city = "Lima"

# UI
st.title("Modelo de Regresión - Precio de Casas 🏠")
st.markdown("##### Ingresa los datos de la casa para predecir su precio")

# Sidebar
st.sidebar.header("Campos a Evaluar")

# Inputs
size = st.sidebar.number_input("**Size (m²)**", min_value=0.0, value=2000.0)
bedrooms = st.sidebar.number_input("**Bedrooms**", min_value=0, value=3)
bathrooms = st.sidebar.number_input("**Bathrooms**", min_value=0, value=2)
distance = st.sidebar.number_input("**Distance to Center (km)**", min_value=0.0, value=5.0)

# Ciudad
st.sidebar.markdown("<h1 style='font-size: 24px;'>City</h1>", unsafe_allow_html=True)
selected_city = st.sidebar.selectbox(
    "Select City",
    ["Lima", "Arequipa", "Trujillo"],
    index=["Lima", "Arequipa", "Trujillo"].index(selected_city)
)

# Reset
def reset_inputs():
    global size, bedrooms, bathrooms, distance, selected_city
    size = bedrooms = bathrooms = distance = 0.0
    selected_city = "Lima"

# Botón predecir
if st.sidebar.button("Predecir"):

    if all(val >= 0 for val in [size, bedrooms, bathrooms, distance]):

        # DataFrame (CLAVE 🔥)
        obs = pd.DataFrame({
            'Size': [size],
            'Bedrooms': [bedrooms],
            'Bathrooms': [bathrooms],
            'Distance_to_Center': [distance],
            'City': [selected_city]
        })

        # Debug
        st.write("DataFrame de entrada:")
        st.write(obs)

        # Predicción
        target = regressor.predict(obs)

        st.markdown(
            f'<p style="font-size: 40px; color: green;">Precio estimado: ${target[0]:,.2f}</p>',
            unsafe_allow_html=True
        )

    else:
        st.warning("Valores inválidos")

# Reset botón
if st.sidebar.button("Resetear"):
    reset_inputs()



#   R&D Spend	Administration	Marketing Spend  Ciudad  
#	  142107.34  	91391.77	366168.42         Florida    ---->

# Cambiar los valores.
# Para asignar valores: ver los rangos de las cuantitativas ( MÍNIMO --MÁXIMO)
# eso determinan  cómo predice el modelo. 

#  streamlit run streamlitpipelines.py       en la consola
#  pip freeze > requirements.txt