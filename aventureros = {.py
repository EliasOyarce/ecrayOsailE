aventureros = {
    "COD133":{
        "nombre":"Elias",
        "edad":21,
        "puntajes":[90,50,120]
    },
    "COD134":{
        "nombre":"Horacio",
        "edad":30,
        "puntajes":[100,100,100]
    }
}

def registrar_aventureros(lst_aventureros:dict,codigo:str,datos:list)->bool:
    nombre,edad = datos
    if codigo not in lst_aventureros:
        lst_aventureros[codigo]={"nombre":nombre,"edad":edad,"puntajes":[]}
        return True
    return False

registrar_aventureros(aventureros,"COD135",["Hans",18])
registrar_aventureros(aventureros,"COD136",["Flavio",24])

def registrar_puntaje(lst_aventureros:dict,codigo:str,puntaje:int)->bool:
    if codigo in lst_aventureros:
        lst_aventureros[codigo]["puntajes"].append(puntaje)
        return True
    return False

registrar_puntaje(aventureros,"COD135",100)
registrar_puntaje(aventureros,"COD136",100)

def modificar_puntaje(lst_aventureros:dict,codigo:str,sesion:int,nuevo_puntaje:int)->bool:
    if codigo in lst_aventureros and 0 <= sesion < len(lst_aventureros[codigo]["puntajes"]):
        lst_aventureros[codigo]["puntajes"][sesion] = nuevo_puntaje
        return True
    return False

def mostrar_participantes(lst_aventureros:dict)->None:
    for codigo,datos in lst_aventureros.items():
        nombre = datos["nombre"]
        puntajes = datos["puntajes"]
        total = sum(puntajes)
        promedio = total/len(puntajes) if puntajes else 0
        print(f"{nombre}{codigo}-total:{total},promedio:{promedio:.2f}")

#for i,d in aventureros.items():
#    print(i,d)