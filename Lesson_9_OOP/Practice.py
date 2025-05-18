# Класс "Круг"
# Напишите класс Circle, который имеет свойство radius (радиус) и методы для вычисления площади и периметра круга.

# class Circle:
#
#     def __init__(self, radius):
#         self._radius = radius
#
#     @property
#     def square(self):
#         return 3.14 * self._radius ** 2
#
#     @property
#     def perimeter(self):
#         return 2 * 3.14 * self._radius
#
#     @property
#     def radius(self):
#         return self._radius
#
#     @radius.setter
#     def radius(self, new_radius):
#         self._radius = new_radius
#
#
# circle = Circle(10)
# print(circle.square)
# print(circle.perimeter)
# circle.radius = 20
# print(circle.square)
# print(circle.perimeter)


# Создайте класс Student с атрибутами name (имя) и grades (список оценок).
# Добавьте метод для добавления новой оценки, а также для вычисления среднего балла.

# class Student:
#
#     def __init__(self, name):
#         # Инициализация имени студента и пустого списка оценок
#         self._name = name
#         self.__grades = []
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, name):
#         self._name = name
#
#     def add_grade(self, grade):
#         # Метод для добавления новой оценки
#         self.__grades.append(grade)
#
#     def add_grades(self, grades):
#         # Метод для добавления новой оценки
#         self.__grades.extend(grades)
#
#     @property
#     def average_grade(self):
#         # Метод для вычисления среднего балла
#         return sum(self.__grades) / len(self.__grades)
#
#
# student = Student('John')
# student.add_grade(5)
# student.add_grade(3)
# student.add_grade(3)
# print(f"Средний балл для {student.name}: {student.average_grade}")

# Создайте класс Triangle, который будет содержать атрибуты для длины сторон a, b, c.
# Реализуйте методы для вычисления периметра и площади треугольника.

# class Triangle:
#
#     def __init__(self, a, b, c):
#         self._a = a
#         self._b = b
#         self._c = c
#
#     @property
#     def perimeter(self):
#         return self._a + self._b + self._c
#
#     @property
#     def square(self):
#         p = self.perimeter / 2
#         return (p * (p - self._a) * (p - self._b) * (p - self._c)) ** 0.5
#
#
# triangle = Triangle(2, 2, 3)
# print(triangle.perimeter)
# print(triangle.square)


# Создайте класс Book с атрибутами title (название), author (автор), year (год издания).
# Добавьте метод для отображения полной информации о книге.

# class Book:
#
#     def __init__(self, title, author, year):
#         self._title = title
#         self._author = author
#         self._year = year
#
#     @property
#     def info(self):
#         return f"Название: {self._title}, Автор: {self._author}, Год издания: {self._year}"
#
#
# book = Book("Знайка в земле", "Вася Пупкин", 1900)
# print(book.info)


# Создайте класс Product с атрибутами name (название товара) и price (цена).
# Создайте класс Cart для хранения списка продуктов и метод для вычисления общей стоимости.

class Product:
    def __init__(self, name, price, discount=0):
        # Инициализация продукта (название и цена)
        self._name = name
        self._price = price
        self._discount = discount

    def __repr__(self):
        return f"<{self._name}: {self.price}>"

    def __call__(self, amount):
        return self.price * amount

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def price(self):
        return self._price - self._price * self._discount

    @price.setter
    def price(self, price):
        self._price = price

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount):
        self._discount = discount


class Cart:
    def __init__(self):
        # Инициализация пустой корзины
        self._cart = []

    def __len__(self):
        return len(self._cart)

    def add_product(self, product):
        # Метод для добавления продукта в корзину
        self._cart.append(product)

    @property
    def total_price(self):
        # Метод для вычисления общей стоимости товаров в корзине
        total_price = 0
        for product in self._cart:
            total_price += product.price
        return total_price


cart = Cart()
hleb = Product("Hleb", 10)
milk = Product("Milk", 20)
kolbasa = Product("Kolbasa", 30)
cart.add_product(hleb)
cart.add_product(milk)
cart.add_product(kolbasa)
print(cart.total_price)
print(milk) # обращение к объекту
print(milk(20)) # вызов объекта
print(len(cart))
