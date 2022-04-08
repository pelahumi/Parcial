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





