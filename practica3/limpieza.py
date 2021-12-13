import pandas as pd
import unidecode


def generarCodigo(clave_entidad, clave_municipio, clave_localidad, clave_ageb, clave_manzana):
    mapa_codigo = ""
    if len(clave_entidad) < 2:
        mapa_codigo += "0" * (2 - len(clave_entidad))
    mapa_codigo += clave_entidad

    if len(clave_municipio) < 3:
        mapa_codigo += "0" * (3 - len(clave_municipio))
    mapa_codigo += clave_municipio

    if len(clave_localidad) < 4:
        mapa_codigo += "0" * (4 - len(clave_localidad))
    mapa_codigo += clave_localidad

    if len(clave_ageb) < 4:
        mapa_codigo += "0" * (4 - len(clave_ageb))
    mapa_codigo += clave_ageb

    if len(clave_manzana) < 3:
        mapa_codigo += "0" * (3 - len(clave_manzana))
    mapa_codigo += clave_manzana

    return mapa_codigo


inegi_file = pd.read_csv("data_inegi.csv", index_col=None)
df_inegi = pd.DataFrame(inegi_file)

df1 = df_inegi[['ENTIDAD', 'NOM_ENT', 'MUN', 'NOM_MUN',
                'LOC', 'NOM_LOC', 'AGEB', 'MZA', 'POBTOT', 'POBMAS', 'POBFEM', 'VIVTOT']].copy()

df2 = df1[~ df1.NOM_MUN.str.contains("Total")]
df3 = df2[~ df2.NOM_LOC.str.contains("Total")]
df3 = df3.reset_index()
df3 = df3.drop(columns=["index"])


# Creacion de archivos finales
cabeceras_poblacion = ["pob_total", "pob_masculina",
                       "pob_femenina", "total_viviendas_habitadas"]
cabeceras_lugar = ["mapa", "cve_ent", "nom_ent",
                   "cve_num", "nom_mun", 'cve_loc', "nom_loc"]
df_poblacion = pd.DataFrame(columns=cabeceras_poblacion)
df_lugar = pd.DataFrame(columns=cabeceras_lugar)

for index, row in df3.iterrows():
    if (index / (df3.shape[0])) % 5:
        print((index / (df3.shape[0]))*100, "%")
    mapa = generarCodigo(str(row["ENTIDAD"]), str(row["MUN"]),
                         str(row["LOC"]), str(row["AGEB"]), str(row["MZA"]))

    df_poblacion.loc[index] = [row["POBTOT"],
                               row["POBMAS"], row["POBFEM"], row["VIVTOT"]]
    df_lugar.loc[index] = [str(mapa),
                           row["ENTIDAD"], unidecode.unidecode(row["NOM_ENT"].upper()), row["MUN"],  unidecode.unidecode(row["NOM_MUN"].upper()), row["LOC"], unidecode.unidecode(row["NOM_LOC"].upper())]

# exportar datos
df_poblacion.to_csv("poblacion.csv", index_label="id_poblacion")
df_lugar.to_csv("lugar.csv", index_label="id_lugar")
