from utils.http_methods import Http_methods



base_url = 'http://127.0.0.1:8000/'
class PutLstPostId:
    @staticmethod
    def lst_put_user_id(authorization, id):
        path_put = f'api/posts/{id}/'
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {authorization}"

        }
        body_json = {
                "title": "December",
                "content": "31"
            }

        put_url = base_url + path_put
        res_put_id = Http_methods.put(put_url, header=headers, body=body_json)
        print(res_put_id.text)
        return res_put_id