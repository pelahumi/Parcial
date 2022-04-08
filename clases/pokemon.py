class Pokemon():
    #Constructor
    def __init__(self, id, nombre, ataques, salud, defensa):
        self.id = id #int
        self.nombre = nombre #str
        self.ataques = ataques #diccionario
        self.salud = salud #int
        self.defensa = defensa #int
    
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

    

        





