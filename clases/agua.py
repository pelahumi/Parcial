from clases.pokemon import *

class PokemonAgua(Pokemon):
    def __init__(self, id, nombre, tipo,  ataques, salud, ataque, defensa):
        super.__init__(id, nombre, tipo,  ataques, salud, 14, defensa)

        if isinstance(ataque, int):
            if 11 <= ataque <= 20:
                self.ataque = ataque
            else:
                raise ValueError("El ataque tiene que ser un número del 1 al 10")
        else:
            raise TypeError("El ataque tiene que ser un número")

    def set_ataque(self, ataque_to_be_set):
        if isinstance(ataque_to_be_set, int):
            if 11<= ataque_to_be_set <=20:
                self.defensa =ataque_to_be_set
            else:
                raise ValueError("El ataque tiene que estar entre 11 y 20")
        else:
            raise TypeError("El ataque tiene que ser un número")