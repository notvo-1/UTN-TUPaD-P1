from math import pi

def leer_entero_validado_float(mensaje:str, min=float("-Inf"), max=float("Inf")) -> float:
    num = float(input(f"{mensaje}: "))
    while num < min or num > max:
        num = float(input(f"ERROR!. {mensaje}: "))
    return num

def leer_entero_validado_int(mensaje:str, min=float("-Inf"), max=float("Inf")) -> int:
    num = int(input(f"{mensaje}: "))
    while num < min or num > max:
        num = int(input(f"ERROR!. {mensaje}: "))
    return num

def tabla_multiplicar(numero):
    for i in range(11):
        print(f"{i} x {numero} = {numero * i}")
        
def segundos_a_horas(segundos:int)->float:
     return segundos / 3600
 
def hm():
    print("Hola Mundo!")
    
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")
    
def calcular_area_circulo(radio:float):
    return pi * radio**2       

def calcular_perimetro_circulo(radio:float):
    return pi * radio * 2 

def operaciones_basicas_tupla(a:int,b:int)->tuple:
    sum = suma(a,b)
    res = resta(a,b)
    mul = multiplicacion(a,b)
    div = division(a,b)
    return (sum, res, mul, div )

def suma(a:int, b:int):
    return a + b
def resta(a:int, b:int):
    return a - b
def multiplicacion(a:int, b:int):
    return a * b
def division(a:int, b:int):
    return a / b

def calcular_imc(altura, peso):
    altura = altura/100
    imc = peso / (altura**2)
    return imc

def celsius_a_fharenheit(celsius):
    fharenheit = (celsius * 9/5) + 32
    return fharenheit

def fharenheit_a_celsius(fha):
    celsius = (fha - 32)* 5/9
    return celsius

def calcular_promedio(a,b,c):
    promedio = (a + b + c) / 3
    return promedio

def ingresar_lista_numeros(mensaje):
    iterador = leer_entero_validado_int(mensaje,1)
    lista = []
    for i in range(1, iterador+1):
        num = leer_entero_validado_int(f"Ingresa el {i}/{iterador} numero, debe ser entero positivo", 1)
        lista.append(num)
    return lista

def promedio_lista(lista:list):
    suma = 0
    for i in lista:
        suma += i
    promedio = suma / len(lista)
    return promedio
