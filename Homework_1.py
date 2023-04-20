#1. Создать класс Person с атрибутами fullname, age, is_married
#2. Добавить в класс Person метод introduce_myself, который бы распечатывал всю информацию о человеке
"""3. Создать класс Student наследовать его от класса Person и дополнить его атрибутом marks, который был бы словарем, где ключ это название урока, а значение - оценка.
4. Добавить метод в класс Student, который бы подсчитывал среднюю оценку ученика по всем предметам
5. Создать класс Teacher и наследовать его от класса Person, дополнить атрибутом experience.
6. Добавить в класс Teacher атрибут уровня класса salary
7. Также добавить метод в класс Teacher, который бы считал зарплату по следующей формуле: к стандартной зарплате прибавляется бонус 5% за каждый год опыта свыше 3х лет.
8. Создать объект учителя и распечатать всю информацию о нем и высчитать зарплату
9. Написать функцию create_students, в которой создается 3 объекта ученика, эти ученики добавляются в список и список возвращается функцией как результат.
10. Вызвать функцию create_students и через цикл распечатать всю информацию о каждом ученике с его оценками по каждому предмету. Также рассчитать его среднюю оценку по всем предметам.

"""
class Person:
    def __init__(self,fullname,age,is_married):
        self.fullname=fullname
        self.age=age
        self.is_married=is_married
    
    def introduce_myself(self):
        print(f"fullname=",self.fullname)
        print(f"age=",self.age)
        print(f"is_married=",self.is_married)

class Student(Person):
        def __init__(self, fullname, age, is_married,mark):
            Person.__init__(self,fullname, age, is_married)
            self.mark=dict(mark)

        def calculator(self):
          marks_sum=0
          values=self.mark.values()
          for mark in values:     
              marks_sum+=mark
          return marks_sum/len(values)
          
class Teacher(Person):
    def __init__(self, fullname, age, is_married,experience,salary):
          super().__init__(fullname, age, is_married)
          self.experience=experience
          self.salary=salary
    def teacher_salary(self):
        bonus=0
        if self.experience >=3:
           bonus=self.experience*5/100
           bonus=self.salary*bonus
           self.salary=self.salary+bonus
        return self.salary
              

My_teacher=Teacher(fullname="Aydar",age=15,is_married="no",experience=5,salary=1500)
print(f"fullname:{My_teacher.fullname}\nage:{My_teacher.age}\nis_married:{My_teacher.is_married}\nexperience:{My_teacher.experience}\nsalary={My_teacher.salary}")
print(My_teacher.teacher_salary())


def create_students():
    student1=Student(fullname="Aydar",age=15,is_married="no",mark={"Математика":2,"Физика":5,"English":4})
    student2=Student(fullname="Beka",age=16,is_married="no",mark={"Математика":3,"Физика":4,"English":2})
    student3=Student(fullname="Esentur",age=18,is_married="no",mark={"Математика":5,"Физика":5,"English":5})
    return (f"student#1 fullname:{student1.fullname}, age:{student1.age}, is_married:{student1.is_married}, mark:{student1.mark}"),(f"Student #2 fullname:{student2.fullname}, age:{student2.age}, is_married:{student2.is_married}, mark:{student2.mark}"),(f"Student#3 fullname:{student3.fullname}, age:{student3.age}, is_married:{student3.is_married}, mark:{student3.mark}")
print(create_students())
student1=Student(fullname="Aydar",age=15,is_married="no",mark={"Математика":2,"Физика":5,"English":4})
print(student1.calculator())
for i in create_students():
    print(i)




