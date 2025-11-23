from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional


class AbstractJSONSaver(ABC):
    """Абстрактный класс для работы с файлами"""

    @abstractmethod
    def add_vacancy(self, vacancy: Dict) -> None:
        pass

    @abstractmethod
    def get_vacancies(self, criteria: Optional[Dict[str, Any]] = None) -> List[Dict]:
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Dict) -> None:
        pass