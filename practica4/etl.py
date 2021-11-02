from os.path import isfile, join
import os
import pandas as pd
import shutil

def get_files(year, final_txt):
  path = "recursos/datos/{}REDDA".format(
    year[2:])
  filenames = [f for f in os.listdir(path) if isfile(join(path, f))]

  print("Obteniendo archivos de {}".format(path))
  for filename in filenames:
    if filename.endswith(final_txt):
      shutil.copyfile("{}\\{}".format(path, filename),
          "recursos/datos/pph/{}".format(filename))

  print("Archivos obtenidos".format(final_txt))


# obtener archivos solicitados de los años y guardarlos en una carpeta aparte
try:
  os.mkdir("recursos/datos/pph")
except:
  print("carpeta datos_solicidatos ya existe")

for year in range(2010, 2020):
  get_files(str(year), "PPH.xls")


dataframes = []
for year in range(2010, 2020):
  path = "recursos/datos/pph/{}PPH.xls".format(year)
  df = pd.read_excel(path, index_col=None)
  df.index.name = "ID"

  # Se remueven filas vacias
  df.dropna(how="all", inplace=True)

  # Se unifican los tipos de dato de las fechas
  if df["FECHA"].dtype != "datetime64[ns]":
      df["FECHA"] = df["FECHA"].astype(str)
      df["FECHA"] = pd.to_datetime(df["FECHA"])

  # Se agregan las columnas para el semana, mes y año
  df.insert(loc=1, column="AÑO", value = df["FECHA"].dt.year, allow_duplicates = False)
  df.insert(loc=2, column="MES", value = df["FECHA"].dt.month, allow_duplicates = False)
  df.insert(loc=3, column="SEMANA", value = df["FECHA"].dt.isocalendar().week, allow_duplicates = False)

  dataframes.append(df)

# Se concatenan los dataframes
join_table = pd.concat(dataframes).reset_index(drop=True)

# Leemos estaciones.csv
path = "recursos/datos/{}".format("estaciones.csv")
stations = pd.read_csv(path, index_col=None)
df_stations = pd.DataFrame(stations)
locations = dict(zip(list(df_stations["Clave"]), list(df_stations["Estación"])))

# creacion de archivo bitacora para guardar eliminaciones de los otros archivos, inconsistencias, etc
bitacora_col = [ 'elemento', 'fecha', 'año', 'mes', 'semana', 'localizacion', 'medicion']
dt_bt = pd.DataFrame(columns=bitacora_col)

print('Escribiendo tabla de hechos...')
count = 0
for index in range(0, len(join_table)):
  for col_title in join_table.columns.values[4:]:
    if(join_table.iloc[index][col_title] != -99.0):
      dt_bt.loc[count] = [
        "Precipitación pluvial",
        join_table.iloc[index]["FECHA"],
        join_table.iloc[index]["AÑO"],
        join_table.iloc[index]["MES"],
        join_table.iloc[index]["SEMANA"],
        locations[col_title],
        join_table.iloc[index][col_title]
      ]

      count+=1

  dt_bt.index.name = "ID"

# Escritura de tabla de hechos en archivo bitacora.csv
path = 'recursos/datos/pph/{}'.format("bitacora.csv")
dt_bt.to_csv(path, index=True)

print('Completo')