#Analisis exploratorio para Facturación
import pandas as pd
import dtale
import dtale.app as dtale_app

df=pd.read_csv('tabla_h_historico_lc.csv',sep='|', encoding='latin-1')
data=dtale.show(df)
data.open_browser()