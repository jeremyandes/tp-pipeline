class DataEncuentasPorParaje:
    paraje: str
    cantidad_encuestas: int

    def __init__(self, paraje: str, cantidad_encuestas: int):
        self.paraje = paraje
        self.cantidad_encuestas = cantidad_encuestas

    def get_as_dataframe(self):
        return [self.paraje, self.cantidad_encuestas]

    def get_columns_for_dataframe(self):
        return ["paraje", "cantidad_encuestas"]
