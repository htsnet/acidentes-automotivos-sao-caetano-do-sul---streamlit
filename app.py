# importando a biblioteca
import streamlit as st
import pandas as pd
import pydeck as pdk
import seaborn as sns
import matplotlib.pyplot as plt
import altair as alt

df = pd.read_csv('dfSCS.csv')
# comandos executados na geração do arquivo, não é mais preciso aqui
# trocando o nome do campo e ajustando o valor para tirar informação inexistente
# df['latitude'] = df['LAT_(GEO)'].apply(lambda x: float(x.replace(',', '.')) if x != 'NAO DISPONIVEL' else -23.62306)
# df['longitude'] = df['LONG_(GEO)'].apply(lambda x: float(x.replace(',', '.')) if x != 'NAO DISPONIVEL' else -46.55111)
# df['hora_cheia'] = df['Hora do Acidente'].apply(lambda x: x[0:2])



PAGE_CONFIG = {
    'page_title': 'Acidentes São Caetano do Sul',
    'page_icon': ':smiley',
    'layout': 'centered'
}
#st.beta_set_page_config(**PAGE_CONFIG)
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

    # st.write(alt.Chart(df_selected).mark_bar().encode(
    #     x=alt.X('Dia da Semana', sort=None),
    #     y='Dia',
    # ))

    fig, ax = plt.subplots()
    g = sns.countplot(x='ano_mes_acidente', data=df_selected)
    g.set_xticklabels(g.get_xticklabels(), rotation=90  )
    g.set(ylabel='Qtde.')
    st.pyplot(fig)


    fig, ax = plt.subplots()
    g = sns.countplot(x='Dia da Semana', data=df_selected, order=df_selected['Dia da Semana'].unique())
    g.set_xticklabels(g.get_xticklabels(), rotation=30)
    g.set(ylabel='Qtde.')
    st.pyplot(fig)

    fig, ax = plt.subplots()
    g = sns.countplot(x='hora_cheia', data=df_selected)
    g.set(xlabel='Hora Cheia', ylabel='Qtde.')
    st.pyplot(fig)
    
    

    # fig, ax = plt.subplots()
    # ax.hist(df_selected['Dia da Semana'], bins=13)
    # st.pyplot(fig)

    # day_order = ["DOMINGO", "SEGUNDA", "TERÇA", "QUARTA", "QUINTA", "SEXTA", "SÁBADO"]
    # sns.countplot(x = "Dia da Semana", data = df_selected, order = day_order)

    #Bar Chart
    # st.bar_chart(df_selected['Dia da Semana'])
    

    #histogram
    
    # df_selected['Dia da Semana'].hist()
    # plt.show()
    # st.pyplot()

    # st.pydeck_chart(pdk.Deck(
    #     initial_view_state=pdk.ViewState(
    #         latitude=-23.62306,
    #         longitude=-46.55111,
    #         zoom=12,
    #         radius=20,
    #         pitch=40
    #     ),
    #     layers=[
    #         pdk.Layer(
    #             'HexagonLayer',
    #             data=df_selected[['latitude', 'longitude']],
    #             get_position='[longitude, latitude]',
    #             elevation_state=10,
    #             pickable=True,
    #             extruded=True,
    #             get_color='[200, 30, 0, 160]',

    #         )
    #     ]
    # ))
    
    st.write('Algumas linhas de informação não apresentam as coordenadas geográficas do acidente. Para todos estes casos foi considerado um ponto único')


if __name__ == '__main__':
	main()  