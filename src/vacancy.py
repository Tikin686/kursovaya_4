class Vacancy:
    def __init__(self, title:str, salary:dict, url:str, requirements:str):
        if not isinstance(salary, dict):
            raise TypeError("Salary must be a dictionary")
        self.title = title
        self.salary = salary
        self.url = url
        self.requirements = requirements
    def __str__(self):
        return (
            f"Название: {self.title}\n"
            f"Зарплата: от {self.salary['from']} до {self.salary['to']}{self.salary['currency']}\n"
            f"Ссылка: {self.url}\n"
            f"Требования: {self.requirements}"
        )
    def __repr__(self):
        return f"{Vacancy.__class__.__name__}({self.title}, {self.salary}, {self.url}, {self.requirements})"

    def __gt__(self, other):
        return self.salary['to'] > other.salary['to']

    def __lt__(self, other):
        return self.salary['to'] < other.salary['to']