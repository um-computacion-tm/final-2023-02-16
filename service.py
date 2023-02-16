from persona import Persona
from base import Base


class Service:

    def add(self, persona: Persona = None, base: Base = None):
        base.data[persona.id] = persona

    def order_by_fecha(self, base: Base = None):
        lista = []
        for persona in base.data.values():
            lista.append(persona)
        count = len(lista)
        for i in range(count - 1):
            for j in range(i + 1, count):
                if lista[i].nacimiento.compare_to(lista[j].nacimiento) > 0:
                    lista[i], lista[j] = lista[j], lista[i]
        return lista

    def order_by_apellido(self, base: Base = None):
        lista = []
        for persona in base.data.values():
            lista.append(persona)
        count = len(lista)
        for i in range(count - 1):
            for j in range(i + 1, count):
                if lista[i].apellido > lista[j].apellido:
                    lista[i], lista[j] = lista[j], lista[i]
        return lista