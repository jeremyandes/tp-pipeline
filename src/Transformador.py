# Juan Andres Cherviere version 1 - Configurar patron de conception decorateur
import datetime

class Transformador:
    def __init__(self):
        pass

    def formatear(self, data, columna, tipo_formateo):
        if tipo_formateo == "mayusculas":
            valor_formateado = data[columna].upper()
        elif tipo_formateo == "minusculas":
            valor_formateado = data[columna].lower()
        elif tipo_formateo == "quitar_espacios":
            valor_formateado = data[columna].strip()
        elif tipo_formateo == "invertir":
            valor_formateado = data[columna][::-1]
        elif tipo_formateo == "fecha_dmy":
            fecha = datetime.datetime.strptime(data[columna], "%Y-%m-%d")
            valor_formateado = fecha.strftime("%d/%m/%Y")
        else:
            # Si el tipo de formateo no coincide con ninguna opción, no se realiza ninguna modificación
            valor_formateado = data[columna]

        data[columna] = valor_formateado
