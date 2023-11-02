class CajaFuerte:
    '''
    DOC: Completar
    '''

    def __init__(self, clave):
       self.clave = clave
       self.abierta = False
       self.objeto = ""

    def esta_abierta(self):
        return self.abierta
    
    def guardar(self, objeto):
        if not self.abierta:
            raise Exception("La caja fuerte está cerrada")
        else:
            self.objeto = objeto
    
    def abrir(self, clave):
        if(clave != self.clave):
            raise Exception("La clave es invalida")
        else:
            self.abierta = True
        
    def sacar(self):
        if(self.objeto == ""):
            raise Exception("No hay nada para sacar")
        else:
            self.objeto = ""

    