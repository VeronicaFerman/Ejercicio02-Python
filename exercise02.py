class Ingresos():
    def __init__(self):
        self.ingresosList = []
        self.idCounter = 0

    def nuevoIngreso(self, nombreAbono, montoAbono):
        self.idCounter += 1
        movimientoId = self.idCounter
        movId = self.idCounter
        movimientoDict = {"id": movimientoId, "tituloAbono": nombreAbono, "monto": montoAbono}
        movimientoDict2 = {"id": movId, "tituloAbono": nombreAbono, "monto": montoAbono}
        self.ingresosList.append(movimientoDict2)
        return movimientoDict
    
    def mostrarTodosLosIngresos(self):
        return self.ingresosList

class Egresos():
    def __init__(self):
        self.egresosList = []
        self.idCounter = 0

    def nuevoEgreso(self, nombreRetiro, montoRetiro):
        self.idCounter += 1
        movimientoId = self.idCounter
        movId = self.idCounter
        movimientoDict = {"id": movimientoId, "tituloRetiro": nombreRetiro, "monto": montoRetiro}
        movimientoDict2 = {"id": movId, "tituloRetiro": nombreRetiro, "monto": montoRetiro}
        self.egresosList.append(movimientoDict2)
        return movimientoDict

    
    def mostrarTodosLosEgresos(self):
        return self.egresosList



class Finanzas(Ingresos,Egresos):
    def __init__(self):
        Ingresos.__init__(self)
        Egresos.__init__(self)
        self.montoTotal = 0.0
        self.cuentaList = []
        self.ingresosList = []


    def newIngreso(self, nombreAbono, montoAbono):
        herencia = self.nuevoIngreso(nombreAbono, montoAbono)
        self.cuentaList.append(herencia)
        self.montoTotal += montoAbono
        return self.cuentaList
        

    def getAllIngresos(self):
        return self.mostrarTodosLosIngresos()
    
    def newEgreso(self, nombreRetiro, montoRetiro):
        herencia = self.nuevoEgreso(nombreRetiro, montoRetiro)
        self.cuentaList.append(herencia)
        self.montoTotal = (self.montoTotal-montoRetiro)
        return self.cuentaList
    
    def getAllEgresos(self):
        return self.mostrarTodosLosEgresos()

    def getAllMovimientos(self):
        return self.cuentaList
    
    def getMontoTotal(self):
        return self.montoTotal

