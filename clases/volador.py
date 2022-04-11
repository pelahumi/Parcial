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
        