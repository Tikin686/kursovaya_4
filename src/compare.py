from abc import ABC, abstractmethod
import json


class LoadVacancy(ABC):
    @abstractmethod
    def read_file(self):
        pass

    @abstractmethod
    def save_file(self, data):
        pass

    @abstractmethod
    def del_file(self):
        pass


class CreateFile(LoadVacancy):
    def __init__(self):
        self.__file_name = 'vacancy.json'

    def read_file(self):
        with open(f"data/{self.__file_name}", "r", encoding="utf8") as file:
            return json.load(file)

    def save_file(self, data):
        vacancy = []
        try:
            vacancy.extend(self.read_file())
        except json.decoder.JSONDecodeError as err:
            pass
        vacancy.extend(data)
        with open(f"data/{self.__file_name}", "w", encoding="utf8") as file:
            json.dump(vacancy, file, ensure_ascii=False, indent=4)

    def get_data(self, criterion):
        """Метод получения данных из файла по указанным критериям"""
        criterion_vac = []
        with open(f"data/{self.__file_name}", "r", encoding="utf8") as file:
            vacancies = json.load(file)
            for vac in vacancies:
                if not vac["snippet"]["requirement"]:
                    continue
                else:
                    if criterion in vac["snippet"]["requirement"]:
                        criterion_vac.append(vac)
        return criterion_vac

    def del_file(self):
        with open(f"data/{self.__file_name}", "w") as file:
            pass