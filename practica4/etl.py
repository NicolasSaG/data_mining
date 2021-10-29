from os.path import isfile, join
import os


def get_files(year, final_txt):
    path = "C:\\Users\\fnico\\Documents\\github\\data_mining\\practica4\\recursos\\datos\\{}REDDA".format(
        year[2:])
    filenames = [f for f in os.listdir(path) if isfile(join(path, f))]

    print("Borrando archivos de {}".format(path))
    for filename in filenames:
        if not filename.endswith(final_txt):
            os.remove("{}\\{}".format(path, filename))

    print("Archivos que no concuerdan con {} han sido borrados".format(final_txt))


for year in range(2010, 2020):
    get_files(str(year), "PPH.xls")
