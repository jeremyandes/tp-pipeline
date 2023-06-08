import datetime
# Comentario agregado

class Data:

    id: int
    fecha_inicial: datetime
    estado_encuesta: str
    paraje: str
    cantidad_personas: int

    def __init__(self, id, fecha_inicial, estado_encuesta, paraje, cantidad_personas):
        self.id = id
        self.fecha_inicial = fecha_inicial
        self.estado_encuesta = estado_encuesta
        self.paraje = paraje
        self.cantidad_personas = cantidad_personas

    def get(self):
        return self.id, self.fecha_inicial, self.estado_encuesta, self.paraje, self.cantidad_personas

    def get_id(self) -> int:
        return self.id

    def get_fecha_inicial(self) -> datetime:
        return self.fecha_inicial

    def get_estado_encuesta(self) -> str:
        return self.estado_encuesta

    def get_paraje(self) -> str:
        return self.paraje

    def get_cantidad_personas(self) -> int:
        return self.cantidad_personas

    def set_id(self, id: int):
        self.id = id

    def set_fecha_inicial(self, fecha_inicial: datetime):
        self.fecha_inicial = fecha_inicial

    def set_estado_encuesta(self, estado_encuesta: str):
        self.estado_encuesta = estado_encuesta

    def set_paraje(self, paraje: str):
        self.paraje = paraje

    def set_cantidad_personas(self, cantidad_personas: int):
        self.cantidad_personas = cantidad_personas

    def print_data(self):
        print("--------------------")
        print("id: ", self.id)
        print("fecha_inicial: ", self.fecha_inicial)
        print("estado_encuesta: ", self.estado_encuesta)
        print("paraje: ", self.paraje)
        print("cantidad_personas: ", self.cantidad_personas)
        print("--------------------")
