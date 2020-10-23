from exercise02 import Finanzas
"""
Ejercicio 02

finanzas personales (ingresos y egresos)

hacer un programa python para consola que le permita al usuario:

1. iniciar un proyecto de finanzas personales con cuenta a 0.00
2. dar opcion para registrar un ingreso o un egreso
3. si es un ingreso sumarlo a la cuenta
4. si es un egreso restarlo a la cuenta
5. verficar que si es un egreso y la cuenta esta a 0.0 debe aparecer
    el monto en negativo.
6. poder generar un reporte de todos los ingresos
7. poder generar un reporte de todos lo egresos
8. poder generar un reporte de todas las transacciones (ingresos y egreso)
9. poder generar un reporte solo de el total de la cuenta

restricciones del ejercicio:
el proyecto finanzas debe ser una clase, un ingreso debe ser una clase
y un egreso debe ser una clase tambien.

"""
print("Inicio de la aplicación FinanzasResponsables: \n")

exercise02Obj = Finanzas()
cuentaList = []

def showAllTransacciones():
    cuentaList = exercise02Obj.getAllMovimientos()
    print("\n")
    if len(cuentaList) > 0:
        for x in cuentaList:
            print(x)
        print("\n")
    else:
        print("\n**no hay transacciones por el momento**\n")

def showAllIngresos():
    ingresosList = exercise02Obj.getAllIngresos()
    print("\n")
    if len(ingresosList) > 0:
        for x in ingresosList:
            print(x)
        print("\n")
    else:
        print("\n**no hay ingresos por el momento**\n")

def showAllEgresos():
    egresosList = exercise02Obj.getAllEgresos()
    print("\n")
    if len(egresosList) > 0:
        for x in egresosList:
            print(x)
        print("\n")
    else:
        print("\n**no hay egresos por el momento**\n")

def createNewIngreso():
    print("Ingrese los siguientes datos: ")
    nombreAbono = input("Concepto del Ingreso: ")
    montoAbono = float(input("Monto del ingreso: "))
    exercise02Obj.newIngreso(nombreAbono, montoAbono)
    showAllIngresos()

def createNewEgreso():
    print("Ingrese los siguientes datos: ")
    nombreRetiro = input("Concepto del Egreso: ")
    montoRetiro = float(input("Monto del Egreso: "))
    exercise02Obj.newEgreso(nombreRetiro, montoRetiro)
    showAllEgresos()

def balanceCuenta():
    print("El saldo disponible en la cuenta es: \n")
    balance = exercise02Obj.getMontoTotal()
    print(balance)





while True:
    print("\n")
    print("Menu: \n")
    print("(0) salir")
    print("(1) registrar un ingreso")
    print("(2) registrar un egreso")
    print("(3) ver reporte de todos los ingresos")
    print("(4) ver reporte de todos los egresos")
    print("(5) ver reporte de las transacciones (ingresos y egresos)")
    print("(6) generar reporte del total disponible en la cuenta \n")
    opcion = int(input("opcion: "))

    if opcion == 0:
        print("Vuelva pronto \n")
        break
    elif opcion == 1:
        createNewIngreso()
    elif opcion == 2:
        createNewEgreso()
    elif opcion == 3:
        showAllIngresos()
    elif opcion == 4:
        showAllEgresos()
    elif opcion == 5:
        showAllTransacciones()
    elif opcion == 6:
        balanceCuenta()
    



