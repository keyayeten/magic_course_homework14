from utils.http_methods import Http_methods



base_url = 'http://127.0.0.1:8000/'
class CreatedPutComments:
    @staticmethod
    def created_put_comments(authorization, id):
        path_put = f'api/comments/{id}/'
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {authorization}"

        }
        json_body = {
                "post": 100,
                "text": "Hello"
        }
        put_url = base_url + path_put
        res_put = Http_methods.put(put_url, header=headers, body=json_body)
        print(res_put.text)
        return res_put