from base import Base
from persona import Persona
from fecha import Fecha
from service import Service

if __name__ == '__main__':
    base = Base()
    service = Service()

    service.add(Persona(5, 'Perez', Fecha(2022, 3, 14)), base)
    service.add(Persona(2, 'Gomez', Fecha(2024, 6, 1)), base)
    service.add(Persona(1, 'Diaz', Fecha()), base)
    service.add(Persona(4, 'Zen', Fecha(1995, 11, 11)), base)

    order_by_fecha = service.order_by_fecha(base)
    print(order_by_fecha)

    order_by_apellido = service.order_by_apellido(base)
    print(order_by_apellido)
