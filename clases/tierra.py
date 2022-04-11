from clases.pokemon import *

class PokemonTierra(Pokemon):
    def __init__(self, id, nombre, tipo,  ataques, salud, ataque, defensa):
        super.__init__(id, nombre, tipo,  ataques, salud, ataque, 16)

        if isinstance(defensa, int):
            if 11 <= defensa <= 20:
                self.defensa = defensa
            else:
                raise ValueError("La defensa tiene que ser un número del 1 al 10")
        else:
            raise TypeError("La defensa tiene que ser un número")

    def set_defensa(self, defensa_to_be_set):
        if isinstance(defensa_to_be_set, int):
            if 11<= defensa_to_be_set <=20:
                self.defensa =defensa_to_be_set
            else:
                raise ValueError("La defensa tiene que estar entre 11 y 20")
        else:
            raise TypeError("La defensa tiene que ser un número")
        

        
