""" #Declarando un arreglo
numeros = [10,20,30,40,50]

#imprimimos un elmento 
print(numeros[2])

#Reasignacion
numeros[3]= 35
print(numeros)

#Agregar un nuevo valor al final del arreglo
numeros.append(60)
print(numeros)

#Eliniamos unvlor delglo 
numeros.remove(35)
print(numeros)

#Eliminamos un valor del arreglo usando la funcion pop
numeros.pop(4)
print(numeros)

frutas = ["manzana", "freza", "sandia", "mango", "melon", "platano"]
frutas.pop(4)
print(frutas)

frutas.remove("manzana")
print(frutas)

#Declaracion de un arreglo vacio 
arreglo = []
print(arreglo)



n = int(input("ingrece el tamaño del arreglo: "))




for i in range(n):
    dato = int(input("ingrese un numero: "))
    arreglo.append(dato)


    print("El arreglo es:", arreglo)


    n = int(input("ingrese el tama;o del arreglo:"))
    print(n)


    arreglo = [0] * n

    for i in range(n):
        dato = int(input("ingrese un numero: "))
        arreglo[i] = dato


        print(arreglo)
 """


# Programa Cincuerizado
original = []
print("Introduce 15 numeros entre 0 y 500:")

for i in range(15):
    while True:
        try:
            num = int(input(f"Numero {i+1}: "))
            if 0 <= num <= 500:
                original.append(num)
                break
            else:
                print("Error: debe estar entre 0 y 500")
        except ValueError:
            print("Error: introduce un numero entero")

# Cincuerizar
cincuerizado = []
for n in original:
    if n % 5 == 0:
        cincuerizado.append(n)
    else:
        cincuerizado.append(n + (5 - n % 5))