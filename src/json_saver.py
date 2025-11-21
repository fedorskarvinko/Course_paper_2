import json
import os
from typing import Any, Dict, List, Optional

from src.abstract_json_saver import AdstractJSONSaver


class JSONSaver(AdstractJSONSaver):
    """Класс для работы с json-файлом вакансий"""

    def __init__(self, file_name: str = "data/vacancies.json") -> None:
        self.__file_name = file_name

    def __load(self) -> List[Dict]:
        """Загружает данные из json-файла"""
        if os.path.exists(self.__file_name):
            with open(self.__file_name, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, dict) and "items" in data:
                    return data["items"]
                return data
        return []

    def __save(self, data: List[Dict]) -> None:
        """Сохраняет данные в json-файл"""

        directory = os.path.dirname(self.__file_name)
        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

        with open(self.__file_name, "w", encoding="utf-8") as f:
            json.dump({"items": data}, f, ensure_ascii=False, indent=4)

    def add_vacancy(self, vacancy: Dict) -> None:
        """Добавляет вакансию в файл"""
        data = self.__load()
        if not any(v["id"] == vacancy["id"] for v in data):
            data.append(vacancy)
        self.__save(data)

    def get_vacancies(self, criteria: Optional[Dict[str, Any]] = None) -> List[Dict]:
        """Возвращает вакансии, соответствующие критериям поиска"""
        data = self.__load()
        if criteria:
            return [v for v in data if all(v.get(k) == criteria[k] for k in criteria)]
        return data

    def delete_vacancy(self, vacancy: Dict) -> None:
        """Удаляет вакансию из файла"""
        data = self.__load()
        data = [v for v in data if v["id"]]
        self.__save(data)
