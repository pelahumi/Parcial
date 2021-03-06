from typing import Type
from clases.ataques import *

class Pokemon():

    pokedex = []

    #Constructor
    def __init__(self, id, nombre, tipo, tipo_ataque, salud, ataque, defensa):
        self.id = id #int
        self.nombre = nombre #str
        self.tipo = tipo
        self.tipo_ataque = tipo_ataque #str
        self.salud = salud #int
        self.ataque = ataque #int
        self.defensa = defensa #int

        #Comprobar
        if isinstance(id, int):
            if id not in Pokemon.pokedex:
                self.id = id
                Pokemon.pokedex.append(self.id)
            else:
                raise ValueError("El pokemon elegido ya está registrado en la pokedex")
        else:
            raise TypeError("El id del pokemon tiene que ser un número")

        if isinstance(nombre, str):
            self.nombre = nombre
        else: 
            raise TypeError("El nombre tiene que ser un str")
        
        if isinstance(tipo, str):
            self.tipo = tipo
        else:
            raise TypeError("El tipo tiene que ser un str")
        
        if isinstance(tipo_ataque, str):
            self.tipo_ataque = tipo_ataque
        else: 
            raise TypeError("El tipo de ataque tiene que ser un str")

        if isinstance(salud, int):
            if 1 <= salud <=100:
                self.salud = salud
        else:
            raise ValueError("La salud tiene que ser un número del 1 al 100")
        
        if isinstance(ataque, int):
            if 1 <= ataque <= 10:
                self.ataque = ataque
            else:
                raise ValueError("El ataque tiene que ser un número del 1 al 10")
        else:
            raise TypeError("El ataque tiene que ser un número")

        if isinstance(defensa, int):
            if 1 <= defensa <= 10:
                self.defensa = defensa
            else:
                raise ValueError("La defensa tiene que ser un número del 1 al 10")
        else:
            raise TypeError("La defensa tiene que ser un número")

    #Destructor
    def destructor(self):
        print("Se ha transferido el pokemon")
        Pokemon.pokedex.remove(self.id)

    #Getters y setters
    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre
    
    def get_tipo(self):
        return self.tipo
    
    def get_tipo_ataque (self):
        return self.tipo_ataque 
    
    def get_salud(self):
        return self.salud
    
    def get_defensa(self):
        return self.defensa

    def set_id(self, id_to_be_set):
        if isinstance(id_to_be_set, int):
            if id not in Pokemon.pokedex:
                self.id = id_to_be_set
                Pokemon.pokedex.append(self.id)
            else:
                raise ValueError("El pokemon elegido ya está registrado en la pokedex")

    def set_nombre(self, name_to_be_set):
        if isinstance(name_to_be_set, str):
            self.nombre = name_to_be_set
        else: 
            raise TypeError("El nombre tiene que ser un str")
    
    def set_tipo(self, type_to_set):
        if isinstance(type_to_set, str):
            self.tipo = type_to_set
        else: 
            raise TypeError("El tipo tiene que ser un str")
    
    def set_tipo_ataque (self, ataques_to_be_set):
        if isinstance(ataques_to_be_set, list):
            self.tipo_ataque  = ataques_to_be_set
        else:
            raise TypeError("Los ataques tienen que ser un str")

    def set_salud(self, salud_to_be_set):
        if isinstance(salud_to_be_set, int):
            if 1 <= salud_to_be_set <=100:
                self.salud = salud_to_be_set
            else:
                raise ValueError("La salud tiene que ser un número del 1 al 100")
        else:
            raise TypeError("La salud tiene que ser un número")

    def set_ataque(self,ataque_to_be_set):
        if isinstance(ataque_to_be_set, int):
            if 1 <= ataque_to_be_set <= 10:
                self.ataque = ataque_to_be_set
            else:
                raise ValueError("El ataque tiene que ser un número del 1 al 10")
        else:
            raise TypeError("El ataque tiene que ser un número")

    def set_defensa(self, defensa_to_be_set):
        if isinstance(defensa_to_be_set, int):
            if 1 <= defensa_to_be_set <= 10:
                self.ataque = defensa_to_be_set
            else:
                raise ValueError("La defensa tiene que ser un número del 1 al 10")
        else:
            raise TypeError("La defensa tiene que ser un número")

    #Descripción del pokemon
    def __str__(self):
        descripcion = ("El pokemon " + str(self.nombre) + "con id " + str(self.id) + 
                        ", sus ataques son: " + str(self.tipo_ataque.nombre) + 
                        "y " + str(self.salud)  + "puntos de vida")
        
        return descripcion
 
    #Comprobar si está vivo --> bool
    def is_alive(self):
        if self.salud > 0:
            return True
        else: 
            return False

    #Atacar
    def attack(self, pokemon_to_attack):
        daño = self.ataque
        print(self.nombre," fue atacado por ",pokemon_to_attack.get_nombre()," e hizo un daño de: ",str(daño))
        pokemon_golpeado = pokemon_to_attack.defense(daño)
        return pokemon_golpeado

    #Defender
    def defense(self, daño):
        if not isinstance(daño, int):
            raise TypeError("Los puntos de ataque tienen que ser un int")

        print(self.nombre," recibió ",daño," puntos de daño")

        if daño > self.defensa:
            self._health_points = (self.salud -
                                   (daño - self.defensa))
            pokemon_golpeado = True
        else:
            print("No recibió daño")
            pokemon_golpeado = False

        if self.salud < 1:
            self.salud = 0

        return pokemon_golpeado







    

        





