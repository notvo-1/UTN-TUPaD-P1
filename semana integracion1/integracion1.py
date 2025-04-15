numero=int(input("Ingrese un numero decimal para convertir a binario: "))
resultado=[]
while numero>0:
    resultado.append(str(numero%2))
    numero=numero//2

final=''.join(reversed(resultado))
print(final)
