# Класс "Круг"
# Напишите класс Circle, который имеет свойство radius (радиус) и методы для вычисления площади и периметра круга.

# class Circle:
#
#     def __init__(self, radius):
#         self.radius = radius
#
#     def get_square(self):
#         return 3.14 * self.radius ** 2
#
#     def get_perimeter(self):
#         return 2 * 3.14 * self.radius
#
#     def set_radius(self, new_radius):
#         self.radius = new_radius
#
# circle = Circle(10)
# print(circle.get_square())
# print(circle.get_perimeter())
# circle.set_radius(20)
# print(circle.get_square())
# print(circle.get_perimeter())

# Создайте класс Student с атрибутами name (имя) и grades (список оценок).
# Добавьте метод для добавления новой оценки, а также для вычисления среднего балла.

# class Student:
#
#     def __init__(self, name):
#         # Инициализация имени студента и пустого списка оценок
#         self.name = name
#         self.grades = []
#
#     def add_grade(self, grade):
#         # Метод для добавления новой оценки
#         self.grades.append(grade)
#
#     def get_average_grade(self):
#         # Метод для вычисления среднего балла
#         return sum(self.grades) / len(self.grades)
#
# student = Student('John')
# student.add_grade(5)
# student.add_grade(3)
# student.add_grade(3)
# print(f"Средний балл студента: {student.get_average_grade()}")

# Создайте класс Triangle, который будет содержать атрибуты для длины сторон a, b, c.
# Реализуйте методы для вычисления периметра и площади треугольника.

# class Triangle:
#
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_perimeter(self):
#         return self.a + self.b + self.c
#
#     def get_square(self):
#         p = self.get_perimeter() / 2
#         return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
#
# triangle = Triangle(1, 2, 3)
# print(triangle.get_perimeter())
# print(triangle.get_square())

# Создайте класс Book с атрибутами title (название), author (автор), year (год издания).
# Добавьте метод для отображения полной информации о книге.

# class Book:
#
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
#
#     def display_full_information(self):
#         return f"Название: {self.title}, Автор: {self.author}, Год издания: {self.year}"
#
# book = Book("Знайка в земле", "Вася Пупкин", 1900)
# print(book.display_full_information())

# Создайте класс Product с атрибутами name (название товара) и price (цена).
# Создайте класс Cart для хранения списка продуктов и метод для вычисления общей стоимости.

class Product:
    def __init__(self, name, price):
        # Инициализация продукта (название и цена)
        self.name = name
        self.price = price


class Cart:
    def __init__(self):
        # Инициализация пустой корзины
        self.cart = []

    def add_product(self, product):
        # Метод для добавления продукта в корзину
        self.cart.append(product)

    def total_price(self):
        # Метод для вычисления общей стоимости товаров в корзине
        pass
