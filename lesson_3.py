class MusicPlayMixin:
    @staticmethod
    def play_music(self,song):
        print(f"играет музыка:{song}")

class Car(MusicPlayMixin):
    def __init__(self,model,year) -> None:
        self.__model=model
        self.__year=year
    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self,model,value):
        self.__model=value

    @property
    def year(self):
        return self.__year
    
    @model.setter
    def model(self,year,value):
        self.__year=value

    def drive(self):
        print("I can drive!")

class ElectricCar(Car):
    def __init__(self, model, year,battery) -> None:
        Car.__init__(self,model, year)
        self.__battery=battery
    @property
    def battery(self):
        return self.__battery
    
    @battery.setter
    def model(self,__battery,value):
        self.__battery=value
    def drive(self):
        print("I can drive using electric engine")
    def __str__(self) -> str:
        return f"{self.model},{self.year},{self.battery}"
class FuelCar(Car):
    __total_fuel=500
    @classmethod
    def put_fuel(cls,car,amount):
        cls.__total_fuel-=amount
        car.fuel_amount+=amount
        print(f"Total fuel:{cls.__total_fuel}")
    @staticmethod
    def print_fuel_type():
            print("Ai 98")

    
    def __init__(self, model, year,fuel_amount) -> None:
        Car.__init__(self,model, year)
        self.__fuel=fuel_amount
    @property
    def fuel(self):
        return self.__fuel_amount
    
    @fuel.setter
    def model(self,value):
        self.__fuel_amount=value
    def drive(self):
        print("I can drive using fuel engine")
    def __str__(self) -> str:
        return f"{self.model},{self.year},{self.__fuel_amount}"
    def __add__(self,other):
        return"JJ"
    def __sub__(self,other):
        return self.year-other.year
class HybrydCar(FuelCar,ElectricCar):
        def __init__(self, model, year, battery,fuel) -> None:
            ElectricCar.__init__(self, model, year,battery)
            FuelCar.__init__(self, model, year,fuel)

hammer=FuelCar("hammer X-super",2015,100)
Tesla=ElectricCar("Tesla Mx",2020,80000)
prius=HybrydCar("M50",2020,5000,70)
BMW=FuelCar("hammer X-super",2015,100)
# hammer.drive()
# Tesla.drive()
# prius.drive()
# print(HybrydCar.mro())
# print(HybrydCar.__mro__)
# hammer.__fuel_amount(30)
# hammer.__fuel_amount(50)
 
# print(prius.__fuel_amount)
# HybrydCar.put_fuel(prius,50)
# print(prius.__fuel_amount)
# hammer.print_fuel_t

# print(BMW+prius+hammer)
print(BMW-hammer)
Tesla.play_music("god's plan")