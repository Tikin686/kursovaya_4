import requests
from abc import ABC, abstractmethod

class Parser(ABC):
    @abstractmethod
    def load_vacancies(self):
        pass


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать
    """

    def __init__(self,keyword):
        self.url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': keyword, 'page': 0, 'per_page': 100}
        self.vacancies = []


    def load_vacancies(self, **kwargs):
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.__headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1

    def status_code(self):
        return requests.get(self.url).status_code