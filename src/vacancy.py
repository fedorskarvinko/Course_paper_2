from typing import Optional, Dict, List


class Vacancy:
    """Класс для работы с вакансиями"""

    __slots__ = ("name", "url", "salary_from", "salary_to", "description", "employer")

    def __init__(self, name: str, url: str, salary: Optional[Dict], description: str, employer: str = "") -> None:
        """Инициализация Vacancy"""

        self.name = name
        self.url = url
        self.salary_from = self.__validate_salary(salary.get("from") if salary else None)
        self.salary_to = self.__validate_salary(salary.get("to") if salary else None)
        self.description = description
        self.employer = employer

    @staticmethod
    def __validate_salary(value: Optional[int]) -> int:
        """Приватная валидация зарплаты (0, если не указана)"""

        return value if isinstance(value, (int, float)) and value > 0 else 0

    # Методы сравнения зарплаты

    def __lt__(self, other: "Vacancy") -> bool:
        """Сравнение 'меньше'"""

        return self.salary_from < other.salary_from

    def __le__(self, other: "Vacancy") -> bool:
        """Сравнение 'меньше или равно'"""

        return self.salary_from <= other.salary_from

    def __eq__(self, other: "Vacancy") -> bool:
        """Сравнение 'равенства'"""

        return self.salary_from == other.salary_from

    def __str__(self) -> str:
        """Возвращает строковый объект"""

        salary = f"{self.salary_from}-{self.salary_to}" if self.salary_to else str(self.salary_from)
        salary = salary if salary != "0" else "Не указана"
        return (
            f"{self.name} ({self.employer}) | Зарплата: {salary} | {self.url}\nОписание: {self.description[:100]}..."
        )

    @classmethod
    def cast_to_object_list(cls, data: List[Dict]) -> List["Vacancy"]:
        """Конвертация JSON в список Vacancy"""

        return [
            cls(
                v["name"],
                v["alternate_url"],
                v.get("salary"),
                str(v["snippet"].get("requirement", "") or "") + str(v["snippet"].get("responsibility", "") or ""),
                v["employer"]["name"],
            )
            for v in data
        ]