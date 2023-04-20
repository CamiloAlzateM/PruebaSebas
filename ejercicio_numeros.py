# Programa que permita que el usuario ingrese un numero del 1 al 100, 
# si es par validar que el numero esté entre 0 y 6, si sí imprimir, hola,
# validar que el numero esté entre 5 y 21 para imprimir hola hermoso y 
# si es mayor o igual que 20 imprimir, que grande, si es impar, imprimir impar

numero = int(input("Ingrese un numero del 1 al 100, por favor:"))

if numero % 2 == 0:
    if numero >= 0 and numero <= 6:
        print("Hola")
    elif numero >= 20:
        print("Que grande")
else: 
    print("El numero es impar")
    if numero >= 5 and numero <= 21:
        print("Hola hermoso")

    
