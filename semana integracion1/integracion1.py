numero_user=int(input("Ingrese un numero decimal positivo para convertirlo: "))
numero=numero_user
# cifra_h=[]
hexa=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"] #lista de los valores hexa para buscarlos por el indice segun el valor de cada digito
opciones = str(input("Indique a que sistema quiere convertir el numero ingresado (B, O, H, Z): ")) #agregue la opcion Z
opciones = opciones.upper().strip()

if numero_user == 0: #si el valor es 0 devolvemos 0
    final_decimal, final_octal, final_hexa=0
    opciones="P" #condicional para un if asi no evalua nada mas quizas deberia ser el primer if
elif numero_user > 0: #no hace nada por ahora, queda como esta porque evaluaria nomarmalmente
    pass
elif numero_user < 0: #esto es lo que estoy probando ahora al final del codigo
    opciones=opciones+"N"
    print("pase por aca")
    


if opciones == "B" or opciones== "Z":
    resultado=[]
    numero=numero_user
    while numero>0:
        resultado.append(str(numero%2))
        numero=numero//2
    final_decimal=''.join(reversed(resultado))
    print(f"El numero decimal {numero_user} equivale a {final_decimal} en el sistema binario.") #separe cada resultado final para que cuando se piza "Z" se los pueda diferenciar
elif opciones == "O" or opciones== "Z":
    resultado=[]
    numero=numero_user
    while numero>0:
        resultado.append(str(numero%8))
        numero=numero//8
    final_octal=''.join(reversed(resultado))
    print(f"El numero decimal {numero_user} equivale a {final_octal} en el sistema octal.")
elif opciones == "H" or opciones== "Z":
    resultado=[]
    numero=numero_user
    while numero>0:
        cifra_h=numero%16
        numero=numero//16
        resultado.append(str(hexa[cifra_h])) #aca reemplazamos cada valor decimal por su igual en la lista hexa al comeinzo. Podria ser un diccionario pero como no vimos... cumple
    final_hexa="".join(reversed(resultado))
    print(f"El numero decimal {numero_user} equivale a {final_hexa} en el sistema hexadecimal.")
else:
    print("Opcion no válida")
    
if opciones=="BN": #intentanto hacer la conversion a binario de un negativo usando ca1 y ca2
    resultado=[]
    numero=abs(numero_user)
    print(numero)
    c1=[]
    while numero>0:
        resultado.append(str(numero%2))
        numero=numero//2
        final_decimal=''.join(reversed(resultado))
    print(final_decimal)
    for bit in final_decimal:
        if bit == "1":
            c1.append("0")
        else:
            c1.append("1")
    c1="".join(c1) #hasta aca es ca1
    print(c1)