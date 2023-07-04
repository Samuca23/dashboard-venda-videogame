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

    return df

df = importa_dado()