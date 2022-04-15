import csv
import copy

from clases.ataques import *
from clases.pokemon import *

def get_data_from_user(name_file):
    equipo_pokemon = []

    if not isinstance(name_file, str):
        raise TypeError("El nombre del archivo no es un string")

    name_file_s = name_file
    