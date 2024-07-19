import json
from abc import ABC, abstractmethod


class BaseHH(ABC):
    """Класс-конструктор для работы с API HH"""
    @abstractmethod
    def __init__(self):
        pass

class Parser(BaseHH):

    def __init__(self, file_worker) -> None:
        self.file_worker = file_worker

    def save_in_file(self, vacancies) -> None:
        """
        Метод класса Parser(BaseHH) записывающий в файл *.json всю информацию по вакансиям
        :param vacancies: список вакансий полученных с сайта hh.ru по запросу
        """
        with open(self.file_worker, "w", encoding="utf-8") as file:
            json.dump(vacancies, file, indent=4)
