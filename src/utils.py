from typing import List

from src.vacancy import Vacancy


def filter_vacancies(vacancies: List[Vacancy], words: List[str]) -> List[Vacancy]:
    """Фильтрация по ключевым словам"""

    return [v for v in vacancies if any(w.lower() in v.description.lower() for w in words)]


def get_by_salary(vacancies: List[Vacancy], range_str: str) -> List[Vacancy]:
    """Фильтрация по зарплате (формат 'min-max')"""
    if not range_str:
        return vacancies
    min_s, max_s = map(int, range_str.split("-"))
    return [v for v in vacancies if v.salary_from >= min_s and (v.salary_to or v.salary_from) <= max_s]


def sort_vacancies(vacancies: List[Vacancy]) -> List[Vacancy]:
    """Сортировка по убыванию зарплаты"""
    return sorted(vacancies, reverse=True)


def get_top(vacancies: List[Vacancy], n: int) -> List[Vacancy]:
    """Получение топ N вакансий"""
    return vacancies[:n]


def print_vacancies(vacancies: List[Vacancy]) -> None:
    """Читаемый вывод"""
    for v in vacancies:
        print(v)
        print("-" * 80)
