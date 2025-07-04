from os import system
system("cls")

Programa_Activo = True
opc = 0
puntaje = 0

aventureros = {}

def registrar_aventureros(lst_aventureros:dict,codigo:str,datos:list)->bool:
    nombre,edad = datos
    if codigo not in lst_aventureros:
        lst_aventureros[codigo]={"nombre":nombre,"edad":edad,"puntajes":[]}
        return True
    else:
        return False

def registrar_puntaje(lst_aventureros:dict,codigo:str,puntaje:int)->bool:
    if codigo in lst_aventureros:
        lst_aventureros[codigo]["puntajes"].append(puntaje)
        if puntaje < 0:
            print("Error: No se pueden ingresar numeros negativos.")
            return True
        elif puntaje < 10:
            print("Error: El puntaje ingresado no es valido, el minimo a registrar es 10.")
            return True
    elif codigo not in lst_aventureros:
        print("Error: El codigo ingresado no se encuentra registrado.")
        return True
    return False

def modificar_puntaje(lst_aventureros:dict,codigo:str,sesion:int,nuevo_puntaje:int)->bool:
    if codigo not in lst_aventureros:
        print("Error: El código ingresado no se encuentra registrado.")
        return True
    if 0 <= sesion < len(lst_aventureros[codigo]["puntajes"]):
        lst_aventureros[codigo]["puntajes"][sesion] = nuevo_puntaje
        if nuevo_puntaje < 0:
            print("Error: No se pueden ingresar números negativos.")
            return True
        elif nuevo_puntaje < 10:
            print("Error: El puntaje ingresado no es válido, el mínimo a registrar es 10.")
            return True
    else:
        if sesion > len(lst_aventureros[codigo]["puntajes"]):
            print("Error: La sesión ingresada es mayor a las que están registradas.")
            return True
        elif sesion < 0:
            print("Error: No se pueden ingresar números negativos.")
            return True
    return False

def mostrar_participantes(lst_aventureros:dict)->None:
    for codigo,datos in lst_aventureros.items():
        nombre = datos["nombre"]
        puntajes = datos["puntajes"]
        total = sum(puntajes)
        promedio = total/len(puntajes) if puntajes else 0
        print(f"Nombre:{nombre}   Codigo:{codigo}   total:{total}   promedio:{promedio:.2f}")

while Programa_Activo:
    print("="*20,"MENU","="*20,"\n")
    print("""1. Registrar Aventureros.
2. Registrar Puntaje.
3. Modificar Puntaje.
4. Mostrar Aventureros.
0. Salir del Programa""")
    try:
        opc = int(input("Ingrese opcion:"))
    except:
        print("Valor ingresado invalido")
        continue
    if opc == 1:
        try:
            codigo = str(input("Ingrese el codigo del aventurero: "))
            nombre = str(input("Ingrese nombre del aventurero: "))
            edad = int(input("Ingrese edad del aventurero: "))
        except ValueError:
            print("Error: Debe llenar los campos correctamente.")
            continue
        registrar_aventureros(aventureros,codigo,[nombre,edad])
    elif opc == 2:
        while True:
            try:
                codigo = str(input("Ingrese el código del aventurero: "))
                puntaje = int(input("Ingrese el puntaje a agregar al aventurero: "))
                break
            except ValueError:
                print("Error: Debe llenar los campos correctamente.")
        registrar_puntaje(aventureros,codigo,puntaje)
    elif opc == 3:
        while True:
            try:
                codigo = str(input("Ingrese el código del aventurero: "))
                sesion = int(input("Ingrese cual sesion desea modificar: "))
                nuevo_puntaje = int(input("Ingrese el nuevo puntaje a cambiar para el aventurero: "))
                break
            except ValueError:
                print("Error: Debe llenar los campos correctamente.")
        modificar_puntaje(aventureros,codigo,sesion,nuevo_puntaje)
    elif opc == 4:
        mostrar_participantes(aventureros)
    elif opc == 0:
        print("Saliendo del programa...")
        Programa_Activo = False
    else:
        print("Opcion invalida. Intente Nuevamente.")
