"""#Ejercicio 1
#  Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad=int(input("Ingrese su edad: ")) #ingreso de edad y convertir el valor a int para evaluar
if edad>=18: #evaluamos si edad es mayor o menor a 18
    print("Es mayor de edad.")"""

"""#Ejercicio 2
#  Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”

nota=int(input("Ingrese su nota: ")) #ingreso de la nota y convertir a int para evaluar
if nota >= 6: # se evalua si nota es mayor o igual a 6
    print("Aprobado.")
else:
    print("Desaprobado.")"""

"""#Ejercicio 3
# Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.

num=int(input("Ingrese un numero: ")) #ingreso de numero
if num%2==0: #evalua si el valor es par al calcular el resto de un num div por 2
    print("El numero es par") 
else:        #resultado si no es par
    print("El numero es impar")"""
    
"""#Ejercicio 4
# Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.

edad=int(input("Ingrese su edad: ")) #ingreso edad
if edad < 12:   #evalua si la edad es menor a 12
    print("Pertenece a la categoria: Niño/a")
elif edad < 18: #si la edad no es menor a doce pero si menor a 18
    print("Pertenece a la categoria: Adolescente")
elif edad < 30: #si la edad es mayor o igual a 18 pero menor que 30
    print("Pertenece a la categoria: Adulto/a joven")
else: #si la edad es mayor a 30
    print("Pertenece a la categoria: Adulto/a")"""

"""#Ejercicio 5
# Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.

print("Vamos a crear tu nueva contraseña!")
print("La nueva contraseña debe tener al menos 8 caracteres y como maximo 14.")

password=input("Ingrese la contraseña: ") #Ingreso de la nueva contraseña

if len(password)>=8 and len(password)<=14: #evalua si password es mayor o igual a 8 y menor o igual a 14 con el operador logico and
    print("La contraseña ingresada es correcta.") #valor si verdadero
else: 
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.") #valor si falso"""
    
"""#Ejercicio 6
# El paquete statistics de python contiene funciones que permiten tomar una lista de números
# y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el
# siguiente:
# from statistics import mode, median, mean
# mi_lista = [1,2,5,5,3]
# mean(mi_lista)
# En la documentación oficial se puede encontrar más información sobre este paquete:
# https://docs.python.org/es/3.8/library/statistics.html.
# La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
# pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
# ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
# mediana es mayor que la moda.
# ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
# la mediana es menor que la moda.
# ● Sin sesgo: cuando la media, la mediana y la moda son iguales.
# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
# Definir la lista numeros_aleatorios de la siguiente forma:
# import random
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de
# forma aleatoria.

from statistics import mode, median, mean
import random
muestra=[random.randint(1,10) for i in range(50)] #crea una lista de 50 num aleatorios entre 1 y 100
# print(muestra)
moda=mode(muestra)
mediana=median(muestra)
media=mean(muestra)

print(f'Media: {media}')
print(f'Moda: {moda}')
print(f'Mediana: {mediana}')
print(sorted(muestra))

if media==moda==mediana: #evaluamos sin sesgo
   print("Los datos no presentan sesgo") 
elif media > mediana and mediana > moda: # evaluamos sesgo positivo
    print("Los datos presentan un sesgo positivo")
elif media < mediana and mediana < moda: #evaluamos sesgo negativo
    print("Los datos presentan sesgo negativo")"""
    
"""#Ejercicio 7
# Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla

frase=input("Ingrese una frase: ").lower() #ingresa 
ultima_letra= frase[-1]
if ultima_letra=="a":
    print(frase+"!")
elif ultima_letra=="e":
    print(frase+"!")
elif ultima_letra=="i":
    print(frase+"!")
elif ultima_letra=="o":
    print(frase+"!")
elif ultima_letra=="u":
    print(frase+"!")
else:
    print(frase)

# vocales= ("a","e","i","o","u")
# x=False        
# while x==False:
#     if frase[-1]==vocales[i]:
#         frase=frase+"!"
#         x=True
#     else:
#         i+=1
    
#     if i==len(vocales):
#         x=True"""

"""#Ejercicio 8
# Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

print("Ingrese su nombre: ")
nombre=input()
print("Ingrese 1, 2 o 3 segun las siguientes opciones: ")
print("1 - Si quiere su nombre en mayúsculas.")
print("2 - Si quiere su nombre en minúsculas.")
print("3 - Si quiere su nombre con la primera letra en mayúscla.")

opcion=input()

if opcion=="1":
    print(nombre.upper())
elif opcion=="2":
    print(nombre.lower())
elif opcion=="3":
    print(nombre.title())
else:
    print("Opcion invalida")"""
    
"""#Ejercicio 9
# Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

print("Ingrese la maginitud del terremoto segun la escala Richter a partir de 0:")
mag=float(input())

if mag < 0:
    print("Magnitud no valida")
elif mag < 3:
    print("Muy Leve (Imperceptible)")
elif mag < 4:
    print("Leve (Ligeramente perceptible)")
elif mag < 5:
    print("Moderado (Sentido por personas pero generalmente no causa daños)")
elif mag < 6:
    print("Fuerte (Puede causar daños en estructuras débiles)")
elif mag < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")"""

"""#Ejercicio 10
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano

print("¿En qué emisferio se encuenta?")
print("Ingrese N para norte y S para sur")
emisferio = input().lower() #ingreso del emisferio y lo hace minusculas

print("Ingrese la fecha, para eso utilicemos el formato dd/mm")
fecha = input() #ingreso de fecha
dia,mes = fecha.split("/") #separar la fecha en dia y mes
dia=int(dia) #convertir a int
mes=int(mes) #convertir a int
# print(dia, mes)
periodo1= (dia >= 21 and mes == 12) or mes in [1,2] or (dia<=20 and mes== 3)  #perido 1 del 21 de dic a 20 de marzo, si emisferio norte entonces verano, si sur invierno

periodo2=(dia >=21 and mes ==3) or mes in [4,5] or (dia <= 20 and mes==6) #periodo de 21 de marzo a 20 de junio, si norte primavera, si sur otoño

periodo3= (dia >= 21 and mes ==6) or mes in [7,8] or (dia <= 20 and mes==9) #periodo de 21 de junio a 20 de septiembre, si norte verano si sur invierno

periodo4 = (dia >= 21 and mes == 9) or mes in [10,11] or (dia <= 20 and mes == 12) #periodo 21 de septiembre a 20 de diciembre, si norte otoño si sur primavera. 


if periodo1: #se evaluna periodo 1 y se resuelve con anidado
    if emisferio=="n": #se evalua solo norte, sino es sur
        print("Se encuentra en Invierno")
    else:
        print("Se encuentra en Verano")
elif periodo2:#evalua periodo 2
    if emisferio=="n":
        print("Se encuentra en Primavera")
    else:
        print("Se encuentra en Otoño")
elif periodo3: #evalua periodo3
    if emisferio=="n":
        print("Se encuentra en Verano ")
    else:
        print("Se encuentra en Invierno")
elif periodo4: #evalua periodo 4
    if emisferio=="n":
        print("Se encuentra en Otoño")
    else:
        print("Se encuentra en Primavera")
        
###resolucion usando operadores ternarios###
# if periodo1:
#     estacion="Invierno" if emisferio=="n" else "Verano"
# elif periodo2:
#     estacion="Primavera" if emisferio=="n" else "Otoño"
# elif periodo3:
#     estacion="Verano" if emisferio=="n" else "Invierno"
# elif periodo4:
#     estacion="Otoño" if emisferio=="n" else "Primavera"
    
# print(f'Se encuentra de la estacion: {estacion}')"""