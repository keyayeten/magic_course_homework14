from utils.http_methods import Http_methods



base_url = 'http://127.0.0.1:8000/'
class CreatedLstPost:
    @staticmethod
    def created_lst_posts_user(authorization):
        path_post = 'api/posts/'
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {authorization}"

        }
        json_body = {
            "title": "Hello",
            "content": "5"
        }
        post_url = base_url + path_post
        res_post = Http_methods.post(post_url, header=headers, body=json_body)
        print(res_post.text)
        return res_post