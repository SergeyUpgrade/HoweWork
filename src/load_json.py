import json
from abc import ABC, abstractmethod
from typing import List, Dict


class ParserABC(ABC):
    @abstractmethod
    def save_in_file(self):
        pass

class Parser(ParserABC):

    def __init__(self, file_worker: str) -> None:
        self.file_worker = file_worker

    def save_in_file(self, vacancies: List[Dict]) -> None:
        """
       Метод класса Parser(BaseAPI) записывающий в файл *.json всю информацию по вакансиям
        :param vacancies: список вакансий полученных с сайта hh.ru по запросу
        """
        with open(self.file_worker, "w", encoding="utf-8") as file:
            json.dump(vacancies, file, indent=4)
