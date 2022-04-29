suma = 0
cont = 0
num1 = int(input("Ingrese el primer numero: "))
if num1 % 2 == 0:
    suma = suma + num1
elif num1 % 2 >= 1:
    cont = cont + 1
num2 = int(input("ingrese un segundo numero: "))
if num2 % 2 == 0:
    suma = suma + num2
elif num2 % 2 >= 1:
    cont = cont + 1
num3 = int(input("Ingrese un tercer numero: "))
if num3 % 2 == 0:
    sume = suma + num3
elif num3 % 2 >= 1:
    cont = cont + 1

print("La suma de los numeros pares es: ",suma)
print("El contador de impares es: ",cont)
