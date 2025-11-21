import pytest

from src.json_saver import JSONSaver


@pytest.fixture
def test_data1():
    return [
        {
            "name": "Python-разработчик",
            "alternate_url": "https://hh.ru/vacancy/1",
            "salary": {"from": 100000, "to": 150000},
            "snippet": {"requirement": "Знание основ Python", "responsibility": "Разработка"},
            "employer": {"name": "Company BigData"},
        },
        {
            "name": "Программист",
            "alternate_url": "https://hh.ru/vacancy/2",
            "salary": None,
            "snippet": {"requirement": "ML experience", "responsibility": "Анализ данных"},
            "employer": {"name": "Company B"},
        },
    ]


@pytest.fixture
def test_data2():
    return [
        {
            "name": "Программист",
            "alternate_url": "https://hh.ru/vacancy/1",
            "salary": {"from": 100000},
            "snippet": {},  # Пустой snippet
            "employer": {"name": "Company BigData"},
        }
    ]


@pytest.fixture
def saver(tmpdir):
    file = tmpdir.join("test.json")
    return JSONSaver(str(file))
