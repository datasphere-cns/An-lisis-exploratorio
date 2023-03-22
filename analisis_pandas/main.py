#Analisis exploratorio para Productos
import pandas as pd
from pandas_profiling import ProfileReport

data=pd.read_csv('tabla_h_historico_lc.csv',sep='|', encoding='latin-1')
profile = ProfileReport(data, title="tabla_h_historico_lc Profiling Report")
profile.to_file("tabla_h_historico_lc.html")

