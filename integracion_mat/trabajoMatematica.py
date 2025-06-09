entrada1 = input("Ingrese el número de documento del primer miembro: ")
entrada2 = input("Ingrese el número de documento del segundo miembro: ")

def digito_compartido(dni1:set, dni2:set):
    return True if dni1.intersection(dni2) else False

def suma_digitos(dni):
    if dni < 10:
        return dni
    else:
        return dni%10 + suma_digitos(dni//10)

def frecuencia_digito(cadena_numero):
    cadena_numero = sorted(cadena_numero)
    frecuencia = {}
    for digito in cadena_numero:
        if digito in frecuencia:
            frecuencia[digito] += 1
        else:
            frecuencia[digito] = 1
    return frecuencia

#DNI ordenados
entrada1_set = set(entrada1)
entrada2_set = set(entrada2)

print(f"Conjunto A = {sorted(entrada1_set)}")
print(f"Conjunto B = {sorted(entrada2_set)}")

#Frecuencia de digitos en DNI
frec_dni1 = frecuencia_digito(entrada1)
frec_dni2 = frecuencia_digito(entrada2)

print(f"La frecuencia de los digitos en el {entrada1} es:")
for i,j in frec_dni1.items():
    print(f"Digito {i}: {j} veces.")
    
print(f"La frecuencia de los digitos en el {entrada2} es:")
for i,j in frec_dni2.items():
    print(f"Digito {i}: {j} veces.")

#Suma de digitos de DNI recursivamente

print(f"La suma de los numeros del DNI {entrada1} es: {suma_digitos(int(entrada1))}")
print(f"La suma de los numeros del DNI {entrada2} es: {suma_digitos(int(entrada2))}")

#Operaciones de conjuntos 
interseccion = entrada1_set.intersection(entrada2_set)
union = entrada1_set.union(entrada2_set)
diferencia = entrada1_set.difference(entrada2_set)
diferencia2 = entrada2_set.difference(entrada1_set)
diferenciaSimetrica = entrada1_set.symmetric_difference(entrada2_set)

print(f"A U B = {sorted((union))}")
print(f"A ∩ B = {sorted(interseccion)}")
print(f"A - B = {sorted(diferencia)}")
print(f"B - A = {sorted(diferencia2)}")
print(f"A Δ B = {sorted(diferenciaSimetrica)}")

#Evaluacion de condiciones logicas
condicion1= entrada2_set.difference(interseccion) #Si A contiene a todos los elementos de B excepto 1
if len(condicion1)==1:
    print(f"El conjunto {sorted(entrada1_set)} es una extencion del conjunto {sorted(entrada2_set)}")

condicion2= entrada1_set.intersection(entrada2_set) #Si la interseccion AyB tiene al menos 3 elementos
if len(condicion2)>= 3:
    print("Los conjuntos son coincidencias significativas")

condicion3 = digito_compartido(entrada1_set, entrada2_set)
if condicion3:
    print("Tiene digitos compartidos")


#### B. Operaciones con años de nacimiento ###

# year1 = 1989
# year2 = 2000

# """"·         Ingreso de los años de nacimiento (Si dos o mas integrantes del grupo tienen el mismo año, ingresar algún dato ficticio, según el caso).

# ·         Contar cuántos nacieron en años pares e impares utilizando estructuras repetitivas.

# ·         Si todos nacieron después del 2000, mostrar "Grupo Z".

# ·         Si alguno nació en año bisiesto, mostrar "Tenemos un año especial".

# ·         Implementar una función para determinar si un año es bisiesto.

# ·         Calcular el producto cartesiano entre el conjunto de años y el conjunto de edades actuales."""

# def contar_par(years):
#     par = 0
#     impar = 0
#     for i in years:
#         if i % 2 == 0:
#             par += 1
#         else:
#             impar += 1
#     return par, impar

# def grupo_z(years):
#     for i in years:
#         if i < 2000:
#             return False
#     return True

# def bisiesto(years):
#     for year in years:
#         if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#             return "Tenemos uno especial"
#     return "Ninguno es biciesto"

# def calcular_edad(year):
#     return 2025-year

# def producto_carteciano(con1, con2):
#     con1 = sorted(con1)
#     con2 = sorted(con2)
#     return[(x,y) for x in con1 for y in con2]

# years = (year1, year2)
# # print(years)

# contar_pares_impares = contar_par(years)
# print(f"La cantidad de años pares e impares en {years}es: ")
# print("Pares:", contar_pares_impares[0])
# print("Impares:", contar_pares_impares[1])

# # Grupo z

# if grupo_z(years):
#     print("Grupo Z")
    
# # Bisiesto

# print(bisiesto(years))

# # Producto cartesiano

# print(producto_carteciano(set(str(year1)), set(str(year2))))