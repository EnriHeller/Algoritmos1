class Angulo:
    def __init__(self,grado, minuto, segundo) -> None:

        if 0 <= minuto <= 59 and 0 <= segundo <= 59:
            self.grado = grado
            self.minuto = minuto
            self.segundo = segundo
        else:
            raise ValueError("El ángulo es inválido")
        
    
    def __str__(self) -> str:
        return f"{self.grado}°, {self.minuto}', {self.segundo}''"
    
    def sumar_segundos(self, segs):
        if segs > 0:
            minutos = segs / 60
            segundos = segs % 60
            self.minuto += minutos
            self.segundo += segundos
        else:
            raise ValueError("No se puede restar segundos")
