import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Análisis de Ventas de Vehículos')

st.header('Resumen Ejecutivo')
st.write("""
- Se analizaron las bases de datos de clientes y vehículos.
- Se construyeron modelos predictivos de compra de vehículos y precios.
- Se logró un accuracy de 82% en el modelo de compra de vehículos. 
- El error cuadrático medio del modelo de precios fue de 47435983.
""")

st.header('Insights Clave')
insights = [
    "- Los clientes de 30-50 años son los más propensos a comprar vehículos.",
    "- El precio se ve impactado principalmente por características como tamaño del motor y tipo de vehículo.",
    "- Los modelos SUV y Pickup tienen mayor demanda que los Sedan."
]

for insight in insights:
    st.markdown(insight)

st.header('Modelos Predictivos')

# Cargar datos de ejemplo
df_ventas = pd.DataFrame(
    [[20, 1000, 'SUV', 'NY'], 
     [31, 2000, 'Sedan', 'CA'],
     [18, 500, 'Hatchback', 'FL']], 
     columns=['Edad', 'Ingresos', 'TipoVehiculo', 'Estado']) 

c = st.container()
col1, col2 = c.columns(2)

# Gráfica modelo de ventas 
with col1:
    fig, ax = plt.subplots()
    ax.bar(df_ventas['TipoVehiculo'], df_ventas['Ingresos'])
    st.write(fig)

# Métricas modelo de precios
with col2:
    st.metric(label="MSE", value="47435983", delta="10%")
    st.metric(label="MAE", value="5000", delta="5%")
    
st.markdown('---')
st.subheader('Recomendaciones')
st.write(
    """- Lanzar campañas enfocadas en clientes de 30 a 50 años.
    - Aumentar inventario de vehículos SUV y Pickup.
    - Explorar partnership con proveedores de autopartes para reducir costos.
    """
)