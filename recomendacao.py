import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st
import io # Não usado, mas inofensivo.

# --- 1. CONFIGURAÇÃO DA PÁGINA (DEVE SER O PRIMEIRO COMANDO STREAMLIT) ---
st.set_page_config(page_title="Sistema de Recomendação de Filmes", layout="centered", page_icon="🎬")

# --- 2. CARREGAR E PREPARAR DADOS ---
@st.cache_data
def load_data():
    """Carrega os dados dos filmes de um arquivo CSV."""
    try:
        movies_df = pd.read_csv('movies.csv')
    except FileNotFoundError:
        st.error("O arquivo 'movies.csv' não foi encontrado. Por favor, baixe o dataset MovieLens (ml-latest-small) e coloque 'movies.csv' na mesma pasta deste script.")
        st.stop() # Interrompe a execução do aplicativo se o arquivo não for encontrado.
    movies_df['genres'] = movies_df['genres'].fillna('') # Preenche valores nulos em 'genres' com string vazia
    return movies_df

# Chamada da função para carregar os dados
movies_df = load_data()

# --- 3. VETORIZAÇÃO TF-IDF E SIMILARIDADE DE COSSENO ---
@st.cache_resource
def train_model(data_df):
    """Treina o modelo TF-IDF e calcula a similaridade de cosseno."""
    # Usando um tokenizador customizado para gêneros separados por '|'
    tfidf_vectorizer = TfidfVectorizer(stop_words=None, tokenizer=lambda x: x.split('|'))
    tfidf_matrix = tfidf_vectorizer.fit_transform(data_df['genres'])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    return tfidf_vectorizer, tfidf_matrix, cosine_sim

# Chamada da função para treinar o modelo
tfidf_vectorizer, tfidf_matrix, cosine_sim = train_model(movies_df)

# --- 4. FUNÇÃO DE RECOMENDAÇÃO ---
def recommend_movies(title, n=5):
    # Tenta encontrar uma correspondência exata primeiro para priorizar a precisão
    exact_match_movie = movies_df[movies_df['title'] == title]

    if not exact_match_movie.empty:
        idx = exact_match_movie.index[0]
    else:
        # Se não houver correspondência exata, tenta correspondência parcial
        matching_movies = movies_df[movies_df['title'].str.contains(title, case=False, na=False)]
        if matching_movies.empty:
            return None, "Filme não encontrado. Por favor, verifique a grafia ou tente outro título."
        # Se houver várias correspondências parciais, pega a primeira
        idx = matching_movies.index[0]

    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Exclui o próprio filme das recomendações
    sim_scores = sim_scores[1:n+1] # Pega as top N recomendações

    recommended_movies = []
    for i, score in sim_scores:
        recommended_movies.append({'title': movies_df.iloc[i]['title'], 'similarity': score})

    return recommended_movies, None

# --- 5. INTERFACE DO APLICATIVO STREAMLIT ---
st.title("🎬 Sistema de Recomendação de Filmes")

st.markdown("""
    Bem-vindo ao sistema de recomendação de filmes!
    Digite o nome de um filme e receba recomendações de filmes semelhantes baseados em seus gêneros.
""")

movie_input = st.text_input("Digite o nome do filme:", "")

if st.button("Recomendar Filmes"):
    if movie_input:
        with st.spinner("Buscando recomendações..."):
            recommendations, error_message = recommend_movies(movie_input)

            if error_message:
                st.error(error_message)
            elif recommendations:
                st.subheader(f"Filmes semelhantes a '{movie_input}':")
                for rec in recommendations:
                    st.write(f"- **{rec['title']}** (Similaridade: {rec['similarity']:.2f})")
            else:
                st.info("Nenhuma recomendação encontrada para este filme. Tente outro!")
    else:
        st.warning("Por favor, digite o nome de um filme para obter recomendações.")

### **Sobre o Projeto**

st.sidebar.header("Sobre o Projeto")
st.sidebar.info(
    "Este projeto é um sistema de recomendação de filmes baseado em conteúdo, desenvolvido com o objetivo de oferecer "
    "sugestões personalizadas aos usuários. Ele analisa características dos filmes que você gostou "
    "(como título e gênero) para encontrar outros filmes com perfis semelhantes."
)
st.sidebar.header("Repositório do Projeto")
st.sidebar.info(
    "O código-fonte completo e mais detalhes sobre a implementação podem ser encontrados no repositório do GitHub."
)
st.sidebar.markdown("[**GitHub**](https://github.com/MaduAraujo/Recomendador-de-Filmes)")