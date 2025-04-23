
"""#Ejercicio 1
# Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(101):
    print(i)"""
    
 
""" #Ejercicio 2
# Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

numero = input("Ingrese un numero entero: ")
dig = 0
for i in range(len(numero)):
    dig+=1
print(f"La cantidad de digitos que contiene el numero {numero} es {dig}.")
print(f"La cantidad de digitos que contiene el numero {numero} es {len(numero)}.")"""
 
"""#Ejercicio 3
# Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

numero1 = int(input("Ingrese un numero entero que sera el limite inferior: "))
numero2 = int(input("Ingrese un numero entero que sera el limite superior: "))
suma = 0
if numero1 > numero2:
    print("El limite inferior no puede ser mayor que el superior")
else:
    respuesta = input(f"Los numeros ingresados son {numero1} y {numero2}, es correcto? Si o No: ")
    respuesta.lower()
    if respuesta=="si":
        for i in range(numero1+1,numero2):
            suma += i
            print(f"El valor es {i} y la suma es {suma}")
            
        print(f"La suma de los numeros entre {numero1} y {numero2} es: {suma}.")
    
    else:
        print("Intente nuevamente")
"""

"""#Ejercicio 4
# Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

numero= ""
suma = 0

while numero != "0":
    numero = input("Ingrese un numero entero positivo: ")
    if numero.isdigit() and int(numero) > 0:
        suma += int(numero)
    elif numero=="0":
        print(f"El total de la suma es: {suma}.")
    else:
        print("Debe ingresar un numero entero positivo")"""

"""#Ejercicio 5
# Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.


import random #importar liberia random para poder usar el metodo randint
num_random = random.randint(0,9) #usando randint elejimos un nuero al azar entre 0 y 9 inclusive
adivinado = False
# print(num_random)
count = 1 #Inicializamos el contador de opotunidades en 1

print("Intente adivinar el numero entre 0 y 9.")
   
while adivinado == False: #mientras que la variable adivinado sea false se ejecuta el bucle
    user_choise = input(f"Intento n° {count}: ") #inicializamos la variable que contendra la eleccion del usuario y pedimos que ingrese 
    if not user_choise.isdigit() or int(user_choise) > 10 or int(user_choise) < 0: #evalua el valor ingresado. Si no es un numero, o esta fuera de rango salta al proximo bucle sin aumentar el contador
        print("Ingrese un valor correcto")
        continue
    else:
        user_choise=int(user_choise) # si el valor es valido, se convierte el str en int
    if user_choise==num_random: #evalua si la eleccion es la misma que el numero a adivinar
        print(f"Excelente, los adivinaste en {count} intentos") #si es correcto imprime el numero de intentos
        adivinado=True #cambia adivinado a True para que no se repita el cliclo 
    elif user_choise > num_random: #Da una pista si el numero es mayor o menor al numero a adivinar
        print("Pista: el numero es menor")
    else:
        print("Pista: el numero es mayor")
        
    count +=1 #aumenta el contador en 1"""
    
"""#Ejercicio 6
# Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for i in range(100,-1,-2):
    print(i)"""

"""#Ejercicio 7
# Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.
x = True
suma=0
while x==True:
    numero = input("Ingrese un numero positivo ")
    if not numero.isdigit() or int(numero) < 0:
        print("Valor invalido")
        continue
    else:
        numero = int(numero)
        for i in range(1,numero):
            suma+=i
            print(f"{i}- la suma hasta el momento es {suma}")
        x=False"""
        
"""#Ejercicio 8
# Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

import random

negativos = 0 #inicializa los contadores
positivos = 0
pares = 0
impares = 0

# numeros = [random.randint(-100,100) for i in range(100)] #generador de numeros al azar para probar

numeros = [] #inicializa la lista vacia donde almacenar los numeros generados

while len(numeros) <100: #mientras el tamaño de la lista sea menor a x se ejecuta el while
    print(len(numeros), "- ","Ingrese un numero entero, puede ser negativo o positivo: ") #ingresar los numeros de a 1
    x = input() #variable que toma el valor
    if x.lstrip("-").isdigit(): #evalua si x es un int pero antes le quita el signo negativo a los numeros negativos (si lo tiene)
        numeros.append(int(x)) #si es valido, lo agrega a la lista numeros
    else:
        print("Valor invalido.") #sino es valido vuelve al loop
        continue
        

print(numeros)

for i in range (len(numeros)): #for que itera el len de los numeros
    if numeros[i] >= 0: #evalua si el numero en la posicion i de la lista es igual o mayor a cero (positivo)
        positivos += 1 #si lo es, lo suma al contador
    else:
        negativos += 1 #si no es positivo, es negativo. Lo agrega al contador de negativos
    if numeros[i] % 2 == 0: #evalua si el numero es par y si lo es suma 1 al contador de pares
        pares += 1
    else:
        impares += 1 #si no es par, es impar. Suma 1 al contador
 #imprime la cuenta de los numeros pares, impares, positivos y nmegativos. 
print(f"Los numeros pares son {pares}")
print(f"Los numeros impares son {impares}")
print(f"Los numeros positivos son {positivos}")
print(f"Los numeros negativos son {negativos}")"""

"""#Ejercicio 9
# Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

#incializamos contador y suma
contador = 0 
suma = 0

#loop hasta acumular 10 en el cotador
while contador < 10:
    print(f"{contador + 1}- Ingrese un numero entero: ")
    x=input() #toma el valor ingresado por el usuario
    
    #Evalua si x es un numero entero pero antes le quita el signo negativo si lo tiene
    if x.lstrip("-").isdigit():
        suma += int(x) #si es correcto lo suma a la variable suma
        contador += 1 #y aumenta el contador em 1
    else:
        print("Incorrecto, ingrese un numero entero") #si no es conrrecto repite el loop

print(suma)    
print(f"La media de los valores ingresados es {suma/contador}")"""

"""#Ejercicio 10
# Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

#inicializamos las variables booleanas y la lista que contenedra los valores invertidos
negativo = False
valido = False
invertido = []

while not valido: #mientras valido sea falso se ejecuta el loop
    print("Ingrese un numero entero")
    numero = input() #ingreso del valor por el usuario
    
    if numero.lstrip("-").isdigit() and len(numero.lstrip("-")) >= 2: #evalua si el numero ingresado es un digito, quitando el signo primero, y despues evalua si tiene al menos 2 digitos sin contar el signo
        valido=True #si cumple, se sale del loop
        if int(numero) < 0: #evalua tambien si es negativo, si lo es le quita el signo y cambia a verdadero la bandera negativo
            negativo = True
            numero = numero.lstrip("-")
    else:
        print("valor incorrecto")

for i in range(len(numero) -1 , -1, -1): #recorre el largo del numero sin signo de derecha a izquierda para usar el indice
    invertido.append(numero[i]) #se inserta en el la variable invertido el numero en la posicion mas a la derecha y luego hacia la izquierda
#si ademas es negativo se vuelve a insertar el signo
if negativo:
    invertido.insert(0,"-")
    
#se imprime todo como un str
print("".join(invertido))"""


    