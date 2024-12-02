from utils.http_methods import Http_methods



base_url = 'http://127.0.0.1:8000/'
class DeletedComments:
    @staticmethod
    def delete_comments(authorization, id):
        path_delete = f'api/comments/{id}/'
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {authorization}"

        }

        delete_url = base_url + path_delete
        res_delete = Http_methods.delete(delete_url, header=headers)
        print(res_delete.text)
        return res_delete