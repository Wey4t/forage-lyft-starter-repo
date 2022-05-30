from tire.tires import Tires
class OctoprimeTires(Tires):
    def __init__(self, *worn):
        self.worn = list(worn)
    def needs_service(self):
        return sum(self.worn) >= 3
