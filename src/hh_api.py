import json
from pprint import pprint
from typing import Any, List

import requests

from src.abstract_hh_api import AbstractHHApi


class HeadHunterAPI(AbstractHHApi):
    """Класс для работы с API HeadHunter"""

    def __init__(self) -> None:
        self.__base_url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.vacancies = []

    def __connection_setup(self) -> None:
        """Отправляет запрос на базовый URL. Приватный метод, доступен только внутри класса"""

        response = requests.get(self.__base_url, headers=self.__headers)
        status_code = response.status_code
        if status_code == 200:
            print(status_code)
        else:
            print(f"Запрос не был успешным. Возможная причина {response.reason}")

    def public_connection_setup(self) -> None:
        """Это публичный метод, который вызывает приватный метод"""

        self.__connection_setup()

    def get_vacancies(self, keyword: str) -> List[Any] | None:
        """Получает список вакансий с сервера"""

        self.public_connection_setup()
        params = {"text": keyword, "area": 66, "page": 0, "per_page": 100, "only_with_salary": True}
        while params["page"] != 20:
            try:
                response = requests.get(self.__base_url, headers=self.__headers, params=params)
                response.raise_for_status()
                vacancies = response.json()["items"]
                self.vacancies.extend(vacancies)
                params["page"] += 1
                return self.vacancies
            except requests.exceptions.RequestException as e:
                print(f"Ошибка при выполнении запроса: {e}")
                return []
            except json.JSONDecodeError:
                print("Ошибка при парсинге JSON-ответа.")
                return []