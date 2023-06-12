# Juan Andres Cherviere version 2
import datetime

class Validador:
    def __init__(self, columnas_validar):
        self.columnas_validar = columnas_validar

    def validar(self, data):
        for columna in self.columnas_validar:
            if not hasattr(data, columna):
                raise ValueError(f"La columna {columna} no existe en el objeto Data.")
            valor = getattr(data, columna)
            if not self.validar_tipo(columna, valor):
                raise ValueError(f"El valor de la columna {columna} no cumple con el tipo de dato esperado.")
    
    def validar_tipo(self, columna, valor):
        # Si el tipo es válido, retorna True. De lo contrario, retorna False.
        if columna == "id":
            return isinstance(valor, int) and valor > 0
        elif columna == "fecha_inicial":
            return self.validar_fecha(valor)
        elif columna == "estado_encuesta":
            return valor in ['', 'Completa', 'Imposibilitada', 'De Prueba', 'En proceso']
        elif columna == "cantidad_personas":
            return isinstance(valor, int) and valor > 0
        else:
            # Si la columna no está definida en las condiciones anteriores, se considera válida 
            return True
    
    def validar_fecha(self, fecha):
        try:
            datetime.datetime.strptime(fecha, '%d/%m/%Y')
            return True
        except ValueError:
            return False
