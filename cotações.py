import pandas as pd
import plotly.graph_objects as go
import datetime

df = pd.read_excel('/Unidade R\Rodrigo\Diversos\MBA\PUCMinas\TCC\PETR45M.xlsx')
df['Hora'] = pd.to_datetime(df['Data']).dt.time

#df = df.loc[(df['Hora'] >= datetime.time(hour=10)) & (df['Hora'] < datetime.time(hour=11))]
#df = df.loc[df['']]
df = df.loc[(df['Hora'] <= datetime.time(hour=10, minute= 59))]
#df = df.loc[(df['Data'] == '2020-2-18 01:00:00')]

df = df[(df['Data'] >= '2020-2-1 01:00:00') & (df['Data'] <= '2020-2-19 00:00:00')]


'''
fig = go.Figure(data=[go.Candlestick(x=df['Data'],
                                  open=df['Abertura'], 
                                  high=df['Máxima'],
                                   low=df['Mínima'], 
                close=df['Fechamento'])
                     ])

cotacoes = go.Figure(data=[go.Candlestick(x=df['Data'],
                                       open=df['Abertura'], 
                                       high=df['Máxima'],
                                        low=df['Mínima'], 
                                    close=df['Fechamento'])])
print('cotacoes')
print(cotacoes)
mme1 = [x= df['Data'],    
        y= df['Média Móvel E [17]'],
     type= 'scatter',
     mode= 'lines',
     line= [
        'width': 1,
        'color': 'red'
         ],
    name= 'Média (17 periodos)'
       ]

print('mme')
print(mme1)

t3 = {
    'x': df['Data'],
    'y': df['Média Móvel E [72]'],
    'type': 'scatter',
    'mode': 'lines',
    'line': {
        'width': 1,
        'color': 'blue'
    },
    'name': 'Média (30 dias)'
}


'''

#fig.update_layout(xaxis_rangeslider_visible=False)  
#fig.show()

t1 = {
    'x': df.Data,
    'open': df.Abertura,
    'close': df.Fechamento,
    'high': df.Máxima,
    'low': df.Mínima,
    'type': 'candlestick',
    'name': 'PETR$',
    'showlegend': False
}

print('Trace1')
print(trace1)

# média de 30 dias (linha)
t2 = {
    'x': df['Data'],
    'y': df['Média Móvel E [17]'],
    'type': 'scatter',
    'mode': 'lines',
    'line': {
        'width': 1,
        'color': 'red'
    },
    'name': 'Média (30 dias)'
}

print('Trace2')
print(trace2)

t3 = {
    'x': df['Data'],
    'y': df['Média Móvel E [72]'],
    'type': 'scatter',
    'mode': 'lines',
    'line': {
        'width': 1,
        'color': 'blue'
    },
    'name': 'Média (30 dias)'
}
 
# informar todos os dados e gráficos em uma lista
data = [t1, t2, t3]
 
# configurar o layout do gráfico
layout = go.Layout({
    'title': {
        'text': 'Gráfico de Candlestick - BBAS3',
        'font': {
            'size': 20
        }
    }
})
 
# instanciar objeto Figure e plotar o gráfico
fig = go.Figure(data=data, layout=layout)
fig.show()
