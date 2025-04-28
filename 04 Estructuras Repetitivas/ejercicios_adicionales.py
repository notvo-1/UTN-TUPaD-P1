"""#Ejercicio 1 - Bucle for para numeros pares

for i in range(2,21,2):
    print(i)"""

"""#Ejercicio 2 - Bucle while con suma acumulativa

suma = 0

while suma <=100:
    numero = input("Ingrese un numero entero positivo: ")
    if numero.isdigit():
        suma += int(numero)
    else: 
        print("Valor incorrecto")

print(f"La suma total es {suma}")"""

"""#Ejercicio 3 - Filtrar palabras por letra incial

palabras = "Avión arbol Amarillo abeja ancla Barco Búho Beso Bota Botón Casa Café Cielo Cebra Coco Dedo Dulce Duna Dardo Diosa Elefante Espejo Escoba Erizo Estrella Flor Fuego Fresa Farol Fila Gato Girasol Gema Golpe Grano Hola Huevo Hilo Hacha Horno Isla Iglú Imán Idea Inicio Jirafa Juego Jarra Joven Jabón Koala Kiwi Kilo Karma Ketchup Lápiz Luna Lago Lente Lomo Manzana Mesa Miel Mango Muro Nido Nube Nuez Nariz Nácar Oso Ola Ojo Ocho Ostra Perro Pelo Piso Puma Pozo Queso Quito Quena Quiso Queja Rosa Río Rana Risa Rayo Sol Sapo Silla Seta Saco Tigre Taza Tren Tomo Tiza Uva Uno Uña Urbe Uso Vaso Vino Vela Vaca Voz Waffle Waterpolo Windsurf Web Wifi Xilófono Xenón Xerografía Xenofobia Xerocopia Yogur Yate Yeso Yunque Yema Zorro Zapato Zanahoria Zumo Zigzag"
lista = palabras.split()

for i in lista:
    if i[0].lower() == "a":
        print(i)"""
 
"""#Ejercicio 4 - Tabla de multiplicar del 7

numero = input("Ingrese un numero entre el 1 y 10: ")
count = 0
tabla = []
for i in range(11):
    resultado = int(numero) * i
    # print(f"{count}- {numero} x {i} = {resultado}")
    count += 1
    tabla.append(f"{count}- {numero} x {i} = {resultado}")
 
print("\n".join(tabla))"""

"""#Ejercicio 5 - Contador de vocales

vocales = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
palabra = input("Ingrese una palabra: ").lower()

for i in palabra:
    if i in vocales.keys():
        vocales[i] += 1
    
for j in vocales.keys():
    print(f"{j}: {vocales[j]}")"""

#Ejercicio 6 - Numeros repetidos en una lista

# Objetivo: Filtrar elementos duplicados manteniendo el orden. Instrucciones:
# 1.
# Dada una lista (ej: [3, 1, 3, 5, 1]), crea una nueva lista con los números que aparecen más de una vez (en este caso: [3, 1]).





