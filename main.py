#sumar 3 numeros y la suma de los tres agregarlos a una lista y mostrar

lista = [] #aca cree una lista vacia
respuesta = True #aca hice esta variable booleana para el while de mas abajo

def suma(n1,n2,n3): #hice el metodo xd ingreso tres parametros luego pido q las sume
    r = n1 + n2 + n3#se guarda la suma en r
    lista.append(r)#se agrega la suma a la lista
    return lista#retorna la lista


while respuesta:#un while para preguntar al usuario tres digitos
    n1 = int(input("Ingrese numero 1: "))
    n2 = int(input("Ingrese numero 2: "))
    n3 = int(input("Ingrese numero 3: "))
    sum = suma(n1,n2,n3)#guardo en variable sum el resultado de la funcion
    print(sum)#imprimo la funcion
    opc = input("si desea terminar presione 'r', sino ENTER: ")#aca quize validar si quiere seguir el usuario digitando tees numeros...
    if opc == "r":#si presiona r
        respuesta = False#el bucle para puesto que esta en true... si da con R entonces hacemos parar el while sin ocupar un break por ejemplo
        print(f"Lista Concluye en: {lista}")#al terminar y darle que pare ... muestra la lista . veamos como funka