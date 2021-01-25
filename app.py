# importando a biblioteca
import streamlit as st
import pandas as pd
import pydeck as pdk
import seaborn as sns
import matplotlib.pyplot as plt
import altair as alt

# utitliza o arquivo csv já trabalhado no programa inicial: clean_csv.py
df = pd.read_csv('dfSCS.csv')

st.set_page_config(page_title='Acidentes Automotivos em São Caetano do Sul', page_icon=':car', layout='centered', )

def main():
  # definindo os parâmetros
    st.title('Acidentes automotivos em São Caetano do Sul')
    st.markdown("""
    Usando as informações do site oficial do **Estado de São Paulo** (http://www.respeitoavida.sp.gov.br/relatorios/), 
    este quadro apresenta um resumo dos acidentes automotivos registrados na
    cidade de **São Caetano do Sul**. 
    Você pode escolher na lateral esquerda o ano desejado para visualização.
    """)
    # informação na side bar
    st.sidebar.info('Foram localizados {} acidentes.'. format(df.shape[0]))

    if st.sidebar.checkbox('Ver dados de entrada'):
        st.header('Dados de entrada')
        st.write(df)

    separa_por_ano = st.sidebar.checkbox('Separar por ano')

    if separa_por_ano:
        ano_selecionado = st.sidebar.slider('Selecione um ano', 2019, 2020, 2020)     # limite inferior, limite superior, valor default
        df_selected = df[df['Ano do Acidente'] == ano_selecionado]
        st.write('Ano com {} registros de acidentes'.format(df_selected.shape[0]))
    else:
        df_selected = df
        fig, ax = plt.subplots()
        sns.countplot(x='Ano do Acidente', data=df_selected)
        st.pyplot(fig)  

    st.subheader('Mapa dos acidentes veiculares')
    st.map(df_selected)

    st.write(' ')

    fig, ax = plt.subplots()
    g = sns.countplot(x='ano_mes_acidente', data=df_selected, order=reversed(df_selected['ano_mes_acidente'].unique()))
    g.set_xticklabels(g.get_xticklabels(), rotation=90 )
    g.set(ylabel='Qtde.', xlabel='Ano/Mês do Acidente')
    st.pyplot(fig)


    fig, ax = plt.subplots()
    g = sns.countplot(x='dia_da_semana', data=df_selected, order=df_selected['dia_da_semana'].value_counts().index)
    g.set_xticklabels(g.get_xticklabels(), rotation=30)
    g.set(ylabel='Qtde.')
    st.pyplot(fig)

    fig, ax = plt.subplots()
    g = sns.countplot(x='hora_cheia', data=df_selected)
    g.set(xlabel='Hora Cheia', ylabel='Qtde.')
    st.pyplot(fig)
    
    st.write('Algumas linhas de informação não apresentam as coordenadas geográficas do acidente. Para todos estes casos foi considerado um ponto único')


if __name__ == '__main__':
	main()  