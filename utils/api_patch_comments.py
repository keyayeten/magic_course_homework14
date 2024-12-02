from utils.http_methods import Http_methods



base_url = 'http://127.0.0.1:8000/'
class CreatedPatchComments:
    @staticmethod
    def created_patch_comments(authorization, id):
        path_patch = f'api/comments/{id}/'
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {authorization}"

        }
        json_body = {
                "post": 100,
                "text": "Hello my friends"
        }
        patch_url = base_url + path_patch
        res_patch = Http_methods.patch(patch_url, header=headers, body=json_body)
        print(res_patch.text)
        return res_patch