from clases.pokemon import *
import random

class PokemonVolador(Pokemon):
    def __init__(self, id, nombre, tipo,  ataques, salud, ataque, defensa):
        super.__init__(id, nombre, tipo,  ataques, salud, ataque, defensa)
    
    def attack(self, pokemon_to_attack):
        daño = self.ataque

        print(self.nombre," golpeó a" + pokemon_to_attack.get_nombre() + "con un daño de "+ str(daño))

        probabilidad_critico = random.randrange(0, 2)

        if probabilidad_critico == 0:
            daño = self.ataque
        else:
            daño = 2 * self.ataque
        
        pokemon_golpeado = pokemon_to_attack.defense(daño)

        return pokemon_golpeado
