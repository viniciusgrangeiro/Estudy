import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# le os arquivos csv e armazenam em variaveis
df_reviews = pd.read_csv("../datasets/customer reviews.csv")
df_top100_books = pd.read_csv("../datasets/Top-100 Trending Books.csv")

# definindo quais sao so maiores e os menores valores de livtos
price_max = df_top100_books["book price"].max()
price_min = df_top100_books["book price"].min()

# barra de pesquisa de valor maximo dos livros
max_price = st.sidebar.slider("Price Range", price_min, price_max, price_max)

# exibe a tabela de livros, mas somente os livros com valores <= que o valor maximo preferido
df_books = df_top100_books[df_top100_books["book price"] <= max_price]

df_books
