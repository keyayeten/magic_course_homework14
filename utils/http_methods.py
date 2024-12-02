import requests
from utils.logger import Logger

"""Список Http методов"""

class Http_methods:

    @staticmethod
    def get(url, headers):
        Logger.add_request(url, method="GET")
        result = requests.get(url, headers=headers)
        Logger.add_response(result)
        return result

    @staticmethod
    def post(url, body, header):
        Logger.add_request(url, method="POST")
        result = requests.post(url, json=body, headers=header)
        Logger.add_response(result)
        return result

    @staticmethod
    def put(url, body, header):
        Logger.add_request(url, method="PUT")
        result = requests.put(url, json=body, headers=header)
        Logger.add_response(result)
        return result

    @staticmethod
    def patch(url, body, header):
        Logger.add_request(url, method="PATCH")
        result = requests.patch(url, json=body, headers=header)
        Logger.add_response(result)
        return result

    @staticmethod
    def delete(url, header):
        Logger.add_request(url, method="DELETE")
        result = requests.delete(url, headers=header)
        Logger.add_response(result)
        return result