class Pokemon():

    pokedex = []

    #Constructor
    def __init__(self, id, nombre, ataques, salud, defensa):
        self.id = id #int
        self.nombre = nombre #str
        self.ataques = ataques #diccionario
        self.salud = salud #int
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

        if isinstance(salud, int):
            if 1 <= salud <=100:
                self.salud = salud
        else:
            raise ValueError("La salud tiene que ser un número del 1 al 100")

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

    #Comprobar si está vivo --> bool
    def is_alive(self):
        if self.salud > 0:
            return True
        else: 
            return False
    

        





