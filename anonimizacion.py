import pandas as pd
f=pd.read_csv(".\Desktop\Viajes-47929.csv", encoding="utf8", sep=",")
keep_col = ['ID','Estado cerrado','Duración','Id de estación de inicio','Fecha de inicio','Nombre de estación de inicio','Fecha de fin','Id de estación de fin de viaje','Nombre de estación de fin de viaje']
new_f = f[keep_col]
new_f.to_csv(".\Desktop\Viajes-47929.csv", index=False)