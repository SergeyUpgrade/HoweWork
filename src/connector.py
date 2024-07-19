import json
from abc import ABC, abstractmethod

from src.vacancy import WorkVacancy


class BaseConnector(ABC):

    @abstractmethod
    def create_vacancy_list(self) -> list:
        pass

    @abstractmethod
    def add_vacancy(self) -> None:
        pass

    @abstractmethod
    def get_info(self, key_name: str, value_name: str | int) -> list:
        pass

    @abstractmethod
    def delete_vacancy(self) -> None:
        pass

class Connector(BaseConnector):

    def __init__(self) -> None:
        self._vacancy_list = []
        self._finish_list = []

    def create_vacancy_list(self) -> list:
        """
        Метод класса для формирования списка вакансий по новому
        :return: список вакансий после обработки классом WorkVacancy
        """

        with open("../HoweWork_4/data/vacancies.json", "r", encoding="utf-8") as file:
            read_vacancy_file = json.load(file)
            for item in read_vacancy_file:
                if item["salary"] is None or item["area"] is None:
                    continue
                else:
                    self._vacancy_list.append(WorkVacancy(item["name"], item["alternate_url"], item["area"]["name"],
                                                          item["salary"]["from"], item["salary"]["to"],
                                                          item["salary"]["currency"], item["snippet"]["requirement"]))
        return self._vacancy_list

    def add_vacancy(self) -> None:
        vacancy_list = self.create_vacancy_list()
        new_vac = []
        with open("../HoweWork_4/data/vacancies_to_work.json", "w", encoding="utf-8") as file:
            for f in vacancy_list:
                new_vac.append({"name": f.name_vacancy, "url": f.url_vacancy, "area": f.city,
                                "salary_from": f.salary_from, "salary_to": f.salary_to,
                                "currency": f.salary_currency, "snippet": f.snippet_requirement})
            return json.dump(new_vac, file, indent=4)

