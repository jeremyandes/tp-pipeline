from enum import Enum

class EstadoEncuesta(Enum):
    VACIA = ""
    COMPLETA = "Completa"
    IMPOSIBILITADA = "Imposibilitada"
    DE_PRUEBA = "De Prueba"
    EN_PROCESO = "En proceso"