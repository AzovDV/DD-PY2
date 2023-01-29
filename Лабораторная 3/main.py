class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super(PaperBook, self).__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, value: int):
        if not isinstance(value, int):
            raise TypeError("pages должно быть типа int.")
        if value < 0:
            raise ValueError("pages не может быть меньше нуля.")
        self._pages = value

    def __str__(self) -> str:
        return f"{super().__str__()} Страницы {self.pages}."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super(AudioBook, self).__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, value: float):
        if not isinstance(value, float):
            raise TypeError("duration должно быть типа float.")
        if value < 0:
            raise ValueError("duration не может быть меньше нуля.")
        self._duration = value

    def __str__(self) -> str:
        return f"{super().__str__()} Длительность {self.duration}."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"


if __name__ == '__main__':
    book1 = Book("Евгений Онегин", "Пушкин")
    book2 = PaperBook("Евгений Онегин", "Пушкин", 15)
    book3 = AudioBook("Евгений Онегин", "Пушкин", 15.4)

    print(book1)
    print(book2)
    print(book3)

    print(book1.__repr__())
    print(book2.__repr__())
    print(book3.__repr__())
