import Context


class Selector(Context):

    @staticmethod
    def create_instance():
        return Selector()

    def ejecutar(self, context):
        # TODO Implementar este metodo
        print("Selector executed")

    #False = alguna o varias filas con campos vacios
    #True = todas las filas son validas

    def fila_valida(self, fila):
        for dato in fila:
            if not dato:
                return False
        return True



