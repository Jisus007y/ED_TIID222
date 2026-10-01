# PREGUNTA 1
print("=== PREGUNTA 1 ===")
numeros = [10, 20, 30, 40, 50]
print(numeros[2])
print()

# PREGUNTA 2
print("=== PREGUNTA 2 ===")
numeros = [10, 20, 30, 40, 50]
numeros[2] = 100
print(numeros)
print()

# PREGUNTA 3 - append(60)
print("=== PREGUNTA 3 - append(60) ===")
numeros = [10, 20, 30, 40, 50]
numeros.append(60)
print(numeros)

print("\n=== OPCIÓN 1 ===")
numeros = [10, 20, 30, 40, 50]
numeros.append([60, 70])
print(numeros)
print(numeros[5])
print(numeros[5][0])

print("\n=== OPCIÓN 2 ===")
numeros = [10, 20, 30, 40, 50]
numeros.append(60)
numeros.append(70)
print(numeros)
print()

# PREGUNTA 4 - insert()
print("=== PREGUNTA 4 - insert() ===")
numeros = [10, 20, 30, 40]
numeros.insert(2, 25)
print(numeros)
print()

# PREGUNTA 5 - Operador +
print("=== PREGUNTA 5 ===")
numeros = [10, 20, 30, 40]
numeros = numeros + [50]
print(numeros)

numeros = [10, 20, 30, 40]
numeros = numeros + [50, 60, 70]
print(numeros)
print()

# PREGUNTA 6 - extend()
print("=== PREGUNTA 6 ===")
numeros = [10, 20, 30]
otros_numeros = [40, 50, 60]
numeros.extend(otros_numeros)
print("numeros:", numeros)
print("otros_numeros:", otros_numeros)
print()

# PREGUNTA 7 - len() y rebanadas
print("=== PREGUNTA 7 ===")
numeros = [10, 20, 30]
print("Longitud:", len(numeros))
numeros[len(numeros):] = [40]
print(numeros)
print()

# EJERCICIO 1
print("===== EJERCICIO 1 =====")
calificaciones = [70, 85, 90, 65]
calificaciones.append(95)
calificaciones.insert(2, 80)
print(calificaciones)
print()

# EJERCICIO 2
print("===== EJERCICIO 2 =====")
colores = ["Azul", "Amarillo", "Rosa"]
colores.extend(["Verde", "Morado", "Rojo"])
colores.append("Negro")
print(colores)
print("Negro:", colores[-1])
print()

# EJERCICIO 3
print("===== EJERCICIO 3 =====")
numeros = [10, 20, 30, 40]
numeros.insert(2, 95)
numeros.extend([50, 67])
print("Arreglo:", numeros)
print("95:", numeros[2], "| Posición: 2")
print("67:", numeros[6], "| Posición: 6")