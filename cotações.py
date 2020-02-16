%matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import pandas_datareader as pdr
import quandl
import datetime 

codigo = 'PETR4.SA'

sns.set(style='whitegrid')

ativo = pdr.get_data_yahoo(codigo)

ativo.head()
ativo.Close.plot(figsize=(17, 6));
