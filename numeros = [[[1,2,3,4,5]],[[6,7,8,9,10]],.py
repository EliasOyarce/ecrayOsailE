from os import system
system("cls")

Programa_funcionando = True

numeros = []
cont = 1  

def agregar_num(lista: list, cont: int) -> int:
    list1 = [f"jugador {cont}", []]
    try:
        cant = int(input("Cuantos numeros desea agregar?: "))
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
    else:
        print("\nListado de jugadores y sus números:")
        for jugador in lista:
            nombre = jugador[0]
            nums = jugador[1]
            print(f"{nombre}: {', '.join(map(str, nums))}")
    return True

while Programa_funcionando:
    print("="*20,"MENÚ","="*20)
    print("A) Agregar números.")
    print("B) Ver números.")
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
    elif opc == "X":
        Programa_funcionando = False
    else:
        print("Opción inválida, intenta nuevamente.")

print("Saliendo del programa.")
