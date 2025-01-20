import streamlit as st
import pandas as pd
import plotly_express as px

df = pd.read_csv('vehicles_us.csv')
print(df.head())
print(df.info())

#Correcion de datos incorrectos
df['model_year'] = df['model_year'].fillna(0).astype(int)

df['cylinders'] = df['cylinders'].fillna(0).astype(int)

df['paint_color'] = df['paint_color'].fillna('unknown')

df['odometer'] = df['odometer'].fillna(0)

df['is_4wd'] = df['is_4wd'].fillna(0).astype(int)

df['date_posted'] = pd.to_datetime(df['date_posted'], format='%Y-%m-%d')

print(df.info())

hist_button = st.button('Construir histogramas exploratorios')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de histogramas para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    odometer_data = df[df['odometer'] != 0]
    fig = px.histogram(odometer_data, x="odometer", range_x=[0, 400000])

    price_data = df[df['price'] < 100000]
    fig1 = px.histogram(price_data, x="price", range_x=[0, 40000])

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
#%%
scatt_button = st.button('Construir graficas de dispersion exploratorios')  # crear un botón

if scatt_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de graficas de dispersion exploratorios del conjunto de datos')

    fig = px.scatter(df, x="condition", y="price")  # crear un gráfico de dispersión
    fig1 = px.scatter(df[df['model_year'] != 0], x="model_year", y="price",
                     trendline='ols')  # crear un gráfico de dispersión
    fig2 = px.scatter(df, x="odometer", y="price", trendline='ols')  # crear un gráfico de dispersión

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

#%%
bar_button = st.button('Construir graficas de barras')  # crear un botón

if bar_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de graficas de barras exploratorios del conjunto de datos')

    model_data = df[df['model'] != 'unknown']
    model_count = model_data['model'].value_counts()
    model_count = model_count.reset_index()
    print(model_count)
    fig = px.bar(model_count.head(30), x="model", y='count', color="model")

    paint_data = df[df['paint_color'] != 'unknown']
    paint_count = paint_data['paint_color'].value_counts()
    paint_count = paint_count.reset_index()
    print(paint_count)
    fig1 = px.bar(paint_count.head(30), x="paint_color", y='count', color="paint_color")


    state_data = df[df['condition'] != 'unknown']
    state_count = state_data['condition'].value_counts()
    state_count = state_count.reset_index()
    print(state_count)
    fig2 = px.bar(state_count.head(30), x="condition", y='count', color="condition")


    year_data = df[df['model_year'] != '0']
    year_count = year_data['model_year'].value_counts()
    year_count = year_count.reset_index()
    year_count.drop(index=0, inplace=True)
    print(year_count)
    fig3 = px.bar(year_count.head(30), x="model_year", y='count', color="model_year")


    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

