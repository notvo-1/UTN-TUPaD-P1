# ###Actividad-1###

# print("Hola Mundo")

# ###Actividad-2###

# nombre=input("Ingrese su nombre ")
# print(f"Hola {nombre}!")

# ###Actividad-3###
# print("-"*60)
# print("Hola, vamos a pedirte que ingreses tus datos.")
# print("-"*60)
# nombre=input("Ingrese su nombre ---> ")
# apellido=input("Ingrese su apellido ---> ")
# edad=input("Ingrese su edad ---> ")
# residencia=input("Ingrese su lugar de residencia---> ")
# print("-"*60)
# print(f"Hola, soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# ###Actividad-4###

# from math import pi

# print("-"*60)
# print("--Calculo de área y perímetro de un circulo--")
# radio=float(input("Ingrese el radio de del circulo a calcular en centimetros (cm)---> "))
# area_circulo= pi*radio**2
# perimetro_circulo= 2*pi*radio
# print(f"Para un circulo de radio {radio}cm: su area es {area_circulo:.2f} cm2 y su perimeto es {perimetro_circulo:.2f} cm.")

###Actividad-5###
# print("-"*60)
# seg=int(input("Ingrese una cantidad de segundos cualquiera para que podamos calcular a cuantas horas equivale --->"))
# horas=seg/3600
# print(f"Entonces: {seg} segundos equivalen a {horas:.2f} horas")
# print("-"*60)

###Actividad-6###

# print("-"*60)
# num=int(input("Ingrese un numero para que calculemos la tabla correspondiente---> "))
# for i in range(1,11):
#     print(f"{num} x {i} = {i*num}")
#     i+=i
# print("-"*60)

###Actividad-7###

# print("-"*60)
# print("Ingrese dos numero distintos de cero.")
# num1=int(input("Ingrese el numero 1, recorda que sea distinto de cero."))
# num2=int(input("Ingrese el numero 2, recorda que sea distinto de cero."))
# suma=num1+num2
# resta1=num1-num2
# resta2=num2-num1
# div1=num1/num2
# div2=num2/num1
# mult=num1*num2
# print(f"Para los numeros {num1} y {num2} los resultados son:")
# print(f"Suma {num1}+{num2}={suma}")
# print(f"Resta {num1}-{num2}={resta1} y {num2}-{num1}={resta2}")
# print(f"Division {num1}/{num2}={div1:.2f} y {num2}/{num1}={div2:.2f}")
# print(f"Multiplicacion {num1}*{num2}={mult}")
# print("-"*60)

###Actividad-8###

# print("-"*60)
# print("Vamos a pedirte tu altura en metros y tu peso en kilos para calcular tu IMC.")
# altura=float(input("Ingresa tu altura en metros separando los decimales con un punto: "))
# peso=float(input("Ingresa tu peso en kilos separando los decimales con un punto: "))
# imc=peso/altura**2
# print(f"Tu IMC para una altura de {altura} metros y un peso de {peso} kilos es: {imc:.2f}")
# print("-"*60)

###Actividad-9###

# print("-"*60)
# celcius=float(input("Ingrese la temperatura en grados celcius: "))
# fah=(9/5)*celcius+32
# print(f"La temperatura en fahrenheit para {celcius}° celcius es de {fah}° fahrenheit.")
# print("-"*60)

###Actividad-10###

print("-"*60)
print("Vamos a pedirle 3 numeros enteros para calcular el promedio entre ellos.")
num1=int(input("Ingrese el primer numero entero: "))
num2=int(input("Ingrese el segundo numero entero: "))
num3=int(input("Ingrese el tercer numero entero: "))
prom=(num1+num2+num3)/3
print(f"El promedio entre los numeros {num1}, {num2} y {num3} es {prom:0.2f}.")
print("-"*60)