from enum import Enum

class TipoAtaque(Enum):
    PUÑETAZO = 2
    PATADA = 4
    CODAZO = 6
    CABEZAZO = 10

    def __str__(self):
        return self.nombre
    
    @staticmethod
    def from_str(str_tipo_ataque):
        str_tipo_ataque = str_tipo_ataque.lower()
        if str_tipo_ataque == "puñetazo":
            return TipoAtaque.PUÑETAZO
        elif str_tipo_ataque == "patada":
            return TipoAtaque.PATADA
        elif str_tipo_ataque == "codazo":
            return TipoAtaque.CODAZO
        elif str_tipo_ataque == "cabezazo":
            return TipoAtaque.CABEZAZO
        else:
            raise TypeError("No existe el ataque: ",str_tipo_ataque)
