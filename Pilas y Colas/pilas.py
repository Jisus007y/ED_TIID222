# Ejercicio 2 - PILAS

def menu_pila():
    pila = [] 

    while True:
        print("\n--- MENÚ PILA ---")
        print("1. Insertar en pila")
        print("2. Borrar en pila")
        print("3. Listar pila")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            numero = input("Ingresa un número para la pila: ")
            pila.append(numero) # append agrega arriba de la pila
            print(f"-> {numero} insertado en la pila.")

        elif opcion == "2":
            if len(pila) == 0:
                print("-> La pila está vacía, no hay nada que borrar.")
            else:
                eliminado = pila.pop() # pop() sin índice saca el ÚLTIMO elemento
                print(f"-> {eliminado} eliminado de la pila.")

        elif opcion == "3":
            if len(pila) == 0:
                print("-> La pila está vacía.")
            else:
                print(f"-> Pila actual: {pila}")
                print(f"-> Tope de la pila (último): {pila[-1]}")

        elif opcion == "4":
            break
        else:
            print("-> Opción no válida.")

    repetir = input("\n¿Deseas ejecutar nuevamente el programa? (s/n): ")
    if repetir.lower() == 's':
        menu_pila()
    else:
        print("Programa finalizado.")

menu_pila()