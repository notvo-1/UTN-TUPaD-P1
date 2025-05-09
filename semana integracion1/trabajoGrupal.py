HEXA=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"] #lista de los valores hexa para buscarlos por el indice 

while True: #bucle para que el usuario ingrese un valor correcto
    opciones = input(
        "Indique a qué sistema quiere convertir el número ingresado:\n"
        "  B - Binario\n"
        "  O - Octal\n"
        "  H - Hexadecimal\n"
        "  Z - Todos los anteriores\n"
        "  D - Binario a Decimal\n"
        "  F - Salir\n"
        "-------------- \n"
        "Opción elegida: ").upper().strip()
    if opciones not in ("B", "O", "H", "Z", "D", "F"): #si el valor ingresado es un numero devolvemos error
        print("Opcion no valida, intente nuevamente.")
        print("-"*40)
        continue
    elif opciones == "F":
        print("Gracias por pasa!")
        print("-"*40)
        break
    
    if opciones in ("B", "O", "H", "Z"):
        print("Ingrese un numero entero positivo en base decimal para convertirlo.")
    
    elif opciones == "D":
        print("Ingrese un numero binario para convertirlo a decimal.")
    print("-"*40)
   
    
    while True:        
        numero_user=input("Numero --> ")
        
        print("-"*40)
        
        if opciones == "D":
            for _ in numero_user:
                if _ not in ("0","1"):
                    es_binario = False
                    break
                else:
                    es_binario = True
        
            if not es_binario:
                print("El numero no es binario, intente nuevamente")
                continue
            

        
        if not numero_user.isdigit(): #si el valor ingresado es un numero devolvemos error
            print("Eror!. Ingrese un numero entero positivo.")
            print("-"*40)
            continue
            
        elif int(numero_user) == 0: #si el valor es 0 devolvemos 0 luego de convertirlo a int
            print("El numero decimal 0 equivale a 0 en todos los sistemas.")
            print("-"*40)
            continue
        
        else:
            break
    
    # opciones = opciones.upper().strip() #lo saco porque ya formateo el str en el input

    
    numero=int(numero_user) #se convierte el str a int
    
    ############# BINARIO ###############
    if opciones in ("B", "Z"): 
        resultado=[]
        num = numero
        while num>0: #While donde se divide el numero entre 2 hasta obtener 0
            resultado.append(str(num%2))
            num=num//2
        binario=''.join(reversed(resultado)) #al final se joinea al revez
        
        
    ############# OCTAL ###############
    if opciones in ("O", "Z"): #Opcion octal
        resultado=[]
        num = numero
        while num>0: #while donde se divide el numero por 8 hasta que el numero sea menor a 0
            resultado.append(str(num%8))
            num=num//8 
        octal=''.join(reversed(resultado))
        
        
    ############# HEXADECIMAL ###############
    if opciones in ("H", "Z"): #Opcion hexadecimal
        resultado=[]
        num=numero
        while num > 0 : #while donde se divide el numero por 16 hasta que sea menor a cero
            cifra_h = num % 16
            num = num // 16
            resultado.append(str(HEXA[cifra_h]))
        hexadecimal = "".join(reversed(resultado))
        
        
    ############# BINARIO A DECIMAL ###############
    if opciones == "D":
        resultado_decimal = 0
        numero_binario = numero_user
        for posicion in range(len(numero_binario)):
            bit = numero_binario[-posicion+1]
            resultado_decimal += int(bit) * 2 ** posicion
            
            
    ############# IMPRESION DE RESULTADOS ###############
    print("#"*40)
    if opciones == "B":
        print(f"Decimal: {numero}")
        print(f"Binario: {binario}")
    elif opciones == "O":
        print(f"Decimal: {numero}")
        print(f"Octal: {octal}")
    elif opciones == "H":
        print(f"Decimal: {numero}")
        print(f"Hexadecimal: {hexadecimal}")
    elif opciones == "Z":
        print(f"Decimal: {numero}")
        print(f"Binario: {binario}")
        print(f"Octal: {octal}")
        print(f"Hexadecimal: {hexadecimal}")
    elif opciones == "D":
        print(f"Binario: {numero_binario}")
        print(f"Decimal: {resultado_decimal}")
    print("#"*40)
    
