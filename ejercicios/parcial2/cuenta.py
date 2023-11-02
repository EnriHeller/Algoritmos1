class Cuenta:
    def __init__(self, apellido):
        self.apellido = apellido
        self.movimientos = []
        self.saldo = 0
    
    def acreditar(self, monto, motivo):
        self.movimientos.append(('acreditación',monto,motivo))
        self.saldo += monto

    def extraer(self, monto, motivo):
        if(monto > self.saldo):
            raise ValueError("Fondos insuficientes")
        else:
            self.movimientos.append(('extracción',monto,motivo))
            self.saldo -= monto

    def saldo(self):
        return self.saldo
    
    def movimientos(self):
        return self.movimientos
    
    """def transferir(self, monto, cuenta):
        """

