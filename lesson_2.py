class Address:
    def __init__(self,city,street,home_number) -> None:
                self.__city=city
                self.__street=street
                self.__home_number=home_number

    @property
    def city(self):
         return self.__city
    @city.setter
    def city(self,city):
         self.__city

class animal:
    def __init__(self,name,age,address1) -> None:
        if not name==str:
             raise Exception("Не верные данные!!!")
        if not age==int and age>1:
             raise Exception("Не верные данные!!!")
        if not type(address)==Address:
            raise Exception("Не верные данные!!!")
        else:
             raise Exception("Не верные данные!!!")
        self.__name=name#__ Скрывает атрибут если использовать внутри класса будет использоваться
        self.__age=age #public , private
        self.address=address1
        self.created
    def created(self):
         print("New animal is creat")

    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age

    def set_name(self,value):
        self.__name = value
    
    def set_age(self,value):
        if value>1:
            self.__age = value
        else:
            print("Значение не может быть меньше нуля")

    def info(self):
        print(f"Name:{self.get_name}\nAge:{self.get_age}\nadress:{address1}")


address1=Address("Bishkek","Ibraimova",103)

cat2=animal("Barsik",2,address1)

# class Dog (animal):
#      def __init__(self,name,age,address1) -> None:
#           super().__init__(name,age,address1)
#      def speak():
#           print("гав Гав")

# e=Dog("Barbos",2,address1,2)
# print(e)
print(cat2.get_name)
