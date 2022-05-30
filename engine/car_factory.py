from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.battery.spindler_battery import  SpindlerBattery
from engine.battery.nubbin_battery import NubbinBattery
class CarFactory:
    def create_calliope(self,current_date,last_service_date,current_mileage,last_service_mileage):
        car = Car();
        car.engine = CapuletEngine(current_mileage,last_service_mileage)
        car.battery = SpindlerBattery(current_date,last_service_date)
        return car
    def create_glissade(self,current_date,last_service_date,current_mileage,last_service_mileage):
        car = Car();
        car.engine = WilloughbyEngine(current_mileage,last_service_mileage)
        car.battery = SpindlerBattery(current_date,last_service_date)
        return car
    def create_palindrome(self,current_date,last_service_date,warning_light_on):
        car = Car();
        car.engine = SternmanEngine(warning_light_on)
        car.battery = SpindlerBattery(current_date,last_service_date)
        return car
    def create_rorschach(self,current_date,last_service_date,current_mileage,last_service_mileage):
        car = Car();
        car.engine = WilloughbyEngine(current_mileage,last_service_mileage)
        car.battery = NubbinBattery(current_date,last_service_date)
        return car
    def create_thovex(self,current_date,last_service_date,current_mileage,last_service_mileage):
        car = Car();
        car.engine = CapuletEngine(current_mileage,last_service_mileage)
        car.battery = NubbinBattery(current_date,last_service_date)
        return car
if __name__ == "__main__":
    f = CarFactory()
    print(f.create_palindrome(3,2,True))


