class Pokemon():

    pokedex = []

    #Constructor
    def __init__(self, id, nombre, tipo,  ataques, salud, ataque, defensa):
        self.id = id #int
        self.nombre = nombre #str
        self.tipo = tipo #str
        self.ataques = ataques 
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

        if isinstance(nombre, str):
            self.nombre = nombre
        else: 
            raise TypeError("El nombre tiene que ser un str")
        
        if isinstance(tipo, str):
            self.tipo = tipo
        else: 
            raise TypeError("El tipo tiene que ser un str")

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

        if isinstance(defensa, int):
            if 1 <= defensa <= 10:
                self.defensa = defensa
        else:
            raise ValueError("La defensa tiene que ser un número del 1 al 10")

    #Destructor
    def __del__(self):
        print("Se ha eliminado el pokemon")
    
    

    #Getters y setters
    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre
    
    def get_ataques(self):
        return self.ataques
    
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
    
    def set_ataques(self, ataques_to_be_set):
        if isinstance(ataques_to_be_set, list):
            self.ataques = ataques_to_be_set
        else:
            raise TypeError("Los ataques tienen que ser una lista")

    def set_salud(self, salud_to_be_set):
        if isinstance(salud_to_be_set, int):
            if 1 <= salud_to_be_set <=100:
                self.salud = salud_to_be_set
        else:
            raise ValueError("La salud tiene que ser un número del 1 al 100")

    def set_ataque(self,ataque_to_be_set):
         if isinstance(ataque_to_be_set, int):
            if 1 <= ataque_to_be_set <= 10:
                self.ataque = ataque_to_be_set
            else:
                raise ValueError("El ataque tiene que ser un número del 1 al 10")

    def set_defensa(self, defensa_to_be_set):
         if isinstance(defensa_to_be_set, int):
            if 1 <= defensa_to_be_set <= 10:
                self.ataque = defensa_to_be_set
            else:
                raise ValueError("La defensa tiene que ser un número del 1 al 10")

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


    

        





