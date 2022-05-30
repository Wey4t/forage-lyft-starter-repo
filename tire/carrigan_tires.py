from tire.tires import Tires
class CarriganTires(Tires):
    def __init__(self, *worn):
        self.worn = list(worn)
    def needs_service(self):
        return max(self.worn) >= 0.9
