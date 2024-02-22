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
        
    def recargarArma(self, municion):
        cargador= 25
        cargador=cargador+municion
        print("Arma recargada al "+ str(cargador)+"%")
 
 #Creamos el objeto de la clase personaje       
spartan = Personaje()

print(spartan.nombre)
print(spartan.especie)
print(spartan.altura)