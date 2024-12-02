from utils.http_methods import Http_methods

base_url = 'http://127.0.0.1:8000/'
class LstPost:
    @staticmethod
    def lst_posts_user(authorization):
        path_get = 'api/posts/'
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": authorization
        }
        get_url = base_url + path_get
        res_get = Http_methods.get(get_url, headers=headers)
        print(res_get.text)
        return res_get
