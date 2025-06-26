numeros = [[[1,2,3,4,5]],[[6,7,8,9,10]],[[11,12,13,14,15]]]

print("\n",sorted((numeros[0][0])+(numeros[1][0])+(numeros[2][0])))
print(sorted((numeros[0][0])+(numeros[1][0])+(numeros[2][0]), reverse=True),"\n")

def agregar_num(lista : list):
    list1 = []
    list2 = []
    cant = int(input("cuant numeros agregar: "))
    for i in range(cant):
        num_mum = int(input("ingrese los numeros que desea agregar: "))
        list1.append(num_mum)
        print("numero agregado exitosamente.")
    list1.append(list2)
    return lista.append(list2)

agregar_num(numeros)

print("\n",sorted((numeros[0][0])+(numeros[1][0])+(numeros[2][0])))
print(sorted((numeros[0][0])+(numeros[1][0])+(numeros[2][0]), reverse=True),"\n")