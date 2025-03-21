import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import scipy.stats as stats

# Configuração da página com um novo design
st.set_page_config(page_title="Dashboard Profissional", layout="wide")

# Customização do estilo
st.markdown(
    """
    <style>
        .big-font {font-size:24px !important;}
        .header {color: #3498db; text-align: center; font-weight: bold; padding: 10px;}
        .sidebar {background-color: #2c3e50; color: white; padding: 20px; border-radius: 10px;}
        .content {background-color: #ecf0f1; padding: 20px; border-radius: 10px;}
        .right-align {display: flex; justify-content: flex-end; align-items: center;}
    </style>
    """,
    unsafe_allow_html=True
)

# Criando o menu lateral interativo
st.sidebar.markdown("<div class='sidebar'><h2>Menu</h2></div>", unsafe_allow_html=True)
pages = st.sidebar.radio("Navegue pelo dashboard:", [
    "Quem sou eu?",
    "Formação e Experiência",
    "Skills",
    "Análise de Dados"
])

st.sidebar.markdown("### Desenvolvido por Vitor Pinheiro")

# Adicionando botões para LinkedIn e GitHub
st.sidebar.markdown("---")
st.sidebar.markdown("### Conecte-se comigo:")
if st.sidebar.button("LinkedIn", key="linkedin", help="Acesse meu perfil no LinkedIn"):
    st.sidebar.markdown("[Clique aqui](https://www.linkedin.com/in/vitor-nascimento-25796224a/) para acessar meu LinkedIn", unsafe_allow_html=True)

if st.sidebar.button("GitHub", key="github", help="Acesse meu repositório no GitHub"):
    st.sidebar.markdown("[Clique aqui](https://github.com/vitorpnascimento) para acessar meu GitHub", unsafe_allow_html=True)

# Seção "Quem sou eu?"
if pages == "Quem sou eu?":
    st.header("Quem sou eu?")
    st.image("eu.png.jpg", width=1300)
    st.write("""
    - Aluno da **Faculdade de Informática e Administração Paulista (FIAP)**, atualmente cursando **Engenharia de Software**.
    - Aberto a desenvolver as minhas habilidades nas mais variadas áreas do curso.
    - Com uma boa Sinergia na parte de gestão de pessoas.
    """)

# Seção "Formação e Experiência"
elif pages == "Formação e Experiência":
    st.header("Formação e Experiência Profissional")
    st.image("Fiap.png", width=1300)
    st.write("""
    - **Formação Acadêmica:**
        - Engenharia de Software na **FIAP** (Faculdade de Informática e Administração Paulista), atualmente no **4º semestre**.
        - Início em **2023**, com término previsto para **2027**.
    - **Experiência Profissional:**
        - Estágio na **KW do Brasil** como auxiliar.
        - Supervisor de vendas na **Sandals**.
    """)

# Seção "Skills"
elif pages == "Skills":
    st.header("Habilidades Técnicas e Pessoais")
    st.image("Teclando.png", width=1300)
    skill_type = st.selectbox("Selecione a categoria de skills:", ["Hard Skills", "Soft Skills"])
    
    if skill_type == "Hard Skills":
        st.write("""
        - **Especialização em design de sites e imagens**
        - **Experiência em Back-end e Front-end**
        - **Uso de inteligência artificial e modelagem 3D**
        - **Linguagens de programação:** Python, Java, JavaScript
        - **Banco de Dados:** MySQL, PostgreSQL
        - **Ferramentas:** Git, Docker, APIs REST
        """)
    else:
        st.write("""
        - **Gestão de grupos**
        - **Facilidade para criação de ideias**
        - **Boa conduta**
        """)
    
# Seção "Análise de Dados"
elif pages == "Análise de Dados":
    st.header("Análise de Dados")
    st.write("Nesta seção, apresentamos uma análise estatística das estatísticas de jogadores de futebol.")
    
    st.subheader("📌 Apresentação do Conjunto de Dados")
    st.write("""
    O conjunto de dados utilizado representa estatísticas de jogadores de futebol. Cada linha corresponde a um jogador e contém informações sobre sua posição, idade, número de gols, assistências, passes e minutos jogados.
    """)
    
    st.subheader("📌 Tipos de Variáveis")
    st.write("""
    - **Nome do Jogador**: Categórica Nominal
    - **Posição**: Categórica Nominal
    - **Idade**: Numérica Discreta
    - **Número de Gols**: Numérica Discreta
    - **Número de Assistências**: Numérica Discreta
    - **Número de Passes**: Numérica Discreta
    - **Minutos Jogados**: Numérica Contínua
    """)
    
    st.subheader("📌 Perguntas de Análise")
    st.write("""
    Algumas perguntas que analisaremos com este conjunto de dados:
    - Existe correlação entre **minutos jogados e número de gols**?
    - Como **a idade influencia no desempenho**?
    - A distribuição de **gols e assistências segue um padrão previsível**?
    """)
    
    uploaded_file = st.file_uploader("Carregue seu arquivo Excel com estatísticas de jogadores", type=["xlsx", "xls"])
    
    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        st.write("Amostra dos dados:", df.head())

                # Estatísticas descritivas
        st.subheader("📊 Estatísticas Descritivas")
        coluna = st.selectbox("Selecione uma coluna numérica para análise:", df.select_dtypes(include=np.number).columns)
        
        if coluna:
            media = df[coluna].mean()
            mediana = df[coluna].median()
            moda = df[coluna].mode().iloc[0]
            desvio = df[coluna].std()
            variancia = df[coluna].var()

            st.write(f"Média: {media:.2f}")
            st.write(f"Mediana: {mediana}")
            st.write(f"Moda: {moda}")
            st.write(f"Desvio padrão: {desvio:.2f}")
            st.write(f"Variância: {variancia:.2f}")

        # Gráfico de dispersão
        st.subheader("📈 Correlação entre Assistências e Gols")
        if "Número de Gols" in df.columns and "Número de Assistências" in df.columns:
            fig = px.scatter(df, x="Número de Assistências", y="Número de Gols",
                             title="Assistências vs Gols",
                             labels={"Número de Assistências": "Assistências", "Número de Gols": "Gols"},
                             trendline="ols")
            st.plotly_chart(fig)

        # Distribuição de Poisson - Gols
        st.subheader("🔢 Distribuição de Poisson - Gols")
        if "Número de Gols" in df.columns:
            media_gols = df["Número de Gols"].mean()
            x = np.arange(0, df["Número de Gols"].max() + 1)
            y = stats.poisson.pmf(x, media_gols)

            fig_poisson = go.Figure()
            fig_poisson.add_trace(go.Bar(x=x, y=y))
            fig_poisson.update_layout(title="Distribuição de Poisson - Número de Gols",
                                      xaxis_title="Gols",
                                      yaxis_title="Probabilidade")
            st.plotly_chart(fig_poisson)

        # Distribuição Normal - Minutos Jogados
        st.subheader("📊 Distribuição Normal - Minutos Jogados")
        if "Minutos Jogados" in df.columns:
            mu = df["Minutos Jogados"].mean()
            sigma = df["Minutos Jogados"].std()
            x = np.linspace(mu - 4*sigma, mu + 4*sigma, 100)
            y = stats.norm.pdf(x, mu, sigma)

            fig_normal = go.Figure()
            fig_normal.add_trace(go.Scatter(x=x, y=y, mode='lines'))
            fig_normal.update_layout(title="Distribuição Normal - Minutos Jogados",
                                     xaxis_title="Minutos",
                                     yaxis_title="Densidade")
            st.plotly_chart(fig_normal)


