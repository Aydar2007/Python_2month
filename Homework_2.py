"""1. Создать класс Figure (фигура) с атрибутом уровня класса unit (единица измерения величин) и присвоить ему значение cm (сантиметры) или mm (миллиметры)

2. В конструкторе класса Figure должен быть только 1 входящий параметр self, то есть не должно быть атрибутов уровня объекта.

3. Добавить в класс Figure нереализованный публичный метод calculate_area (подсчет площади фигуры)

4. Добавить в класс Figure нереализованный публичный метод info(вывод полной информации о фигуре)

5. Создать класс Circle (круг), наследовать его от класса Figure.

6. Добавить в класс Circle атрибут radius (радиус круга), атрибут должен быть приватным.

7. В классе Circle переопределить метод calculate_area, который бы считал и возвращал площадь круга.

8. В классе Circle переопределить метод info, который бы распечатывал всю информацию о круге следующим образом: Например - Circle radius: 2cm, area: 12.57cm.

9. Создать класс RightTriangle (прямой треугольник - 90 градусов), наследовать его от класса Figure.

10. Добавить в класс RightTriangle атрибут side_a (сторона а) и side_b (сторона б), атрибуты должны быть приватными.

11. В классе RightTriangle переопределить метод calculate_area, который бы считал и возвращал площадь треугольника.

12. В классе Triangle переопределить метод info, который бы распечатывал всю информацию о треугольнике следующим образом:Например - RightTriangle side a: 5cm, side b: 8cm, area: 20cm.

13. В исполняемом файле создать список из 2-х разных кругов и 3-х разных треугольников

14. Затем через цикл вызвать у всех объектов списка метод info"""
class Figure:
        unit="cm"

        def __init__(self) -> None:
                pass
        def calculate_area():
                pass
        def info():
                pass
class Circle(Figure):
        def __init__(self,radius) -> None:
                Figure.__init__(self)
                self.__radius=radius
        def calculate_area(self):
                area1=self.__radius**2
                area=area1*3.14
                return area
        def info(self):
            return f"Circle   radius:{self.__radius},  area:{self.calculate_area()}{self.unit}"

class RightTriangle(Figure):
        def __init__(self,side_a,side_b) -> None:
                Figure.__init__(self)
                self.__side_a=side_a
                self.__side_b=side_b
        def calculate_area(self):
                area=self.__side_a*self.__side_b/2
                return area
        def info(self):
            return f"RightTriangle    side a={self.__side_a}, side b={self.__side_b} ,area:{self.calculate_area()}{self.unit}"
                        
Circle_A=Circle(3)
Circle_B=Circle(4)
triangle1=RightTriangle(2,3)
triangle2=RightTriangle(4,5)
triangle3=RightTriangle(6,8)
Figure_areas=[Circle_A,Circle_B,triangle1,triangle2,triangle3]
for Figure in Figure_areas:
       print(Figure.info())




