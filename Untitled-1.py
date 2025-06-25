# Lista de alumnos Duoc UC ses

Alumnos_AP = [
    [
        {
            "Nombre": ["Benjamin","Benjamin","Amaro"]
        }
    ],[
        {
            "Apellido": ["Andrade","Andres","Barria"]
        }
    ],[
        {
            "Correo": ["ben.andrade@duocuc.cl","ben.astudillo@duocuc.cl","am.barria@duocuc.cl"]
        }
    ]
]

Nombre = Alumnos_AP[0][0]["Nombre"]
Apellido = Alumnos_AP[1][0]["Apellido"]
Correo = Alumnos_AP[2][0]["Correo"]

for nom, ape, mem in zip(Nombre, Apellido, Correo):
    print(f"{nom} {ape}, Correo: {mem}")