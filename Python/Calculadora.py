#Progama diseñado para hacer el calculo de funciones basicas

print("Hola bienvenido")
print("Esto es un calculadora")
print("Primero introduce que funcion deseas realizar")

print("1.. Sumar")
print("2.. Restar")
print("3.. Dividir")

opcion = int(input("Introduce la opcion a realizar: "))

if opcion == 1:
    n1 = float(input("Introduzca el numero 1: "))
    n2 = float(input("Introduzca el numero 2: "))

    suma = n1 + n2

    print("El resultado de la suma: ",suma)

if opcion == 2:
    n1 = float(input("Introduzca el numero 1: "))
    n2 = float(input("Introduzca el numero 2: "))

    resta = n1 - n2

    print("El resultado de la suma: ",resta)

if opcion == 3:
    n1 = float(input("Introduzca el numero 1: "))
    n2 = float(input("Introduzca el numero 2: "))

    division = n1/n2

    print("El resultado de la suma: ",division)

    

    