from src.parser import HH
from src.utils import create_class, sorting
from src.compare import CreateFile


def main():
    file_name = input("Введите название файла\n")+".json"
    user_vacancy = input('Введите вакансию для поиска на сайте hh.ru: \n')
    hh = HH(user_vacancy)
    if hh.status_code() != 200:
        print(f"Ошибка {hh.status_code()}")
        quit()
    hh.load_vacancies()
    vacancies = hh.vacancies
    fv = CreateFile()
    fv.save_file(vacancies, file_name)
    name_criterion = input('Введите критерий для отбора вакансий: \n')
    fv.get_data(name_criterion, file_name)
    processed_vacancies = create_class(file_name)
    n = input('Введите количество вакансий для просмотра: \n')
    top_vacancies = sorting(processed_vacancies, int(n))
    for vac in top_vacancies:
        print(vac)
    delete = input("Удалить список вакансий?(Y/N)").upper()
    if delete == "Y":
        fv.del_file(file_name)


if __name__ == '__main__':
    main()