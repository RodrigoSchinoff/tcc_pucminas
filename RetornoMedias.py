import pandas as pd
import plotly.graph_objects as go
import datetime

#df = pd.read_excel('/Unidade R\Rodrigo\Diversos\MBA\PUCMinas\TCC\PETR45M.xlsx')
df = pd.read_excel('/Users/andreaguimaraesrochaoliveira/venvtcc/PETR45M.xlsx',usecols="A,E,F")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df['Hora'] = pd.to_datetime(df['Data']).dt.time
df['Data'] = pd.to_datetime(df['Data']).dt.date
df['Perc'] = df['Fechamento'] / df['Média Móvel E [17]']

#df = df.query('Hora <= datetime.time(hour=10, minute= 30) and (Perc >= 1.004 or Perc <= 0.994)')



#df = df.loc[(df['Hora'] >= datetime.time(hour=10)) & (df['Hora'] < datetime.time(hour=11))]
#df = df.loc[df['']]
#df = df.loc[(df['Hora'] <= datetime.time(hour=10, minute= 59))]
#df = df.loc[(df['Data'] == '2020-2-18 01:00:00')]

#df = df[(df['Data'] >= '2020-2-1 01:00:00') & (df['Data'] <= '2020-2-19 00:00:00')]



vData = '2020-01-01'
#vData = date.today()
vLonge = 'N'
vVoltou = 'N'
vIndexLonge = 0

for index, row in df[::-1].iterrows():
        
    if vData != row['Data'] and vLonge == 'S' and vVoltou == 'N':
        df.loc[vIndexLonge, 'AbriuLongeMedia'] = ''
        
        
    if row['Hora'] <= datetime.time(hour=10, minute= 15) and vData != row['Data'] and (row['Perc'] >= 1.004 or row['Perc'] <= 0.994):
        df.loc[index, 'AbriuLongeMedia'] = 'S'
        vIndexLonge = index
        vData = row['Data']
        vLonge = 'S'
        vVoltou = 'N'
        df.loc[index, 'RetornouMedia'] = ''  
    elif row['Hora'] <= datetime.time(hour=10, minute= 55) and vData == row['Data'] and vLonge == 'S' and vVoltou == 'N' and (row['Perc'] < 1.004 and row['Perc'] > 0.997):
        df.loc[index, 'RetornouMedia'] = 'S'
        vVoltou = 'S'
        df.loc[index, 'AbriuLongeMedia'] = ''
    else:
        df.loc[index, 'AbriuLongeMedia'] = ''
        df.loc[index, 'RetornouMedia'] = ''

#df = df.query('AbriuLongeMedia in ("S", "N")')

#df = df.query('AbriuLongeMedia == "S"')
