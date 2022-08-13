#1
class Saludo():
    def __init__(self, palabra):
        self.palabra=palabra
    def saludar(self):
        print ("Hola "+self.palabra)

def main():
    objetoSaludo=Saludo("Alex")
    objetoSaludo.saludar()

if __name__ == "__main__":
    main()        
#2 
class Gato():
    def __init__(self, nombre, raza, color):
        self.nombre=nombre 
        self.raza=raza
        self.color=color
    def maullar(self):
        print("Miauuuuu")
    def mostrarDatos(self):
        print("Soy el gato",self.nombre,"soy de color", self.color,"y de raza", self.raza)    

def main():
    objetoGato=Gato("Pelusa", "Angora","Plateado")
    objetoGato.mostrarDatos()
    objetoGato.maullar()

if __name__ == "__main__":
    main()    
#3
class Suma():
    def __init__(self, numero1, numero2): 
        self.numero1=numero1
        self.numero2=numero2
    def sumar(self):
        return self.numero1+self.numero2 

def main():
    objetoSuma=Suma(1,2)
    suma=objetoSuma.sumar()
    print(suma)

if __name__ == "__main__":
    main()         
#4
class Operaciones():
    def __init__(self, numero1, numero2): 
        self.numero1=numero1
        self.numero2=numero2
    def sumar(self):
        return self.numero1+self.numero2 
    def restar(self):
        return self.numero1-self.numero2 
    def multiplicar(self):
        return self.numero1*self.numero2    
    def dividir(self):
        return self.numero1/self.numero2      

def main():
    objetoOperaciones=Operaciones(1,2)
    suma=objetoOperaciones.sumar()
    resta=objetoOperaciones.restar()
    multiplicacion=objetoOperaciones.multiplicar()
    division=objetoOperaciones.dividir()
    print("La suma es: ",suma)
    print("La resta es: ",resta)
    print("La multiplicación es: ",multiplicacion)
    print("La división es: ",division)

if __name__ == "__main__":
    main()         

#5
class Persona():
    def __init__(self, nombre, apellidoPaterno, apellidoMaterno): 
        self.nombre=nombre
        self.apellidoPaterno=apellidoPaterno
        self.apellidoMaterno=apellidoMaterno
    def mostrarPersona(self):
        print("Soy", self.nombre,"mi apellido es", self.apellidoPaterno, self.apellidoMaterno)  

def main():
    objetoPersona=Persona(apellidoMaterno="Torres",nombre="Julio", apellidoPaterno="Nureña")
    objetoPersona.mostrarPersona()

if __name__ == "__main__":
    main()           
#6 numpy
import numpy as np

#Lista de valores
lista=[1,2,3]
#Convertimos a array
array=np.array(lista)
print(array)
print(array[1])
#7 
for i in range(len(array)):
    print(array[i])

#8
#np.arange(desde,hasta,saltos)
arrayDel0al20=np.arange(0,20,2)

print(arrayDel0al20)

#9
#np.random.randint(entre,entre,cuantos)
aleatorios=np.random.randint(2,100,50)
print(aleatorios)

#10
valorMayor=aleatorios.max()
posValorMayor=aleatorios.argmax()
print(valorMayor,posValorMayor)

#11
#Poscion valor min
valorMenor=aleatorios.min()
posValorMin=aleatorios.argmin()
print(valorMenor,posValorMin)

#12 Diccionarios
diccionario={'Nombre': "Julio", 'Edad':19}
print(diccionario)
#13 
print(diccionario['Nombre'])
#14
print(diccionario['Edad'])
#15
print(diccionario.keys())
#16
print(diccionario.values())
#17
diccionario2=diccionario.copy()
#18
diccionario.clear()
print(diccionario)
print(diccionario2)