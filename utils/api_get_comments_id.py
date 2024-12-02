from utils.http_methods import Http_methods



base_url = 'http://127.0.0.1:8000/'
class GetCommentsId:
    @staticmethod
    def get_id_comments(authorization, id):
        path_get = f'api/comments/{id}/'
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {authorization}"

        }

        get_url = base_url + path_get
        res_get = Http_methods.get(get_url, headers=headers)
        print(res_get.text)
        return res_get