from tires.tires import Tires


class Octoprimetires(Tires):
    def __init__(self,tire_wear_array):
        self.tire_wear_array = tire_wear_array

    def needs_service(self):
        for tire_wear in self.tire_wear_array:
            if tire_wear >= 3:
                return True
        return False
