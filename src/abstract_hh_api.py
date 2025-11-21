from abc import ABC, abstractmethod
from typing import Any, List


class AbstractHHApi(ABC):
    """Абстрактный класс для работы с API"""

    @abstractmethod
    def get_vacancies(self, keyword: str) -> List[Any] | None:
        pass
