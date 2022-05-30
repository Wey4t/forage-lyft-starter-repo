from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.spindler_battery import  SpindlerBattery
from battery.nubbin_battery import NubbinBattery
class CarFactory:
    def create_calliope(current_date,last_service_date,current_mileage,last_service_mileage):
        car = Car(last_service_date);
        car.engine = CapuletEngine(current_mileage,last_service_mileage)
        car.battery = SpindlerBattery(current_date,last_service_date)
        return car
    def create_glissade(current_date,last_service_date,current_mileage,last_service_mileage):
        car = Car(last_service_date);
        car.engine = WilloughbyEngine(current_mileage,last_service_mileage)
        car.battery = SpindlerBattery(current_date,last_service_date)
        return car
    def create_palindrome(current_date,last_service_date,warning_light_on:bool):
        car = Car(last_service_date);
        car.engine = SternmanEngine(warning_light_on)
        car.battery = SpindlerBattery(current_date,last_service_date)
        return car
    def create_rorschach(current_date,last_service_date,current_mileage,last_service_mileage):
        car = Car(last_service_date);
        car.engine = WilloughbyEngine(current_mileage,last_service_mileage)
        car.battery = NubbinBattery(current_date,last_service_date)
        return car
    def create_thovex(current_date,last_service_date,current_mileage,last_service_mileage):
        car = Car(last_service_date);
        car.engine = CapuletEngine(current_mileage,last_service_mileage)
        car.battery = NubbinBattery(current_date,last_service_date)
        return car
if __name__ == "__main__":
    f = CarFactory()
    print(f.create_palindrome(1231231232133,223,False).needs_service())


