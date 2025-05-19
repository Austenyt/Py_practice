"""
Можно гуглить, но нейронки и готовые работы не принимаются.
Тесты иногда посимвольные, поэтому советую точно следовать инструкциям по выводу.
Советую оставлять в __init__ имена локальных атрибутов такими же, как называются параметры,
поскольку на этом завязаны тесты, однако в задании 2 нужно немного пренебречь этим правилом

Задание 1
Написать класс Artifact, который будет описывать фэнтезийные артефакты.
Класс должен содержать информацию о названии, силе артефакта и его стоимости.

Должен соблюдаться правильный вывод при указании экземпляра класса как агрумента print.
print(экземпляр_Artifact) должен вывести (оступы - пробелы, числа абстрактные, конкретный пример ниже):
Название артефакта
    сила: 1000000
    стоимость: 1000000


Все локальные свойства экземпляров должны быть в режиме доступа protected

Создать метод get_cost_efficient, который будет считать эффективность покупки предмета
относительно его цены и стоимости, возвращает число по формуле:
price / power = efficient

Напишите property ко всем свойствам
"""


class Artifact:
    def __init__(self, name, power, price):
        self._name = name
        self._power = power
        self._price = price

    def __repr__(self):
        return f"{self._name}\n    сила: {self._power}\n    стоимость: {self._price}"

    def get_cost_efficient(self):
        return self._price / self._power

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, power):
        self._power = power

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price


# НЕ МЕНЯТЬ
wizard_hat = Artifact('Шляпа колдуна', 100, 250)

"""
Повтряю!
print(wizard_hat) должен вывести (оступы - пробелы):
Шляпа колдуна
    сила: 100
    стоимость: 250
"""
print(wizard_hat)

# ТЕСТЫ задания 1
assert isinstance(wizard_hat, Artifact), 'Задание 1: переменная wizard_hat не является экзепляром класса Artifact'
assert 'price' in wizard_hat.__dir__(), "Задание 1: Цены нет в локальных свойствах"
assert 'name' in wizard_hat.__dir__(), "Задание 1: Названия нет в локальных свойствах"
assert 'power' in wizard_hat.__dir__(), "Задание 1: Силы нет в локальных свойствах"
assert wizard_hat.price == 250, "Задание 1: Цена не совпадает"
assert wizard_hat.name == 'Шляпа колдуна', "Задание 1: Название не совпадает"
assert wizard_hat.power == 100, "Задание 1: Сила не совпадает"
assert str(wizard_hat) == "Шляпа колдуна\n    сила: 100\n    стоимость: 250", "Задание 1: Вывод информации не совпадает"

speed_boots = Artifact('Ботинки скорости', 25, 125)

assert '_price' in speed_boots.__dir__(), "Задание 1 Цены нет в приватных свойствах"
assert '_name' in speed_boots.__dir__(), "Задание 1 Названия нет в локальных свойствах"
assert '_power' in speed_boots.__dir__(), "Задание 1 Силы нет в локальных свойствах"
assert 'get_cost_efficient' in speed_boots.__dir__(), "Задание 1: Не реализован метод get_cost_efficient"
assert speed_boots.get_cost_efficient() == 5, "Задание 1: Не правильный подсчет коэффицента эффективности"

"""
Задание 2
Написать класс Backpack, который будет хранить информацию о вещах в рюкзаке.
При инициализации экземпляра рюкзак ПУСТОЙ, то есть в него ничего изначально не передается.

Нужно реализовать минимум 4 метода: 
   1. add - добавить конкретный предмет (объект) в рюкзак
   2. remove - удалить конкретный предмет (объект) из рюкзака
   Если предмет был в рюкзаке и был удален, то функция должна вернуть True
   Если предмета нет в рюкзаке, то функция должна вернуть False
   3. get_total_price - возврат общей стоимости предметов в рюкзаке
   4. get_total_power - возврат общей силы всех вредметов в рюкзаке

При вызове len(экземпляр_Backpack) должно возвращаться число - кол-во предметов рюкзаке


Должен соблюдаться правильный вывод при указании экземпляра класса как агрумента print.
"""


class Backpack:

    def __init__(self):
        self._backpack = []

    def __repr__(self):
        info = (f"РЮКЗАК{{\nКоличество предметов в рюкзаке: {len(self._backpack)}\nСтоимость предметов:"
                f"{self.get_total_price()}\nМощь предметов: {self.get_total_power()}\nПредметы в рюкзаке:")
        for artifact in self._backpack:
            info += f"    {artifact.name}\n        "
        return info

    def add(self, artifact):
        self._backpack.append(artifact)

    def remove(self, artifact):
        try:
            self._backpack.remove(artifact)
            return True
        except ValueError:
            return False

    def get_total_price(self):
        total_price = 0
        for artifact in self._backpack:
            total_price += artifact.price
        return total_price

    def get_total_power(self):
        total_power = 0
        for artifact in self._backpack:
            total_power += artifact.power
        return total_power


# НЕ МЕНЯТЬ
wizard_hat = Artifact('Шляпа колдуна', 100, 250)
speed_boots = Artifact('Ботинки скорости', 25, 125)
god_sword = Artifact('Божественный меч', 990, 3000)

backpack = Backpack()
backpack.add(wizard_hat)
backpack.add(speed_boots)
backpack.add(god_sword)
print(backpack)

"""
print(backpack) должен вывести (оступы - пробелы):
РЮКЗАК {
Кол-во предметов в рюкзаке: 3
Стоимость предметов: 3375
Мощь предметов: 1115

Предметы в рюкзаке:
    Шляпа колдуна
        сила: 100
        стоимость: 250

    Ботинки скорости
        сила: 25
        стоимость: 125

    Божественный меч
        сила: 990
        стоимость: 3000
}
"""

# ТЕСТЫ задания 2
assert 'get_total_price' in backpack.__dir__(), "Задание 2: Нет метода для подсчета общей цены"
assert 'get_total_power' in backpack.__dir__(), "Задание 2: Нет метода для подсчета общей мощи"
assert backpack.get_total_price() == 3375, "Задание 2: Общая цена не совпала"
assert backpack.get_total_power() == 1115, "Задание 2: Общая мощь не совпала"
assert '__len__' in backpack.__dir__(), "Задание 2: Нет реализации магического метода len"
assert len(backpack) == 3, "Задание 2: Не правильно посчитано кол-во предметов в рюкзаке"
assert str(backpack) == """РЮКЗАК {
Кол-во предметов в рюкзаке: 3
Стоимость предметов: 3375
Мощь предметов: 1115

Предметы в рюкзаке:
    Шляпа колдуна
        сила: 100
        стоимость: 250

    Ботинки скорости
        сила: 25
        стоимость: 125

    Божественный меч
        сила: 990
        стоимость: 3000
}""", "Задание 2: Вывод не совпал"

backpack.remove(wizard_hat)
assert backpack.get_total_price() == 3125, "Задание 2: Общая цена не совпала"
assert backpack.get_total_power() == 1015, "Задание 2: Общая мощь не совпала"
assert len(backpack) == 2, "Задание 2: Не правильно посчитано кол-во предметов в рюкзаке"
print('\n' + '=' * 20 + '\n' + 'ЗАДАНИЕ 2 ВЫПОЛНЕНО\n' + '=' * 20 + '\n')
