"""1. Создать класс Computer (компьютер) с приватными атрибутами cpu и memory.

2. Добавить сеттеры и геттеры к существующим атрибутам.

3. Добавить в класс Computer метод make_computations, в котором бы выполнялись арифметические вычисления с атрибутами объекта cpu и memory.

4. Создать класс Phone (телефон) с приватным полем sim_cards_list (список симкард)

3. Добавить сеттеры и геттеры к существующему атрибуту.

4. Добавить в класс Phone метод call с входящим параметром sim_card_number и call_to_number, в котором бы распечатывалась симуляция звонка в зависимости от переданного номера сим-карты (например: если при вызове метода передать число 1 и номер телефона, распечатывается текст “Идет звонок на номер +996 777 99 88 11” с сим-карты-1 - Beeline).

5. Создать класс SmartPhone и наследовать его от 2-х классов Computer и Phone.

6. Добавить метод в класс SmartPhone use_gps с входящим параметром location, который бы распечатывал симуляцию проложения маршрута до локации.

7. В каждом классе переопределить магический метод __str__ которые бы возвращали полную информацию об объекте.

8. Перезаписать все магические методы сравнения в классе Computer, для того чтоб можно было сравнивать между собой объекты, по атрибуту memory.

9. Создать 1 объект компьютера, 1 объект телефона и 2 объекта смартфона

10. Распечатать информацию о созданных объектах

11. Опробовать все возможные методы каждого объекта (например: use_gps и тд.)"""
class Computer:
    def __init__(self,cpu,memory) -> None:
        self.__cpu=cpu
        self.__memory=memory
    @property 
    def cpu(self):
        return self.__cpu
    @cpu.setter
    def cpu(self,value):
        self.__cpu=value
    @property 
    def memory(self):
        return self.__memory
    @memory.setter
    def memory(self,value):
        self.__memory=value
    def make_computations(self):
        num1=self.__cpu
        operator=input("+,  -,  *,  /,  **:")
        num2=self.__memory
        if operator=="+":
             print(num1+num2)
        if operator=="-":
             print(num1-num2)
        if operator=="*":
            print(num1*num2)
        if operator=="/":
            print(num1/num2)
        if operator=="**":
            print(num1**num2)
    def __str__(self) -> str:
        return f"Процессор:{self.cpu},\nПамять:{self.memory}\n"
    
    def __sub__(self, other):
        return self.memory - other.memory
    
    def __mul__(self, other):
        return self.memory * other.memory

    def __gt__(self, other):
        return self.memory > other.memory

    def __lt__(self, other):
        return self.memory < other.memory
    
    def __ge__(self, other):
        return self.memory >= other.memory

    def __le__(self, other):
        return self.memory <= other.memory

    def __eq__(self, other):
        return self.memory == other.memory
    
    def __ne__(self, other):
        return self.memory != other.memory

    
class Phone:
    def __init__(self,sim_cards_list:list ) -> None:
        self.__sim_cards_list=sim_cards_list 
    @property
    def sim_cards_list(self):
        return self.__sim_cards_list
    @sim_cards_list.setter
    def sim_cards_list(self,value):
        self.__sim_cards_list=value
    def call(self,sim_card_number,call_to_number):
        return f"\nИдет звонок на номер {call_to_number}”,с сим-карты-{sim_card_number},{self.sim_cards_list[sim_card_number]}"
    def __str__(self) -> str:
        return f"\nСим.Карты:{self.sim_cards_list}\n"

class Smart_Phone(Computer,Phone):
    def __init__(self, cpu, memory,sim_cards_list:list) -> None:
        Computer.__init__(self,cpu, memory)
        Phone.__init__(self,sim_cards_list)
    def use_gps(self,location):
        return f"Вы сейчас находитесь {location}, для точки назначения поверните на права и пройдите 100 метров и поверните на лево пройдя 200 метров вы будете на точке назначения! "
    def __str__(self) -> str:
        return f"\nПроцессор:{self.cpu},\nПамять:{self.memory},\nСим.Карты:{self.sim_cards_list}\n"
phone=Phone(["0SIM не вложенна сим-карта!!!","1SIM-beeline","2SIM-Megacom"])
computer=Computer(5670,1024000)
Smart_Phone1=Smart_Phone(12700,256000,["SIM0-Не Вложенна сим-карта","1SIM-Megacom","SIM2-Beeline"])
Smart_Phone2=Smart_Phone(11700,128000,["SIM0-Megacom","1SIM-Beeline"])
print(phone)

print(computer)

print(Smart_Phone1)
print(Smart_Phone2)

print(phone.call(2,+996222000000))              #Проверка метода-сall
print(Smart_Phone2.call(1,+996222000000))

computer.make_computations() # при использовании make_computations атрибут cpu взоимодействует с атрибутом memory
Smart_Phone1.make_computations()                #Проверка метода-make_computations

print(Smart_Phone1.use_gps("London 96"))        #Проверка метода-use_gps
print(Smart_Phone2.use_gps("New York 76"))