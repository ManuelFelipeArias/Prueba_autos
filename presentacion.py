import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt

st.title('Análisis de Ventas de Vehículos')

# Cargar bases de datos
df_vehiculos = pd.read_csv('DB_2.csv')  
df_customer = pd.read_csv('df_customer.csv')

# Crear selector para filtrar por tipo de vehículo
tipo = st.selectbox('Tipo de vehículo', ['Económico', 'Promedio', 'Caro'])

# Filtrar df_vehiculos según el tipo seleccionado
if tipo == 'Económico':
    df_vehiculos_filtrado = df_vehiculos[df_vehiculos['Price'] < 20000]
elif tipo == 'Promedio':
    df_vehiculos_filtrado = df_vehiculos[(df_vehiculos['Price'] >= 20000) & (df_vehiculos['Price'] < 40000)]
else:
    df_vehiculos_filtrado = df_vehiculos[df_vehiculos['Price'] >= 40000]

# Mostrar datos filtrados de vehículos
st.subheader('Datos de Vehículos Filtrados')
st.dataframe(df_vehiculos_filtrado)

# Filtrar df_customer por clusters 0 y 2
df_customer_filtrado = df_customer[df_customer['Cluster'].isin([0, 2])]

# Mostrar datos filtrados de clientes
st.subheader('Datos de Clientes Filtrados')
st.dataframe(df_customer_filtrado)

# Lista de variables numéricas
numeric_cols = ['Price', 'Mileage', 'Engine volume', 'Cylinders'] 

# Lista de variables categóricas
cat_cols = ['Fuel type', 'Gear box type', 'Manufacturer', 'Category']

# Selector de variable para gráfico
var = st.selectbox('Selecciona variable para graficar', numeric_cols + cat_cols)

# Determinar tipo de gráfico según variable
if var in numeric_cols:
    # Histogramas para variables numéricas
    fig = plt.hist(df_customer_filtrado[var]) 
else:
    # Barras para variables categóricas
    fig = plt.bar(df_vehiculos_filtrado[var].value_counts().index, df_vehiculos_filtrado[var].value_counts().values)
    
st.pyplot(fig)