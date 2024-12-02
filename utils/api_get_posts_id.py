from utils.http_methods import Http_methods



base_url = 'http://127.0.0.1:8000/'
class GetLstPostId:
    @staticmethod
    def lst_posts_user_id(authorization, id):
        path_get = f'api/posts/{id}/'
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {authorization}"

        }

        get_url = base_url + path_get
        res_get_id = Http_methods.get(get_url, headers=headers)
        print(res_get_id.text)
        return res_get_id