# Definicion de funciones
def leer_entero_validado(mensaje, min=float("-Inf"), max=float("Inf")):
    numero = int(input(f"{mensaje}: "))
    while numero < min or numero > max:
        print(f"Error! {mensaje}: ")
    return numero
def informar_es_perfecto(numero):
    if es_perfecto(numero):
        print(f"El numero {numero} es perfecto")
    else: 
        print(f"El numero {numero} NO es perfecto")
        
def informar_solo_perfecto(numero):
    if es_perfecto(numero):
        print(f"El numero {numero} es perfecto")

def es_perfecto(numero):
    mitad = numero//2
    suma=0
    multiplos = []
    for i in range(1, mitad+1):
        if es_multiplo(numero, i):
            suma+=i
        #     multiplos.append(i)
        # if i in multiplos:
        #     print(f"Probando divisor: {i}", end='\r', flush=True)
    return numero == suma and numero != 0

def es_multiplo(num1, num2):
    resto=num1%num2
    return resto == 0



# Programa principal
for i in range(1000000):
    informar_solo_perfecto(i)

# num = leer_entero_validado("Ingrese un numero entero positivo", 1)
# informar_es_perfecto(num)