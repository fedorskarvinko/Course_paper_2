from src.hh_api import HeadHunterAPI
from src.json_saver import JSONSavere
from src.utils import fiter_vacancies, get_by_salary, get_top, print_vacancies, sort_vacancies
from src.vacancy import Vacancy


def user_interaction():
    api = HeadHunterAPI()
    saver = JSONSavere()
    query = input("Поисковый запрос: ")
    vacancies_data = api.get_vacancies(query)

    if isinstance(vacancies_data, list) and len(vacancies_data) > 0:

        for vacancy in vacancies_data:
            saver.add_vacancy(vacancy)

        vacancies = Vacancy.cast_to_object_list(vacancies_data)
    else:
        print("Нет данных от API")
        return

    while True:
        n_input = input("Топ N: ").strip()
        if n_input and n_input.isdigit():
            n = int(n_input)
            break
        else:
            print("Пожалуйста, введите число")
    words = input("Ключевые слова(через пробел): ").split()
    range_str = input("Диапозон зарплат(min-max): ")
    filtered = fiter_vacancies(vacancies, words)
    ranged = get_by_salary(filtered, range_str)
    sorted_v = sort_vacancies(ranged)
    top = get_top(sorted_v, n)
    print_vacancies(top)

    if vacancies_data and len(vacancies_data) > 0:
        saver.delete_vacancy(vacancies_data[0])
        print("Удалена первая вакансия.")

    if __name__ == "__main__":
        user_interaction()
