from utils.http_methods import Http_methods

base_url = 'http://127.0.0.1:8000/'

class Ragister:
    @staticmethod
    def register_user():
        path_post = 'auth/users/'
        json_p = {
                "email": "user@e6xample.com",
                "username": "L0kd1RXVvtEsqGD@4lAv",
                "password": "strin121g",
                "re_password": "strin121g"
            }
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json"
        }
        post_url = base_url + path_post
        res_post = Http_methods.post(post_url, header=headers, body=json_p)
        check_post = res_post.json()
        return res_post