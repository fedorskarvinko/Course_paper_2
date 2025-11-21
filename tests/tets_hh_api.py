from unittest.mock import Mock, patch

import requests

from src.hh_api import HeadHunterAPI


def test_get_vacancies_works():
    """Тестируем работу функции"""
    with patch("src.hh_api.requests.get") as mock_get:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"items": []}
        mock_get.return_value = mock_response

        api = HeadHunterAPI()
        result = api.get_vacancies("test")

        assert result is not None


def test_get_vacancies_on_error():
    """Тестируем возвращение пустого списка при ошибке"""
    with patch("src.hh_api.HeadHunterAPI.public_connection_setup"):  # Отключили проверку подключения
        with patch("src.hh_api.requests.get") as mock_get:
            mock_get.side_effect = requests.exceptions.RequestException("Error")

            api = HeadHunterAPI()
            result = api.get_vacancies("test")

            assert result == []
