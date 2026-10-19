# Ejercicio 1 - COLAS

def menu_cola():
    cola = [] 

    while True:
        print("\n--- MENÚ COLA ---")
        print("1. Insertar cola")
        print("2. Borrar en cola")
        print("3. Listar cola")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            numero = input("Ingresa un número para la cola: ")
            cola.append(numero) # append agrega al final
            print(f"-> {numero} insertado en la cola.")

        elif opcion == "2":
            if len(cola) == 0:
                print("-> La cola está vacía, no hay nada que borrar.")
            else:
                eliminado = cola.pop(0) # pop(0) saca el PRIMER elemento
                print(f"-> {eliminado} eliminado de la cola.")

        elif opcion == "3":
            if len(cola) == 0:
                print("-> La cola está vacía.")
            else:
                print(f"-> Cola actual: {cola}")

        elif opcion == "4":
            break
        else:
            print("-> Opción no válida.")

    repetir = input("\n¿Deseas ejecutar nuevamente el programa? (s/n): ")
    if repetir.lower() == 's':
        menu_cola()
    else:
        print("Programa finalizado.")

menu_cola()