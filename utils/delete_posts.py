from utils.http_methods import Http_methods



base_url = 'http://127.0.0.1:8000/'
class DeleteLstPostId:
    @staticmethod
    def lst_delete_user_id(authorization, id):
        path_delete = f'api/posts/{id}/'
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {authorization}"

        }


        delete_url = base_url + path_delete
        res_delete_id = Http_methods.delete(delete_url, header=headers)
        print(res_delete_id.text)
        return res_delete_id
