from typing import List

BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        # не использовал pydantic, потому что при наложении ограничения conint(gt=0) на id_ и pages
        # __repr__ вместо их реального значения выводил <class '__main__.ConstrainedIntValue'>
        self.validate_attributes(id_, name, pages)

        self.id_ = id_
        self.name = name
        self.pages = pages

    def validate_attributes(self, id_: int, name: str, pages: int):
        if not isinstance(id_, int):
            raise TypeError("Идентификатор должен быть типа int")
        if not id_ > 0:
            raise ValueError("Идентификатор должен быть больше 0")

        if not isinstance(name, str):
            raise TypeError("Название должно быть типа str")
        if len(name) <= 0:
            raise ValueError("Название должно содержать хотя бы один символ")

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if not pages > 0:
            raise ValueError("Количество страниц должно быть больше 0")

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'Book(id_={self.id_}, name={self.name!r}, pages={self.pages})'


class Library:
    def __init__(self, books: List[Book] = []):
        if not isinstance(books, list):
            raise TypeError("Список книг должен быть типа list")
        self.books = books

    def get_next_book_id(self) -> int:
        if len(self.books) <= 0:
            return 1
        return self.books[-1].id_ + 1

    def get_index_by_book_id(self, id_: int) -> int:
        for i, book in enumerate(self.books):
            if book.id_ == id_:
                return i
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
