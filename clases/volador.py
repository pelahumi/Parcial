from clases.pokemon import *
import random

class PokemonVolador(Pokemon):
    def __init__(self, id, nombre, tipo,  ataques, salud, ataque, defensa):
        super.__init__(id, nombre, tipo,  ataques, salud, ataque, defensa)
    
    def defense(self, daño):
        if not isinstance(daño, int):
            raise TypeError("Los puntos de daño tienen que ser un número")

        print(self.nombre," recibió ",str(daño)," puntos de daño")

        probabilidad_fallo = random.randrange(0, 2)

        if probabilidad_fallo == 0:
            if daño > self.defensa:
                self.salud = (self.salud - (daño - self.defensa))
                pokemon_golpeado = True
            else:
                print("No recibió ningún daño")
                pokemon_golpeado = False
        
        else:
            print("No recibió ningún daño")
            pokemon_golpeado = False

        if self.salud < 1:
            self.salud = 0
            
        return pokemon_golpeado