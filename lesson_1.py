class Transport:
    def __init__(self,model,year,color):
        self.model=model
        self.year=year
        self.color=color       
    def change_color(self,new_color):
        self.color=new_color

class Plane:
    def __init__(self,color,model,year,winks_range):
        Transport.__init__(self,model,year,color)
        self.winks_range=winks_range
    def fly(self,contry):
        print("f{self.model}летит в {country}")


class Car(Transport):#Шаблон
    number_of_weels=4#Атрибуты\поля класса
    #__init__-Конструктор
    #model,yer,color-Входящие Параметры
    #self-ссылка на обьект
    #self.module-атрибуты обьекта или поля обЬекта
    def __init__(self,model,year,color,penalties=0):
        Transport.__init__(self,model,year,color)
        self.penalties=penalties

    def drive(self,city):#Метод
        print(f"{self.model} едет в {city}")

transport=Transport("Transport",2020,"Green")
print(Car.number_of_weels)

tesla_car=Car("Tesla Model X",2023,"White")
print(f"Model:{tesla_car.color},Year:{tesla_car.year},Color:{tesla_car.color},penalties:{tesla_car.penalties}")
tesla_car.color="Black"
print(f"Model:{tesla_car.color},Year:{tesla_car.year},Color:{tesla_car.color},penalties:{tesla_car.penalties}")
tesla_car.change_color("Blue")
print(f"Model:{tesla_car.color},Year:{tesla_car.year},Color:{tesla_car.color},penalties:{tesla_car.penalties}")
tesla_car.drive("Ош")
print(tesla_car.number_of_weels)



class Truck(Car):
    def __init__(self,color,model,year,penalties,load_capacity):
        Car.__init__(self,model,year,color,penalties)
        self.load_capacity=load_capacity
    def load_cargo(self,weiht):
        self_weiht=weiht
        if weiht>self.load_capacity:
            print("ты не можешь загрузить груз,груз превышает грузоподьемность")
        else:
            print("Груз загружен")
        

Car.number_of_weels=8
kamaz=Truck(model="kamaz",year=1999,color="red",load_capacity=12000,penalties=0.0)
print(f"Model:{kamaz.model},Year:{kamaz.year},Color:{kamaz.color},penalties:{kamaz.penalties}")
kamaz.drive("Бишкек")
print(kamaz.number_of_weels)
kamaz.load_cargo(12001)

