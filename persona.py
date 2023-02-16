from fecha import Fecha


class Persona:

    def __init__(self, id: int = None, apellido: str = '', nacimiento=Fecha()):
        self.id = id
        self.apellido = apellido
        self.nacimiento = nacimiento

    def __repr__(self):
        return f'{self.id} - {self.apellido} / {self.nacimiento}'
