from src.vacancy import Vacancy


def test_init_with_salary():
    """Тест инициализации с указанной зарплатой"""
    vacancy = Vacancy(
        name="Python-разработчик",
        url="https://hh.ru/vacancy/123",
        salary={"from": 100000, "to": 150000},
        description="Разработка на Python",
        employer="Tech Company",
    )

    assert vacancy.name == "Python-разработчик"
    assert vacancy.url == "https://hh.ru/vacancy/123"
    assert vacancy.salary_from == 100000
    assert vacancy.salary_to == 150000
    assert vacancy.description == "Разработка на Python"
    assert vacancy.employer == "Tech Company"


def test_init_without_salary():
    """Тест инициализации без зарплаты"""
    vacancy = Vacancy(
        name="Intern", url="https://hh.ru/vacancy/124", salary=None, description="Стажировка", employer="Startup"
    )

    assert vacancy.name == "Intern"
    assert vacancy.salary_from == 0
    assert vacancy.salary_to == 0


def test_init_with_partial_salary():
    """Тест инициализации с частичной зарплатой"""
    vacancy = Vacancy(
        name="Developer",
        url="https://hh.ru/vacancy/125",
        salary={"from": 120000},  # только "from"
        description="Разработка",
        employer="Company",
    )

    assert vacancy.salary_from == 120000
    assert vacancy.salary_to == 0


def test_validate_salary_positive():
    """Тест валидации корректной зарплаты"""
    assert Vacancy._Vacancy__validate_salary(100000) == 100000
    assert Vacancy._Vacancy__validate_salary(50000.0) == 50000.0


def test_validate_salary_invalid():
    """Тест валидации некорректной зарплаты"""
    assert Vacancy._Vacancy__validate_salary(None) == 0
    assert Vacancy._Vacancy__validate_salary(0) == 0
    assert Vacancy._Vacancy__validate_salary(-1000) == 0
    assert Vacancy._Vacancy__validate_salary("100000") == 0
    assert Vacancy._Vacancy__validate_salary([]) == 0


def test_lt_comparison():
    """Тест сравнения 'меньше'"""
    v1 = Vacancy("ITech", "url1", {"from": 70000}, "description", "employer")
    v2 = Vacancy("Company XX", "url2", {"from": 100000}, "description", "employer")

    assert v1 < v2
    assert not v2 < v1


def test_le_comparison():
    """Тест сравнения 'меньше или равно'"""
    v1 = Vacancy("ITech", "url1", {"from": 70000}, "description", "employer")
    v2 = Vacancy("Company XX", "url2", {"from": 100000}, "description", "employer")
    v3 = Vacancy("I-Comp", "url3", {"from": 70000}, "description", "employer")

    assert v1 <= v2
    assert v1 <= v3
    assert not v2 <= v1


def test_eq_comparison():
    """Тест сравнения 'равенства'"""
    v1 = Vacancy("A", "url1", {"from": 100000}, "desc", "emp")
    v2 = Vacancy("B", "url2", {"from": 100000}, "desc", "emp")
    v3 = Vacancy("C", "url3", {"from": 50000}, "desc", "emp")

    assert v1 == v2
    assert not v1 == v3


def test_str_with_salary_range():
    """Тест строкового представления с диапазоном зарплат"""
    vacancy = Vacancy(
        name="Developer",
        url="https://hh.ru/vacancy/123",
        salary={"from": 100000, "to": 150000},
        description="Разработка приложений",
        employer="Tech Corp",
    )

    result = str(vacancy)
    assert "Developer" in result
    assert "Tech Corp" in result
    assert "100000-150000" in result
    assert "https://hh.ru/vacancy/123" in result
    assert "Разработка приложений" in result


def test_cast_to_object_list_valid_data(test_data1):
    """Тест конвертации валидных данных в список объектов"""

    vacancies = Vacancy.cast_to_object_list(test_data1)

    assert len(vacancies) == 2
    assert vacancies[0].name == "Python-разработчик"
    assert vacancies[0].salary_from == 100000
    assert vacancies[0].salary_to == 150000
    assert vacancies[0].description == "Знание основ PythonРазработка"
    assert vacancies[0].employer == "Company BigData"

    assert vacancies[1].name == "Программист"
    assert vacancies[1].salary_from == 0
    assert vacancies[1].salary_to == 0


def test_cast_to_object_list_missing_fields(test_data2):
    """Тест конвертации данных с отсутствующими полями"""

    vacancies = Vacancy.cast_to_object_list(test_data2)

    assert vacancies[0].description == ""  # Оба поля snippet пустые
    assert vacancies[0].employer == "Company BigData"
