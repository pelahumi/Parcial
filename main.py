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

    for temp_pokemon in list_of_pokemon:
        if temp_pokemon.is_alive():
            defeated = False
    
    return not defeated
    
def main():
    #Inicio del juego
    print("Bienvenido a Pokemon.")
    print("Empecemos con la configuración de cada usuario")

    #Configuracion usuario 1
    print("Para el usuario 1:")
    game_user_1 = get_data_from_user("coach_1_pokemons.csv")

    #Configuracion usuario 2
    print("Para el usuario 2:")
    game_user_2 = get_data_from_user("coach_2_pokemons.csv")

    print("---------------------------------------------------")
    print("Empieza el juego...")
    print("---------------------------------------------------")
    
    #Copia del equipo pokemon
    temp_list_pokemon_from_coach_1 = game_user_1
    list_pokemons_alive_coach_1 = copy.copy(temp_list_pokemon_from_coach_1)

    temp_list_pokemon_from_coach_2 = game_user_2
    list_pokemons_alive_coach_2 = copy.copy(temp_list_pokemon_from_coach_2)

    #Primeros pokemon
    print("Entrenador 1 elige tu primer pokemon")
    temp_pokemon_from_coach_1 = get_pokemon_in_a_list_of_pokemmons("Por favor entrenador 1 introduce el id del pokemon: ", list_pokemons_alive_coach_1)

    print("Entrenador 2 elige tu primer pokemon")
    temp_pokemon_from_coach_2 = get_pokemon_in_a_list_of_pokemmons("Por favor entrenador 2 introduce el id del pokemon: ", list_pokemons_alive_coach_2)

    while(coach_is_undefeated(temp_list_pokemon_from_coach_1) and coach_is_undefeated(temp_list_pokemon_from_coach_2)):

        if not temp_pokemon_from_coach_1.is_alive():
            #Selecciona un nuevo pokemon
            print("Entrenador 1 tu pokemon: " + str(temp_pokemon_from_coach_1) + " fue derrotado. Selecciona tu siguiente pokemon")
            list_pokemons_alive_coach_1.remove(temp_pokemon_from_coach_1)
            temp_pokemon_from_coach_1 = get_pokemon_in_a_list_of_pokemmons("Introduce el id del nuevo pokemon", list_pokemons_alive_coach_1)

        if not temp_pokemon_from_coach_2.is_alive():
            #Selecciona un nuevo pokemon
            print("Entrenador 2 tu pokemon: " + str(temp_pokemon_from_coach_2) + " fue derrotado. Selecciona tu siguiente pokemon")
            list_pokemons_alive_coach_2.remove(temp_pokemon_from_coach_2)
            temp_pokemon_from_coach_2 = get_pokemon_in_a_list_of_pokemmons("Introduce el id del nuevo pokemon", list_pokemons_alive_coach_2)

        print("Pokemon del entrenador 1 ataca")
        temp_pokemon_from_coach_1.attack(temp_pokemon_from_coach_2)

        print("Pokemon del entrenador 2 ataca")
        temp_pokemon_from_coach_2.attack(temp_pokemon_from_coach_1)

    print("---------------------------------------------------")
    print("El juego ha terminado...")
    print("---------------------------------------------------")

    if (coach_is_undefeated(temp_list_pokemon_from_coach_1) and not coach_is_undefeated(temp_list_pokemon_from_coach_2)):
        print("El ganador es el entrenador 1")

    elif (not coach_is_undefeated(temp_list_pokemon_from_coach_1) and coach_is_undefeated(temp_list_pokemon_from_coach_2)):
        print("El ganador es el entrenador 2")

    else:
        print("El combate termino en empate")
    
    print("---------------------------------------------------")
    print("Estadisticas")
    print("---------------------------------------------------")

    print("Entrenador 1:")
    for temp_pokemon in temp_list_pokemon_from_coach_1:
        print(temp_pokemon)

    print("Entrenador 2:")
    for temp_pokemon in temp_list_pokemon_from_coach_2:
        print(temp_pokemon)    


if __name__ == "__main__":
    main()   





