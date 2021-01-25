# Programa para higienizer o arquivo bruto de acidentes automotivos não fatais 

# importação de bibliotecas
import pandas as pd

# leitura do arquivo completo
df = pd.read_csv('acidentes_naofatais.csv', encoding='iso-8859-1', sep=';')

# faz uma copia para trabalho selecionado apenas uma cidade, no caso, São Caetano do Sul
dfSCS = df.loc[df['Município'] == 'SAO CAETANO DO SUL']

# Modifica o nome do dia da semana
def renomeia_dia_da_semana(texto):
  if texto == 'QUINTA':
    return '5 - Qui'
  elif texto == 'QUARTA':
    return '4 - Qua'
  elif texto == 'DOMINGO':
    return '1 - Dom'
  elif texto == 'TERÇA':
    return '3 - Ter'
  elif texto == 'SEGUNDA':
    return '2 - Seg'
  elif texto == 'SÁBADO':
    return '7 - Sab'       
  elif texto == 'SEXTA':
    return '6 - Sex'
  else:
    return '8 - (?)'

dfSCS['dia_da_semana'] = dfSCS['Dia da Semana'].apply(renomeia_dia_da_semana)
# trocando o nome do campo e ajustando o valor para tirar informação inexistente
dfSCS['latitude'] = dfSCS['LAT_(GEO)'].apply(lambda x: float(x.replace(',', '.')) if x != 'NAO DISPONIVEL' else -23.62306)
dfSCS['longitude'] = dfSCS['LONG_(GEO)'].apply(lambda x: float(x.replace(',', '.')) if x != 'NAO DISPONIVEL' else -46.55111)
dfSCS['hora_cheia'] = dfSCS['Hora do Acidente'].apply(lambda x: x[0:2])
dfSCS['ano_mes_acidente'] = dfSCS['Data do Acidente'].apply(lambda x: x[0:4] + '/' + x[5:7])
#apaga campos desnecessários
dfSCS = dfSCS.drop(["LAT_(GEO)", "LONG_(GEO)", "Ano/Mês do Acidente", 'Mês do Acidente', 'Município', 'Região Administrativa', 'Jurisdição',	'Administração', 'Conservação', 'Serviço de Atendimento - Bombeiro', 'Serviço de Atendimento - PMRV', 'Serviço de Atendimento - PRF', 'Serviço de Atendimento - Radio Patrulha', 'Servciço de Atendimento - CPTRAN'], axis=1)
dfSCS.to_csv('dfSCS.csv', index=False)

dfSCS.head()

a = pd.DataFrame(dfSCS.groupby(['ano_mes_acidente']).size(), columns=['data'])
a.reset_index(inplace=True)
a.head()
#dfSCS.info()
