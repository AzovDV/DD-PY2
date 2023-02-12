from pydantic import BaseModel, conint, confloat, PrivateAttr, validate_arguments


class Pet(BaseModel):
    """Питомец."""

    name: str
    age: conint(ge=0)
    # Прячем голод, чтобы навязать взаимодействие через get_hunger и feed.
    _hunger: confloat(ge=0, le=1) = PrivateAttr(default_factory=lambda: 0.5)

    def get_hunger(self) -> float:
        """Возвращает значение голода."""

        return self._hunger

    @validate_arguments
    def feed(self, value: confloat(ge=0)):
        """Покормить питомца."""

        self._hunger += value
        self._hunger = min(self._hunger, 1)

    def make_noise(self):
        """Вывести звук, который издает питомец. У каждого питомца свой звук, поэтому перегружаем."""

        print("Why are we still here?")

    def __str__(self) -> str:
        return f"{self.name}. {self.age} лет."

    def __repr__(self) -> str:
        return f"Pet(name={self.name!r}, age={self.age})"


class Cat(Pet):
    """Питомец: кот."""

    def make_noise(self):
        """Вывести звук, который издает питомец. У каждого питомца свой звук, поэтому перегружаем."""

        print("Мяу!")


class Dog(Pet):
    """Питомец: собака."""

    def make_noise(self):
        """Вывести звук, который издает питомец. У каждого питомца свой звук, поэтому перегружаем."""

        print("Гав!")


def test_pet(pet: Pet):
    print(pet.__str__())
    print(pet.__repr__())
    pet.make_noise()
    print(f"Before feeding: {pet.get_hunger()}")
    pet.feed(0.3)
    print(f"After feeding: {pet.get_hunger()}")


if __name__ == "__main__":
    test_pet(Pet(name="Владислав", age=12))
    print()
    test_pet(Cat(name="Борис", age=4))
    print()
    test_pet(Dog(name="Шарик", age=10))
