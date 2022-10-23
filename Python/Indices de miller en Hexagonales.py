#(El progama esta diseñado para el calculos de los indices de miller en la hexagonales), colocando las intersecciones en los
#ejes el progama, calculara los reciprocos y mostrara el indice de miller

#Introdución al progama

print("Para este progama esta diseñado para comprabar y calcular los indeces de miller hexagonales")
print("\t\nINDICES DE MILLER HEXAGONALES")
print("\n")
print("\nNOTA: Si el valor es un numero fraccional colocarlo en decimal (Ejemplo: 1/2 = 0.5)")
print("\nNOTA2: Si la intersección es en el infinito colocar: 100")

#Introducción de las intersecciones

print("\nIntroduzca el valor de las intersecciones")
a1 = float(input("\nIntroduce el valor de a1: "))
a2 = float(input("\nIntroduce el valor de a2: "))
a3 = float(input("\nIntroduce el valor de a3: "))
c =  float(input("\nIntroduce el valor de c: "))

#Reciprocos(Para esta parte se calcularan los reciprocos de las intersecciones)

h = 1/a1
k = 1/a2
i = 1/a3
l = 1/c

#Comprobación del indice de miller

valor1 = int(h) + int(k)
valor2 = -1*int(i)

#Impresión del indice

if valor1 == valor2:
 print("\n\n")
 print("\nEl indice de la hexagonal es correcto")
 print("\n\n")
 print("Intersecciones:(", float(a1), float(a2), float(a3), float(c),")")
 print("\nReciprocos:( 1/",float(a1)," ","1/",float(a2)," ","1/",float(a3)," ","1/",float(c),")")
 print("\nIndice de miller:(",int(h),int(k),int(i),int(l),")")
elif valor1 != valor2:
 print("\nEl indice de la hexagonal es incorrecto: Verificar las intersecciones")
      
input()
