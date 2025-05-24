# Alternativa a if anidados con polimorfismo
from abc import ABC, abstractmethod


# Ejemplo de logica que contiene if anidados
def logica(type):
    msg = "Hello World"
    if type == "email":
        print(f"Enviando email: {msg}")
    elif type == "sms":
        print(f"Enviando SMS: {msg}")
    elif type == "push":
        print(f"Enviando notificación push: {msg}")
    else:
        raise ValueError("Tipo de notificación no soportada")


logica("sms")


class Notification(ABC):
    @abstractmethod
    def send_notification(self, msg: str):
        pass


class SendEmail(Notification):
    def send_notification(self, msg: str):
        print("send {msg} by email")


class SendSms(Notification):
    def send_notification(self, msg: str):
        print(f"send {msg} by sms")


class SendPush(Notification):
    def send_notification(self, msg: str):
        print("send {msg} by push")


# ejemplo de logica que usa polimorfismo
def logica(notifier: Notification):
    notifier.send_notification(
        "Hello World"
    )  # usamos el mismo método para todos los tipos de notificaciones. Solo una línea


logica(SendSms())
