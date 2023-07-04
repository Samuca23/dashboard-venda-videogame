import streamlit as st
import pandas as pd
import collections
import plotly.exceptions as px

#Importação/Manipulação dos dados
def importa_dado():
    df = pd.read_csv("vgsales.csv")
    # Remover os valores ausentes
    df = df.dropna()
    df = df[df['Year'] <= 2016]
    df['Year'] = df['Year'].astype(int)
    plataformas = ['Wii', 'PS2', 'PC', 'XOne', 'PS4']
    filtro = df['Platform'].isin(plataformas)

    return df[filtro]

df = importa_dado()

#Configurações iniciais
st.set_page_config(page_title="📊 Dashboard Games", layout="wide")
st.markdown("<h1 style='text-align: center;'>📊 Dashboard Games</h1>", unsafe_allow_html=True)
st.markdown('---')

#Sidebar
st.sidebar.header("Informe o filtro")
plataforma = st.sidebar.multiselect(
    "Selecione a plataforma",
    options=df["Platform"].unique(),
    default=df["Platform"].unique()
)

genero = st.sidebar.multiselect(
    "Selecione a gênero",
    options=df["Genre"].unique(),
    default=df["Genre"].unique()
)

df_selecao = df.query(
    "Platform == @plataforma & Genre == @genero"
)

#Remove estilo Streamlit
remove_st_estilo = """
    <style>
        #MainMenu {visibility: hidden}
        footer {visibility: hidden}
        header {visibility: hidden}
    </style>
"""
st.markdown(remove_st_estilo, unsafe_allow_html=True)