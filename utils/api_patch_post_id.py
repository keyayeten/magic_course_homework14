from utils.http_methods import Http_methods



base_url = 'http://127.0.0.1:8000/'
class PatchLstPostId:
    @staticmethod
    def lst_patch_user_id(authorization, id):
        path_patch = f'api/posts/{id}/'
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {authorization}"

        }
        body_json = {
                "title": "Happy December",
                "content": "31"
            }

        patch_url = base_url + path_patch
        res_patch_id = Http_methods.patch(patch_url, header=headers, body=body_json)
        print(res_patch_id.text)
        return res_patch_id