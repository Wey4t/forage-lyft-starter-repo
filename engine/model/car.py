from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, model, last_service_date):
        self.last_service_date = last_service_date

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()
