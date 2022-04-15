import csv
import copy
from re import T

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

def get_pokemon_in_a_list_of_pokemmons(coach_to_ask, list_of_pokemon):
    if isinstance(list_of_pokemon, list):
        for temp_pokemon in list_of_pokemon:
            if not isinstance(temp_pokemon, Pokemon):
                raise TypeError("Los pokemon tienen que ser de la clase Pokemon")
        
        print("Entrenador " + str(coach_to_ask) + " introduce el id del pokemon: " + "\n")

        while True:
            print("Lista de pokemons:" + "\n")

            for i in list_of_pokemon:
                print(i)

            string_introduced = input(":~>")

            try:
                int_introduced = int(string_introduced)
            
            except ValueError:
                print("Introduce un id que esté en la lista")

            for temp_pokemon in list_of_pokemon:
                if int_introduced == temp_pokemon.get_id():
                    return temp_pokemon
            print("Introduce un número que esté en la lista")

    else:
        raise TypeError("list_pokemon tiene que ser una lista")

def coach_is_undefeated(list_of_pokemon):
    if isinstance(list_of_pokemon, list):
        for temp_pokemon in list_of_pokemon:
            if not isinstance(temp_pokemon, Pokemon):
                raise TypeError("Los pokemon tienen que ser del tipo Pokemon")

    defeated = True


