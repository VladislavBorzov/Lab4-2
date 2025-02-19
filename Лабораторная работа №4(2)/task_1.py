class Animal:
    """
    Базовый класс для животных.

    Атрибуты:
        name (str): Имя животного.
        age (int): Возраст животного.
        species (str): Вид животного.

    Методы:
        __init__(self, name: str, age: int, species: str)
            Конструктор класса Animal.
        __str__(self) -> str
            Возвращает строку с описанием животного.
        __repr__(self) -> str
            Возвращает строку с описанием животного.
        make_sound(self) -> str
            Базовый метод для воспроизведения звука животного.
    """

    def __init__(self, name: str, age: int, species: str):
        """
        Конструктор класса Animal.

        :param name: Имя животного.
        :param age: Возраст животного.
        :param species: Вид животного.
        """
        self._name = name
        self._age = age
        self._species = species

    def __str__(self) -> str:
        """Возвращает строку с описанием животного."""
        return f"{self._name}, возраст {self._age} лет, вид {self._species}"

    def __repr__(self) -> str:
        """Возвращает строку с описанием животного."""
        return f"Animal(name={self._name!r}, age={self._age!r}, species={self._species!r})"

    def make_sound(self) -> str:
        """Базовый метод для воспроизведения звука животного."""
        return "Животное издает звук."


class SportGame:
    """
    Базовый класс для спортивных игр.

    Атрибуты:
        name (str): Название игры.
        num_players (int): Количество игроков.
        equipment (list[str]): Необходимое оборудование.

    Методы:
        __init__(self, name: str, num_players: int, equipment: list[str])
            Конструктор класса SportGame.
        __str__(self) -> str
            Возвращает строку с описанием игры.
        __repr__(self) -> str
            Возвращает строку с описанием игры.
        start_game(self) -> str
            Базовый метод для начала игры.
    """

    def __init__(self, name: str, num_players: int, equipment: list[str]):
        """
        Конструктор класса SportGame.

        :param name: Название игры.
        :param num_players: Количество игроков.
        :param equipment: Необходимое оборудование.
        """
        self._name = name
        self._num_players = num_players
        self._equipment = equipment

    def __str__(self) -> str:
        """Возвращает строку с описанием игры."""
        return f"{self._name}: игра для {self._num_players} игроков, требуется оборудование: {', '.join(self._equipment)}"

    def __repr__(self) -> str:
        """Возвращает строку с описанием игры."""
        return f"SportGame(name={self._name!r}, num_players={self._num_players!r}, equipment={self._equipment!r})"

    def start_game(self) -> str:
        """Базовый метод для начала игры."""
        return f"Игра {self._name} началась!"


# Дочерние классы

class Dog(Animal):
    """
    Класс для собак, который наследует от класса Animal.

    Атрибуты:
        breed (str): Порода собаки.

    Методы:
        __init__(self, name: str, age: int, breed: str)
            Расширяет конструктор базового класса.
        __str__(self) -> str
            Переопределяет метод для описания собаки.
        __repr__(self) -> str
            Переопределяет метод для описания собаки.
        bark(self) -> str
            Перегружает метод make_sound для лая собаки.
    """

    def __init__(self, name: str, age: int, breed: str):
        """
        Расширяет конструктор базового класса.

        :param name: Имя собаки.
        :param age: Возраст собаки.
        :param breed: Порода собаки.
        """
        # Вызываем конструктор базового класса
        super().__init__(name, age, "собака")
        self._breed = breed

    def __str__(self) -> str:
        """Переопределяет метод для описания собаки."""
        return f"{super().__str__()}, порода {self._breed}"

    def __repr__(self) -> str:
        """Переопределяет метод для описания собаки."""
        return f"Dog(name={self._name!r}, age={self._age!r}, breed={self._breed!r})"

    def bark(self) -> str:
        """
        Перегружает метод make_sound для лая собаки.

        Причина перегрузки: Собаки издают характерный лай, который отличается от общего звукового поведения животных.
        """
        return f"{self._name} громко лает!"


class Football(SportGame):
    """
    Класс для футбола, который наследует от класса SportGame.

    Атрибуты:
        field_size (tuple[int, int]): Размеры футбольного поля.

    Методы:
        __init__(self, num_players: int, field_size: tuple[int, int])
            Расширяет конструктор базового класса.
        __str__(self) -> str
            Переопределяет метод для описания футбола.
        __repr__(self) -> str
            Переопределяет метод для описания футбола.
        kick_ball(self) -> str
            Перегружает метод start_game для удара по мячу.
    """

    def __init__(self, num_players: int, field_size: tuple[int, int]):
        """
        Расширяет конструктор базового класса.

        :param num_players: Количество игроков.
        :param field_size: Размеры футбольного поля.
        """
        # Вызываем конструктор базового класса
        super().__init__("Футбол", num_players, ["мяч", "ворота"])
        self._field_size = field_size

    def __str__(self) -> str:
        """Переопределяет метод для описания футбола."""
        return f"{super().__str__()}, размеры поля {self._field_size[0]}x{self._field_size[1]}"

    def __repr__(self) -> str:
        """Переопределяет метод для описания футбола."""
        return f"Football(num_players={self._num_players!r}, field_size={self._field_size!r})"

    def kick_ball(self) -> str:
        """
        Перегружает метод start_game для удара по мячу.

        Причина перегрузки: Удар по мячу является специфической частью футбольной игры.
        """
        return f"Мяч забит в ворота!"