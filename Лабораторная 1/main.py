import doctest
from typing import Union


def validate_type(name: str, value, excepted_type: type):
    if not isinstance(value, excepted_type):
        raise TypeError(f"{name} должен быть типа {excepted_type}")


def validate_positive(name: str, value: Union[int, float]):
    if value < 0:
        raise ValueError(f"{name} не может иметь отрицательное значение.")


class Car:

    def __init__(self, fuel_capacity: float, fuel: float, price: float):
        """
            Создание и подготовка к работе объекта "Машина"
            :param fuel_capacity: Вместимость толливного бака
            :param fuel: Текущий объем топлива
            :param price: Цена машины
            Примеры:
            >>> car = Car(500, 250, 457)
        """
        self.validate_attributes(fuel_capacity, fuel, price)

        self.fuel_capacity = fuel_capacity
        self.fuel = fuel
        self.price = price

    def validate_attributes(self, fuel_capacity: Union[int, float], fuel: Union[int, float], price: Union[int, float]):
        validate_type('fuel_capacity', fuel_capacity, Union[int, float])
        validate_positive('fuel_capacity', fuel_capacity)

        validate_type('fuel', fuel, Union[int, float])
        validate_positive('fuel', fuel)

        validate_type('price', price, Union[int, float])
        validate_positive('price', price)

    def is_affordable(self, money: Union[int, float]) -> bool:
        """
        Функция, которая проверяет хватит ли у вас денег на покупку машины.
        :param money: Количество имеющихся денег.
        :return: Хватит ли денег на машину?
        Примеры:
        >>> car = Car(500, 250, 457)
        >>> car.is_affordable(500)
        """
        validate_type('money', money, Union[int, float])
        ...

    def add_fuel(self, amount: Union[int, float]):
        """
        Функция, которая добавляет топливо в бак.
        :param amount: Количество добавляемого топлива.
        :raise ValueError: Если количество добавляемого топлива превышает свободное место в баке.
        Примеры:
        >>> car = Car(500, 250, 457)
        >>> car.add_fuel(100)
        """
        validate_type('amount', amount, Union[int, float])
        validate_positive('amount', amount)
        ...

    def spend_fuel(self, amount: Union[int, float]):
        """
        Функция, которая тратит топливо.
        :param amount: Количество потреченного топлива.
        :raise ValueError: Если количество потраченного топлива превышает количество оставшегося топлива.
        Примеры:
        >>> car = Car(500, 250, 457)
        >>> car.spend_fuel(100)
        """
        validate_type('amount', amount, Union[int, float])
        validate_positive('amount', amount)
        ...


class Box:

    def __init__(self, width: Union[int, float], height: Union[int, float], length: Union[int, float]):
        """
            Создание и подготовка к работе объекта "Коробка"
            :param width: Ширина
            :param height: Высота
            :param length: Длина
            Примеры:
            >>> box = Box(142, 457, 142)
        """
        self.validate_attributes(width, height, length)

        self.width = width
        self.height = height
        self.length = length

    def validate_attributes(self, width: Union[int, float], height: Union[int, float], length: Union[int, float]):
        validate_type('width', width, Union[int, float])
        validate_positive('width', width)

        validate_type('height', height, Union[int, float])
        validate_positive('height', height)

        validate_type('length', length, Union[int, float])
        validate_positive('length', length)

    def get_volume(self) -> float:
        """
            Функция, возвращающая объем коробки.
            :return: Объем коробки
            Примеры:
            >>> box = Box(142, 457, 142)
            >>> box.get_volume()
        """
        ...

    def is_cube(self) -> bool:
        """
            Функция, которая проверяет является ли коробка кубом(все стороны равны).
            :return: Является ли коробка кубом?
            Примеры:
            >>> box = Box(142, 457, 142)
            >>> box.is_cube()
        """
        ...

    def add(self, box: 'Box') -> 'Box':
        """
            Функция, складывающая длины сторон коробок.
            :return: Новая коробка со сложенными сторонами.
            Примеры:
            >>> box1 = Box(142, 457, 142)
            >>> box2 = Box(42, 75, 147)
            >>> box3 = box1.add(box2)
        """
        validate_type('box', box, Box)
        ...

    def subtract(self, box: 'Box') -> 'Box':
        """
            Функция, вычитающая стороны коробок.
            :raise ValueError: Если вычитание даст коробку с отрицательными сторонами.
            :return: Новая коробка с вычтенными сторонами.
            Примеры:
            >>> box1 = Box(142, 457, 142)
            >>> box2 = Box(42, 75, 147)
            >>> box3 = box1.subtract(box2)
        """
        validate_type('box', box, Box)
        ...


class Cat:

    def __init__(self, breed: str, age: int):
        """
            Создание и подготовка к работе объекта "Кот"
            :param breed: Порода
            :param age: Возраст
            Примеры:
            >>> cat = Cat("Сиамская", 4)
        """
        self.validate_attributes(breed, age)

        self.breed = breed
        self.age = age

    def validate_attributes(self, breed: str, age: int):
        validate_type('breed', breed, str)

        validate_type('age', age, int)
        validate_positive('age', age)

    def say_meow(self) -> None:
        """
            Функция, печатающая 'meow' в консоль
            Примеры:
            >>> cat = Cat("Сиамская", 4)
            >>> cat.say_meow()
        """
        ...

    def get_cat_age(self) -> int:
        """
            Функция, возвращающая возраст кошки в кошачьих годах.
            Примеры:
            >>> cat = Cat("Сиамская", 4)
            >>> cat.get_cat_age()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
