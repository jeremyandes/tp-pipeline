import Modulo


class Extractor(Modulo):
    def __init__(self, url_origen):
        self.url_origen = url_origen

    @staticmethod
    def create_instance(url_origen):
        return Extractor(url_origen)

    def execute(self, context):
        # TODO Implementar este metodo
        print("Extractor executed")
