cont = 0
num1 = int(input("Ingrese Primer numero: "))
if num1 % 2 == 0: 
    cont = cont + 1
num2 = int(input("Ingrese segundo numero"))
if num2 % 2 == 0:
    cont = cont + 1
num3 = int(input("Ingrese terer numero: "))
if num3 % 2 == 0:
    cont = cont + 1

print("La cantidad de numeros pares es ",cont)