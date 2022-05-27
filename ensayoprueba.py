#Definir variables
listaCliente = []
rut = ""
nombre = ""
direccion = ""
comuna = ""
correo = ""
edad = -1
genero = ""
celular =""
tipo =""
suscrito = True
opcion_2 = 0
opcion = 0
#Menu Principal 
while opcion != 4:
    print("**************  M E N Ú - JUAN MAESTRO  **************")
    print("1.- Registro")
    print("2.- Suscripción")
    print("3.- Consultar")
    print("4.- Salir")

    try:
        opcion = int(input("Ingrese la opción:")) 
    except:
        print("Error en el ingreso de la opción")
        input("Presione enter para continuar......")
        continue
        #Pedir informacion
    if opcion == 1:
        print("Seleccionó la opción 1")
        rut = int(input("Su rut sin puntos, sin guin ni digito verificador: "))
        sistema = rut + 1
        if rut > 4000000 and rut < 99999999: 
          nombre = input("Ingrese su nombre ")
          direccion = input("Ingrese su direccion: ")
          comuna = input("Ingrese su comuna:")
          correo = input("Ingrese su correo: ")
          edad = int(input("ingrese su edad: "))
          if edad > 0 and edad < 110:
            genero = input("Ingrese su edad M/F: ")
            genero.lower()
            celular = input("Ingrese su celular: ")
            tipo = input("Escriba su tipo de suscripcion 'PREMIUN' 'GOLD' 'SILVER': ")
            tipo.lower()

        #Opcion Suscripcion 
    elif opcion == 2:
        print("Seleccionó la opción 2")
        sub_rut = int(input("Ingrese el rut: "))
        suscripcion = []
        if sub_rut != rut:
            print("El usuario esta registrado en el sistema")
            fecha = input("Ingrese la fecha: ")



        #Opcion Consulta de datos
    elif opcion == 3:
        print("Seleccionó la opción 3")
        rut_mostrar = int(input("Ingrese su rut: "))
        if rut_mostrar == rut:
            print(f"El nombre es: {nombre}\n la direccion es: {direccion}\n La comuna es: {comuna}\n El correo es: {correo} La edad es: {edad}\n El genero es: {genero}\n El celular es: {celular}\n El tipo de sub es: {tipo}")

        #Opcion salir
    elif opcion == 4:
        print("Aplicación cerrada")

    
    input("Presione enter para continuar.....")


