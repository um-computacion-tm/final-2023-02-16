class Fecha:

    def __init__(self, anho: int = 2023, mes: int = 2, dia: int = 16):
        self.anho = anho
        self.mes = mes
        self.dia = dia

    def __repr__(self):
        return f'{self.dia}-{self.mes}-{self.anho}'

    def compare_to(self, fecha):
        esta_long = (self.anho * 100 + self.mes) * 100 + self.dia
        otra_long = (fecha.anho * 100 + fecha.mes) * 100 + fecha.dia
        if esta_long == otra_long:
            return 0
        if esta_long < otra_long:
            return -1
        return 1
