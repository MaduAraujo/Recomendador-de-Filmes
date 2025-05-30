# Prática de Data Science: Algoritmo de Recomendação

## 📌 O que são Sistemas de Recomendação?

Sistemas de recomendação são tecnologias projetadas para sugerir itens relevantes aos usuários com base em seus interesses, comportamentos e preferências anteriores. 
Eles são amplamente utilizados em plataformas digitais para personalizar a experiência do usuário e aumentar o engajamento com produtos ou conteúdos.

### Exemplos populares:

- 🎬 **Netflix** recomenda filmes e séries com base no que você já assistiu.
- 🛒 **Amazon** sugere produtos com base nas suas compras e visualizações anteriores.
- 🎵 **Spotify** cria playlists personalizadas com músicas semelhantes às que você costuma ouvir.

## 🔍 Tipos Comuns de Sistemas de Recomendação

Existem diversos métodos para realizar recomendações, mas os dois mais comuns são:

### 🧠 1. Sistema de Recomendação **Baseado em Conteúdo** (Content-Based)

#### ✅ Como funciona:

Este tipo de sistema analisa **as características dos itens** que o usuário já consumiu ou avaliou positivamente. A ideia é recomendar **outros itens com atributos semelhantes**.

#### 📚 Exemplo prático:

Se você assistiu a vários filmes de ficção científica no Netflix, o sistema vai procurar **outros filmes com o mesmo gênero, diretor, atores ou temas semelhantes** para recomendar.

#### 🛠️ Técnicas usadas:

- **Extração de características** (ex: gênero, duração, autor, palavras-chave).
- **Representação vetorial** dos itens (TF-IDF, embeddings, etc.).
- **Cálculo de similaridade** (Cosine Similarity, Distância Euclidiana).

#### 🎯 Vantagens:

- Não precisa de muitos dados de outros usuários.
- Funciona bem mesmo com poucos usuários (cold start para usuários).

#### ⚠️ Limitações:

- Pode ser limitado a um universo restrito de itens.
- Pode sofrer com a “bolha de filtro” (recomenda sempre mais do mesmo).

---

### 👥 2. Sistema de Recomendação **Baseado em Usuários** (Collaborative Filtering)

#### ✅ Como funciona:

Este método compara **usuários entre si**. Ele identifica padrões de comportamento e preferências entre usuários semelhantes, e recomenda o que **usuários parecidos com você gostaram**, mesmo que os itens recomendados sejam bem diferentes dos que você já consumiu.

#### 📚 Exemplo prático:

Se você e outro usuário têm gostos muito parecidos e ele gostou de uma série que você ainda não viu, o sistema pode recomendar essa série para você.

#### 🛠️ Técnicas usadas:

- **Filtragem Colaborativa baseada em usuários** (User-User).
- **Filtragem Colaborativa baseada em itens** (Item-Item).
- **Matriz de usuários x itens** com avaliações, visualizações, curtidas etc.
- **Fatoração de matrizes** (ex: SVD) para descobrir relações latentes.

#### 🎯 Vantagens:

- Capta preferências mais amplas e diversas.
- Pode sugerir itens fora do padrão do usuário, com boas chances de aceitação.

#### ⚠️ Limitações:

- Problemas com usuários ou itens novos (cold start).
- Necessita de muitos dados de comportamento de usuários.

---

### 🧠 TF-IDF e Similaridade Cosseno

TF-IDF (Term Frequency - Inverse Document Frequency)
<br> 👉 É uma técnica que transforma textos em números.

#### Como funciona?
Ela dá mais importância para palavras que são frequentes em um filme, mas não muito comuns em todos os filmes.

#### Por que isso é útil?
Assim conseguimos saber quais palavras são mais importantes para descrever cada filme.
<br> Por exemplo, se a palavra "anel" aparece muito em "Senhor dos Anéis", ela vai ter um peso maior ali.

### Similaridade Cosseno
👉 Depois que transformamos os textos em números, queremos saber **quais filmes são parecidos**.

#### Como funciona?
Imaginamos que cada filme é uma "seta" (ou vetor) apontando para algum lugar em um espaço.
<br> A **Similaridade Cosseno** mede o **ângulo** entre duas setas:
    
- Se o ângulo é **pequeno**, os filmes são **bem parecidos**.
- Se o ângulo é **grande**, eles são **bem diferentes**.

#### Por que usamos isso?
Porque é uma forma matemática de comparar os textos, mesmo que eles tenham tamanhos diferentes.

#### Resumindo:

1. **TF-IDF**: transforma o texto em números, destacando as palavras importantes.
2. **Similaridade Cosseno**: compara esses números para ver **quais textos (filmes) são parecidos**.

## 📊 Comparação Rápida

Esta tabela apresenta uma comparação rápida entre dois tipos principais de sistemas de recomendação: **Baseado em Conteúdo** e **Baseado em Usuários**.

| Característica              | Baseado em Conteúdo              | Baseado em Usuários             |
| :-------------------------- | :------------------------------- | :------------------------------ |
| **Fonte da recomendação** | Características dos itens        | Preferências de usuários        |
| **Requer dados de outros?** | Não                              | Sim                             |
| **Lida bem com novos usuários** | Sim                              | Não                             |
| **Lida bem com novos itens** | Não                              | Sim                             |
| **Risco de repetição** | Alto (itens muito parecidos)     | Menor (itens variados)          |

## 💡Conclusão

Sistemas de recomendação são fundamentais na era digital, atuando como guias personalizados que ajudam usuários a descobrir novos conteúdos com base em suas preferências e comportamentos. 
Plataformas como Netflix, Amazon e Spotify se tornaram referência ao combinar diferentes abordagens para oferecer experiências altamente personalizadas.
O conhecimento sobre essas técnicas é essencial para quem trabalha com ciência de dados, inteligência artificial, análise de comportamento do consumidor e desenvolvimento de plataformas digitais.
