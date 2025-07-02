from os import system
system("cls")

Programa_funcionando = True
numeros = []
cont = 1

def agregar_num(lista: list, cont: int) -> int:
    list1 = [f"jugador {cont}", []]
    try:
        cant = int(input("Cuantos números desea agregar?: "))
    except ValueError:
        print("Ingresa un número válido.")
        return cont
    for i in range(cant):
        try:
            num_mum = int(input("Ingresa el número que deseas agregar: "))
        except ValueError:
            print("Valor inválido, intenta de nuevo.")
            continue
        list1[-1].append(num_mum)
        print("Número agregado exitosamente.")
    lista.append(list1)
    return cont + 1

def ver_numeros(lista: list) -> bool:
    if not lista:
        print("No se ingresaron números")
        return False
    print("\nListado de jugadores y sus números:")
    for jugador in lista:
        nombre = jugador[0]
        nums = jugador[1]
        print(f"{nombre}: {', '.join(map(str, nums))}")
    return True

def promedio_general(lista: list) -> None:
    try:
        total = 0
        cantidad = 0
        for jugador in lista:
            total += sum(jugador[1])
            cantidad += len(jugador[1])
        if cantidad == 0:
            print("No hay números para calcular el promedio.")
            return
        promedio = total / cantidad
        print(f"\nPromedio general de todos los puntos: {promedio:.2f}")
    except Exception as e:
        print("Error al calcular el promedio:", e)

def estadisticas(lista: list) -> None:
    try:
        todos_los_puntos = []
        for jugador in lista:
            todos_los_puntos.extend(jugador[1])
        if not todos_los_puntos:
            print("No hay números para analizar.")
            return
        media = sum(todos_los_puntos) / len(todos_los_puntos)
        sobresalientes = [n for n in todos_los_puntos if n > media]
        bajos = [n for n in todos_los_puntos if n < media]

        print(f"\nEstadísticas:")
        print(f"Media de todos los puntos: {media:.2f}")
        print(f"Valores sobresalientes (mayores a la media): {sobresalientes}")
        print(f"Valores por debajo del promedio: {bajos}")
    except Exception as e:
        print("Error al calcular:", e)

while Programa_funcionando:
    print("="*20, "MENÚ", "="*20)
    print("A) Agregar números.")
    print("B) Ver números.")
    print("C) Promedio general de puntos.")
    print("D) Estadísticas generales.")
    print("X) Salir del programa.")
    try:
        opc = input("Elija una opción: ").strip().upper()
    except:
        print("Hubo un error.")
        continue

    if opc == "A":
        cont = agregar_num(numeros, cont)
    elif opc == "B":
        ver_numeros(numeros)
    elif opc == "C":
        promedio_general(numeros)
    elif opc == "D":
        estadisticas(numeros)
    elif opc == "X":
        Programa_funcionando = False
    else:
        print("Opción inválida.")

print("Saliendo del programa.")

