class Empleado:
    # Aqui va el codigo del empleado
    """----------------------------
    Atributos 
    ----------------------------"""
    nombre = "pepito"
    apellido = "perez"
    """----------------------------
    # 1 = Masculino y 2 = Femenino
    ----------------------------"""
    sexo = 0
    salario = 1500000

    """----------------------------
    # Metodos
    ----------------------------"""

    def cambiarsalario(self, nuevoSalario):
        # Aqui va el codigo del metodo cambiar salario
        return 0
    
    def cambiarEmpleado(self, nNombre, nApellido, nSexo, nSalario):
        # Aqui va sl codigo del nuevo empleado
        return None
    
    def ConsultarSalario(self):
        # Aqui va el codigo del metodo
        return self.salario
    
    def consultarNombre(self):
        # Aqui va el codigo del metodo
        return self.nombre
    
    def ConsultarApellido(self):
        # Aqui va el codigo del metodo
        return self.apellido
    
    def ConsultarNombreCompleto(self):
        # Aqui va el codgo del metodo
        return self.nombre +" "+ self.apellido
    
    def AumentoSalario(self):
        nSalario = self.salario * 0.05
        nSalario = nSalario + self.salario
        self.salario = nSalario
        return "El Nuevo Salario es de "+self.salario

    def Duplicarsalario(self):
        # Aqui va el codigo del metodo
        # self.salario=self.salario*2
        # este es la asignacion de la forma uno
        self.salario *=2

    def SalarioAnual(self):
        #Aqui va el codigo del metodo
        self.salario *=12
        