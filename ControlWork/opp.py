#  1. Инкапсуляция
#Задание:
#Создайте класс Person, который будет представлять человека.

#Требования:

     #- У класса должен быть приватный атрибут _age (возраст).
     #- Создайте методы для установки (set_age(age)) и получения (get_age()) возраста.
     #- Убедитесь, что возраст не может быть отрицательным (добавьте проверку).

   # Пример использования: 
        #p = Person()
        #p.set_age(25)
        #print(p.get_age())  # Вывод: 25
        #p.set_age(-5)  # Должна быть ошибка или предупреждение
class Person:
    def __init__(self):
        self._age = 0
    
    def set_age(self, age):
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным")
        self._age = age
    
    def get_age(self):
        return self._age

if __name__ == "__main__":
    p = Person()
    p.set_age(25)
    print(p.get_age())
    try:
        p.set_age(-5)
    except ValueError as e:
        print(f"Ошибка: {e}")

#2. Наследование
#Задание:
#Создайте класс Animal и два наследника: Dog и Cat.

#Требования:

     #- У класса Animal должен быть атрибут name и метод speak(), который возвращает строку "I am an animal".
     #- У класса Dog метод speak() должен возвращать "Woof".
     #- У класса Cat метод speak() должен возвращать "Meow".

#Пример использования:
#dog = Dog("Buddy")
#cat = Cat("Kitty")

#print(dog.name, dog.speak())  # Вывод: Buddy Woof
#print(cat.name, cat.speak())  # Вывод: Kitty Meow

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I am an animal"

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

dog = Dog("Buddy")
cat = Cat("Kitty")

print(dog.name, dog.speak())
print(cat.name, cat.speak())

#  3. Полиморфизм
#Задание:
#Создайте несколько классов, которые будут представлять разные виды транспорта, и функцию move(vehicle), которая вызывает общий метод move() у переданного объекта.

#Требования:

     #- Создайте базовый класс Vehicle с методом move(), который возвращает строку "Vehicle is moving".
     #- Создайте два дочерних класса Car и Bicycle, которые переопределяют метод move().
     #- У Car метод возвращает "Car is driving".
     #- У Bicycle метод возвращает "Bicycle is pedaling".
     #- Напишите функцию move(vehicle), которая принимает объект и вызывает у него метод move().

    #Пример использования:

      #car = Car()
      #bike = Bicycle()

      #print(move(car))  # Вывод: Car is driving
      #print(move(bike))  # Вывод: Bicycle is pedaling

class Vehicle:
    def __init__(self, name):
        self.name = name
    def move(self):
        return "Vehicle is moving"

class Car(Vehicle):
    def move(self):
        return "Car is driving"

class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is pedaling"

def move(vehicle):
    return vehicle.move()

car = Car("Car")
bike = Bicycle("Bicycle")

print(car.move())
print(bike.move())

#.    4. Абстракция
    #Задание:
    #Создайте абстрактный класс Shape с методом area() и конкретные классы-наследники для вычисления площади разных фигур.

    #Требования:

     #- Абстрактный класс Shape должен иметь метод area(), который не реализован (используйте модуль abc).
     #- Реализуйте два наследника Rectangle, принимающий ширину и высоту. Circle, принимающий радиус.
     #- Метод area() унаследованных классов должен вычислять площадь.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
  
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2

rect = Rectangle(10, 5)
circle = Circle(7)

print(rect.area())  # Вывод: 50
print(circle.area())  # Вывод: ~153.94