from os.path import isfile, join
import os
import pandas
import shutil
import csv


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


# limpieza
# valores nulos son los -99


# creacion de archivo bitacora para guardar eliminaciones de los otros archivos, inconsistencias, etc
bitacora_columnas = ['id', 'nombre-archivo', 'data_fecha', 'data_LOM', 'data_DIC', 'data_MCM',
                     'data_TLA', 'data_XAL', 'data_EDL', 'data_IBM', 'data_NEZ', 'data_MON', 'data_EAJ', 'data_AJU', 'data_MPA', 'data_SNT', 'data_COR', 'data_LAA', 'descripcion', 'fecha']

dataset_columnas = ['id', 'fecha', 'LOM', 'DIC', 'MCM',
                    'TLA', 'XAL', 'EDL', 'IBM', 'NEZ', 'MON', 'EAJ', 'AJU', 'MPA', 'SNT', 'COR', 'LAA']

for year in range(2010, 2011):
    path = "recursos/datos/pph/{}PPH.xls".format(year)
    bitacora = pandas.DataFrame(columns=bitacora_columnas)
    file = pandas.read_excel(path)

    dato = {}
    dato["id"] = 1
    dato["nombre-archivo"] = "prueba"
    bitacora.append(dato)
    print(file)
    print(bitacora)
