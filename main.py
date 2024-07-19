from src.api import HH
from src.user_interface import interface
from src.connector import Connector


def main():
    user_input = input("Введите название вакансии: ")
    user_request = HH("../HoweWork_4/data/vacancies.json")

    print("Ожидаем получения данных по вакансиям")

    user_request.load_vacancies(user_input)

    Connector().add_vacancy()
    interface()


if __name__ == "__main__":
    main()