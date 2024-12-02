"""Методы для проверки ответов наших запросов"""
import json

from requests import Response


class Posts_user():
    """Метод для проверки статус кода"""
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print('Успешно', response.status_code)
        else:
            print('Провал', response.status_code)

    """Метод для проверки наличия обязательны полей в ответе запроса"""
    @staticmethod
    def check_json_token(result, expected_value):
        token = json.loads(result.text)
        assert list(token) == expected_value
        print('Все поля присутствуют')

    """Метод провеки значений обязательных полей"""
    @staticmethod
    def check_json_value(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(field_name, 'верен')


