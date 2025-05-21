#definicion de funciones
def leer_entero_validado(mensaje, min=float("-Inf"), max=float("Inf")):
    num = int(input(f"{mensaje}: "))
    while num < min or num > max:
        num = int(input(f"ERROR!. {mensaje}: "))
    return num

def informar_si_numero_es_primo(numero):
    if es_primo(numero):
        print(f"El numero {numero} es primo")
    else:
        print(f"El numero {numero} NO es primo")

def es_primo(numero):
    cont = 2
    mitad = numero // 2
    while cont <= mitad and not es_multiplo(numero, cont) :
        cont += 1
    return cont > mitad
        
def obtener_resto(num1, num2):
    return num1 - num2 *(num1//num2)

def es_multiplo(num1, num2):
    return obtener_resto(num1, num2) == 0
    
#Programa principal
num = leer_entero_validado("Ingrese un numero entero positivo", 1)
informar_si_numero_es_primo(num)