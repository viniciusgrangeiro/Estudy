import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# le os arquivos csv e armazenam em variaveis
df_reviews = pd.read_csv("../datasets/customer reviews.csv")
df_top100_books = pd.read_csv("../datasets/Top-100 Trending Books.csv")

# cria uma lista com os nomes dos livros sem repeti-los
books = df_top100_books["book title"].unique()

# cria uma selectbox com os nomes dos livros e armazena o livro selecionado na variavel "book"
book = st.sidebar.selectbox("Book", books)

# exibe os dados do livro selecionado da selectbox
df_book = df_top100_books[df_top100_books["book title"]== book]
df_review_f = df_reviews[df_reviews["book name"]== book]

# setando algumas variaves com base nas informacoes dos livros

# iloc[0] esta pegando apenas o nome do livro e descartando
# outras informacoes como o indice dele na tabela e o tipo de
# dado. ex: 1 The Woman in Me Name: book title, dtype: object
book_title = df_book["book title"].iloc[0]
book_genre = df_book["genre"].iloc[0]
book_price = f"${df_book['book price'].iloc[0]}"
book_rating = df_book["rating"].iloc[0]
book_year = df_book["year of publication"].iloc[0]

st.title(book_title)
st.subheader(book_genre)
col1, col2, col3 = st.columns(3)
col1.metric("Price", book_price)
col2.metric("Rating", book_rating)
col3.metric("Year of Publication", book_year)

# cria uma linha de divisao de conteudo
st.divider()

# seleciona cada linha da tabela e "row" recebe um valor
# em formato de lista e contem indices, tais quais seriam
# o titulo da resenha, o autor e etc
for row in df_review_f.values:
    # chat_message é usado para estilizar o texto
    message = st.chat_message(f"{row[4]}")
    message.write(f"**{row[2]}**")
    st.write(row[5])
