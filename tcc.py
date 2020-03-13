import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from datetime import date

DIAS = [
    'Segunda-feira',
    'Terça-feira',
    'Quarta-feira',
    'Quinta-Feira',
    'Sexta-feira',
    'Sábado',
    'Domingo'
]

data = date(year=2018, month=6, day=29)
print(data)

indice_da_semana = data.weekday()
print(indice_da_semana)

dia_da_semana = DIAS[indice_da_semana]
print(dia_da_semana)

numero_do_dia_da_semana = data.isoweekday()
print(numero_do_dia_da_semana)


"""
Lendo um arquivo .csv com pandas e criando um pandas data frame
"""

df = pd.read_csv('/Unidade R\Rodrigo\Diversos\MBA\PUCMinas\TCC\PETR4.csv')
#dataframe = (df[df['Date']  <= '2019-09-17'])
#plt.plot(df['Date'], dataframe['Open'], dataframe['High'], dataframe['Low'], dataframe['Close'])

df = (df[df['Date']  <= '2019-09-17'])
#plt.plot(df['Date'], df['Open'], df['High'], df['Low'], df['Close'])
plt.plot(df['Date'], df['Open'])#, df['High'], df['Low'], df['Close'])

plt.show()


"""
#df = pd.read_csv('/Unidade R\Rodrigo\Diversos\MBA\PUCMinas\TCC\PETR4.csv')
fig = go.Figure(data=[go.cadlestick
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])

"""
"""
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['AAPL.Open'],
                high=df['AAPL.High'],
                low=df['AAPL.Low'],
                close=df['AAPL.Close'])])


fig.show()
"""


