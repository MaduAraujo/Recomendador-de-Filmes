import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('filmes.csv')
df['descricao'] = df['descricao'].fillna('')

vetorizar = TfidfVectorizer(stop_words=None)
matriz_tfidf = vetorizar.fit_transform(df['descricao'])

similaridade = cosine_similarity(matriz_tfidf, matriz_tfidf)

def recomendar_filmes(titulo, n=5):
    # Verifica se o título informado está na lista de filmes
    if titulo not in df['titulo'].values:
        print("Filme não encontrado.")  # Caso não encontre, exibe mensagem
        return  # Sai da função

    # Pega o índice do filme escolhido no DataFrame
    idx = df[df['titulo'] == titulo].index[0]

    # Cria uma lista com tuplas (índice, valor de similaridade) entre o filme escolhido e todos os outros
    scores = list(enumerate(similaridade[idx]))

    # Ordena a lista de scores da maior similaridade para a menor
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    # Seleciona os 'n' filmes mais semelhantes, ignorando o primeiro (que seria ele mesmo)
    scores = scores[1:n+1]

    # Exibe os filmes recomendados
    print(f"\nFilmes semelhantes a '{titulo}':")
    for i, score in scores:
        print(f"- {df.iloc[i]['titulo']} (similaridade: {score:.2f})")

recomendar_filmes("Matrix")