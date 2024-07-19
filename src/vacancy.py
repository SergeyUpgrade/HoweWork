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

        if self._validate_salary(salary_from) is None:
            if salary_from is None:
                self.salary_from = 0
            else:
                self.salary_from = salary_from

        if self._validate_salary(salary_to) is None:
            if salary_to is None:
                self.salary_to = 0
            else:
                self.salary_to = salary_to

        self.salary_currency = salary_currency
        self.snippet_requirement = snippet_requirement

    @staticmethod
    def _validate_salary(salary):
        """
        Метод класса осуществляющий валидацию заработной платы вакансий
        :param salary: зарплата передававемая при инициализации, либо salary_to, либо salary_from
        """
        if salary is not None and salary < 0:
            raise ValueError("Salary cannot be negative")
