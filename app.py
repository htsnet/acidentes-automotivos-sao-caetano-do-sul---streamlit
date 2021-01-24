# importando a biblioteca
import streamlit as st
import pandas as pd
import pydeck as pdk

df = pd.read_csv('dfSCS.csv')
# trocando o nome do campo e ajustando o valor para tirar informação inexistente
df['latitude'] = df['LAT_(GEO)'].apply(lambda x: float(x.replace(',', '.')) if x != 'NAO DISPONIVEL' else -23.62306)
df['longitude'] = df['LONG_(GEO)'].apply(lambda x: float(x.replace(',', '.')) if x != 'NAO DISPONIVEL' else -46.55111)



PAGE_CONFIG = {
    'page_title': 'Acidentes São Caetano do Sul',
    'page_icon': ':smiley',
    'layout': 'centered'
}
#st.beta_set_page_config(**PAGE_CONFIG)

def main():
  # definindo os parâmetros
    st.title('Acidentes automotivos em São Caetano do Sul')
    st.markdown("""
    Usando as informações do site oficial do **Estado de São Paulo**, 
    este quadro apresenta um resumo dos acidentes automotivos registrados na
    cidade de São Caetano do Sul. 
    Você pode escolher na lateral esquerda o ano desejado para visualização.
    """)
    # informação na side bar
    st.sidebar.info('Foram carregadas {} linhas'. format(df.shape[0]))

    if st.sidebar.checkbox('Ver dados de entrada'):
        st.header('Dados de entrada')
        st.write(df)

    ano_selecionado = st.sidebar.slider('Selecione um ano', 2019, 2020, 2020)     # limite inferior, limite superior, valor default
    df_selected = df[df['Ano do Acidente'] == ano_selecionado]

    st.subheader('Mapa dos acidentes veiculares')
    st.map(df_selected)

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
    
     


if __name__ == '__main__':
	main()  