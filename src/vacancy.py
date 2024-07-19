class WorkVacancy:
    """
    Класс WorkVacancy формирующий новую структуру для JSON файла
    вакансий с сайта hh.ru
    """
    def __init__(self, name_vacancy: str, url_vacancy: str, city: str, salary_from: int | None,
                 salary_to: int | None, salary_currency: str | None,
                 snippet_requirement: str) -> None:
        self.name_vacancy = name_vacancy
        self.url_vacancy = url_vacancy
        self.city = city

