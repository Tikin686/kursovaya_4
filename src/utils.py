from src.vacancy import Vacancy
from src.compare import CreateFile


def sorting(vacancies, n: int):
    sorted_vacancies = sorted(vacancies, reverse=True)
    return sorted_vacancies[:n]


def create_class(file_name):
    """Приводит полученные данные к данным для вывода"""
    list_vacancies = []
    vacancies = CreateFile()
    for vac in vacancies.read_file(file_name):
        if not vac["salary"]:
            vac["salary"] = {"from": 0, "to": 0, "currency": ""}
        vacancy = Vacancy(vac['name'], vac['salary'], vac['url'], vac["snippet"]['requirement'])
        list_vacancies.append(vacancy)
    return list_vacancies
