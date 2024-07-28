from abc import ABC, abstractmethod
import json


class LoadVacancy(ABC):
    @abstractmethod
    def read_file(self, file_name):
        pass

    @abstractmethod
    def save_file(self, data, file_name):
        pass

    @abstractmethod
    def del_file(self, file_name):
        pass


class CreateFile(LoadVacancy):
    def read_file(self, file_name):
        with open(f"data/{file_name}", "r", encoding="utf8") as file:
            return json.load(file)

    def save_file(self, data, file_name):
        with open(f"data/{file_name}", "w", encoding="utf8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def get_data(self, criterion, file_name):
        """Метод получения данных из файла по указанным критериям"""
        criterion_vac = []
        with open(f"data/{file_name}", "r", encoding="utf8") as file:
            vacancies = json.load(file)
            for vac in vacancies:
                if not vac["snippet"]["requirement"]:
                    continue
                else:
                    if criterion in vac["snippet"]["requirement"]:
                        criterion_vac.append(vac)
        return criterion_vac

    def del_file(self, file_name):
        with open(f"data/{file_name}", "w") as file:
            pass