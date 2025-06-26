import os 
os.system("cls")

# Lista de alumnos Duoc UC ses

Alumnos_AP = [
    {
        "Nombre": ["Benjamin","Benjamin","Amaro","Brian","Martin","Flavio","Benjamin","Bernardo","Williams","Claudio","Gerald","Sebastian","Javier","Jonathan","Elias","Matias","Juan","Felipe","Ignacio","Hans","Horacio","Martina","Cristobal","Dimas","Luis","Sebastian","Elias","Benjamin","Maximiliano","Alexis"]
    },{
        "Apellido": ["Andrade","Andres","Barria","Bravo","Burgos","Bustos","Campos","Cisternas","Cortes","Cordova","Cortes","Escalona","Gajardo","Garrido","Gonzalez","Guerra","Hernandez","Hernandez","Millar","Morales","Navarrete","Norambuena","Olivares","Opazo","Roa","Saez","San Martin","Santibañez","Segovia","Urrutia"]
    },{
        "Correo": ["ben.andrade@duocuc.cl","ben.astudillo@duocuc.cl","am.barria@duocuc.cl","bri.bravom@duocuc.cl","mar.burgosc@duocuc.cl","fl.bustos@duocuc.cl","ben.camposa@duocuc.cl","ber.cisternas@duocuc.cl","w.contreras@duocuc.cl","cla.cordovam@duocuc.cl","gera.cortes@duocuc.cl","s.escalona@duocuc.cl","ja.gajardon@duocuc.cl","jonat.garridos@duocuc.cl","elia.gonzalezm@duocuc.cl","mat.guerraj@duocuc.cl","juac.hernandez@duocuc.cl","felip.hernandezs@duocuc.cl","ig.millar@duocuc.cl","han.morales@duocuc.cl","ho.navarrete@duocuc.cl","mar.norambuenas@duocuc.cl","cr.olivaresm@duocuc.cl","dim.opazo@duocuc.cl","lu.roar@duocuc.cl","seb.saezr@duocuc.cl","el.sanmartin@duocuc.cl","be.santibañezn@duocuc.cl","max.segovia@duocuc.cl","al.urrutian@duocuc.cl"]
    }
]

# Se guardan en variables los diccionarios que vamos a usar

# Se busca "Nombre" en el diccionario que está en el indice 0 de la lista (Alumnos_AP)
Nombre = Alumnos_AP[0]["Nombre"]
# Se busca "Apellido" en el diccionario que está en el indice 1 de la lista (Alumnos_AP)
Apellido = Alumnos_AP[1]["Apellido"]
# Se busca "Correo" en el diccionario que está en el indice 2 de la lista (Alumnos_AP)
Correo = Alumnos_AP[2]["Correo"]

print("numero de alumnos ingresados", len(Nombre),"\n")
o = 1

for i in range(0, len(Nombre), 2):
    full1 = f"{cont}) {Nombre[i]} {Apellido[i]}"
    correo1 = Correo[i]
    bloque1 = f"{full1:<25} {correo1:<30}"
    o += 1

    if i + 1 < len(Nombre):
        full2 = f"{cont}) {Nombre[i+1]} {Apellido[i+1]}"
        correo2 = Correo[i+1]
        bloque2 = f"{full2:<25} {correo2:<30}"
        o += 1
    else:
        bloque2 = ""

    print(f"{bloque1}    {bloque2}")
print()