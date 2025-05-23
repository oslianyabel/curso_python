from enum import Enum

class Weekday(Enum):
    LUNES = 0
    MARTES = 1
    MIERCOLES = 2
    JUEVES = 3
    VIERNES = 4
    SABADO = 5
    DOMINGO = 6

    @classmethod
    def get_all(cls):
        return [tz.name for tz in cls]
    
    @classmethod
    def is_valid(cls, timezone_str):
        return any(timezone_str == tz.name for tz in cls)


print(Weekday.get_all())
print(Weekday.is_valid("LUNES"))
