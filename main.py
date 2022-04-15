import csv
import copy

from clases.ataques import *
from clases.pokemon import *

def get_data_from_user(name_file):
    equipo_pokemon = []

    if not isinstance(name_file, str):
        raise TypeError("El nombre del archivo no es un string")

    name_file_s = name_file

    try:
        with open(name_file_s, newline='') as csv_file:
            reader =csv.reader(csv_file)
            data_from_file = list(reader)
        
        for temp_pokemon_csv in data_from_file:
            entrenador = Pokemon(int(temp_pokemon_csv[0]),
            temp_pokemon_csv[1], 
            TipoAtaque.from_str(temp_pokemon_csv[2]),
            int(temp_pokemon_csv[3]),
            int(temp_pokemon_csv[4]),
            int(temp_pokemon_csv[5]))

            equipo_pokemon.append(entrenador)
    
    except SyntaxError:
        print("El pokemon del entrenador no fue introducido correctamente. Vuelve a intentarlo.")

    return equipo_pokemon


