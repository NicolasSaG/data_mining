import datetime
import pandas as pd
import datetime

# Return the datetime YYYY-MM-DD
def changeDateFormat(date):
    date_file = datetime.datetime.strptime(date, "%d/%m/%Y").strftime("%Y-%m-%d")
    return date_file

def main():
    # Lee datos
    data = pd.read_csv("primer_semestre_2021.csv", header=0)
    d_f = pd.DataFrame(data)
    d_f = d_f.dropna()

    # Creacion de archivos finales
    cabeceras_incidente = ["folio", "incidente_c4",
                          "codigo_cierre", "clas_con_f_alarma"]
    cabeceras_espacial = ["colonia", "delegacion_cierre", "manzana",
                      "longitud_centroide", "latitud_centroide"]
    cabeceras_temporal = ["fecha_creacion", "hora_creacion", "fecha_cierre", "hora_cierre"]
  
    df_incidente = pd.DataFrame(columns=cabeceras_incidente)
    df_espacial = pd.DataFrame(columns=cabeceras_espacial)
    df_temporal = pd.DataFrame(columns=cabeceras_temporal)

    for index, row in d_f.iterrows():
      if (index / (d_f.shape[0])) % 5:
        print((index / (d_f.shape[0]))*100, "%")
      created_date = changeDateFormat(str(row["fecha_creacion"]))
      finished_date = changeDateFormat(str(row["fecha_cierre"]))

      df_incidente.loc[index] = [
        row["folio"],
        row["incidente_c4"],
        row["codigo_cierre"],
        row["clas_con_f_alarma"],
      ]

      df_espacial.loc[index] = [
        row["colonia"],
        row["delegacion_cierre"],
        row["manzana"],
        row["longitud_centroide"],
        row["latitud_centroide"],
      ]

      df_temporal.loc[index] = [
        created_date,
        row["hora_creacion"],
        finished_date,
        row["hora_cierre"],
      ]

    df_incidente.to_csv("indicente.csv", index_label="id_incidente")
    df_espacial.to_csv("ubicacion.csv", index_label="id_ubicacion")
    df_temporal.to_csv("fecha.csv", index_label="id_fecha")

if __name__ == "__main__":
    main()