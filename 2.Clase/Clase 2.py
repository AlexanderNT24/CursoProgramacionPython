#1
monto=int(input("Ingresa un monto:"))
precio=20
print("El precio del prodcuto es de ",precio)
if monto>=precio:
    print("Compra exitosa")
else:
    print("Necesita ingresar mas dinero")    
#2
palabra="Hola"
for i in range(10):
    print(palabra)
#3
numero=10
for i in range(numero):
    if i==7:
        print("Es el numero -->",i)
    else:
        print(i)   
#4 
lista=[1,2,3,4,5]
print(lista)
#5
lista=[1,2,3,4,5]
for i in lista:
    print(i)
#6
lista=[1,2,3,4,5]
print(lista)
lista.append(6)   
print(lista)
#7
lista=[1,2,3,4,5]
numero=lista.count(1)
print(numero)
#8
lista=[1,2,3,4,5]
tamanio=len(lista)
print(tamanio)
#9
def saludar():
    return "Hola a todos"
palabra=saludar()
print(palabra)

def sumar(a,b):
    return a+b
a=1
b=2  
suma=sumar(1,2) 
print(suma)    

def main():
    pass

if __name__ == "__main__":
    main()
#10
import Clase
Clase.metodo()  
import Clase as apodo
apodo.metodo()