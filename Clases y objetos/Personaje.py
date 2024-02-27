class Personaje:
    
    #atributo de personaje
    #Declaramos el constructor
    
    def __init__(self,esp,nom,alt):

        self.especie = esp
        self.nombre = nom
        self.altura = alt
    
    #Metodos del personaje
    def correr(self, estado):
        if(estado):
            print("El personaje"+ self.nombre+" está corriendo")
        else:
            print("El personaje "+ self.nombre+" está muerto")
            
    def lanzarGranada(self):
        print(self.nombre+" Pegó una granada")
