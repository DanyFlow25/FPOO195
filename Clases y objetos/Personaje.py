class Personaje:
    
    #atributo de personaje
    especie= "Humano"
    nombre= "Jhon"
    altura= 2.18
    
    #Metodos del personaje
    def correr(self, estado):
        if(estado):
            print("El personaje"+ self.nombre+" está corriendo")
        else:
            print("El personaje "+ self.nombre+" está muerto")
            
    def lanzarGranada(self):
        print(self.nombre+" Pegó una granada")
