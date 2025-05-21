# Definicion de funciones
def leer_entero_validado(mensaje, min=float("-Inf"), max=float("Inf")):
    numero = int(input(f"{mensaje}: "))
    while numero < min or numero > max:
        numero = int(input(f"Error! {mensaje}: "))
    return numero
def dibujar_matriz(ancho, alto, simbolo):
    for i in range(alto):
        for j in range(ancho):
            print(simbolo, end="")
        print("")
# Programa principal

ancho = leer_entero_validado("Ingrese un numero para el ancho", 1)
alto = leer_entero_validado("Ingrese un numero para el alto", 1)

dibujar_matriz(ancho, alto, "¬")

