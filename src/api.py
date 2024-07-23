from abc import ABC, abstractmethod
from src.load_json import Parser

import requests


class BaseAPI(ABC):
    """Класс-конструктор для работы с API HH"""

    @abstractmethod
    def load_vacancies(self):
        pass

class HH(BaseAPI):
    """Класс для работы с API HeadHunter"""

    def __init__(self) -> None:
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []

    def load_vacancies(self, keyword: str) -> None:
        """
        Метод класса HH(Parser), который запрашивает информацию по вакаснсиям на сайте hh.ru
        :param keyword: наименовании запрашиваемой вакансии
        """
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params, timeout=10)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1
        parser = Parser("./data/vacancies.json")
        parser.save_in_file(self.vacancies)