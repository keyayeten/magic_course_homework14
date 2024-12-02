from utils.api_autorizacia import Avtorizacia
from utils.api_post_created_posts import CreatedLstPost
from utils.api_get_posts import LstPost
from utils.checking import Posts_user
from utils.api_get_posts_id import GetLstPostId
from utils.api_put_posts_id import PutLstPostId
from utils.api_patch_post_id import PatchLstPostId
from utils.delete_posts import DeleteLstPostId
import json


class TestPosts:
    def test_lst_stat(self):
        res_post = Avtorizacia.avrorizacia_user()
        check_post = res_post.json()
        res = check_post.get("access")
        res_get = LstPost.lst_posts_user(res)
        lst_stat = res_get.text
        print(res_get.json())

        Posts_user.check_status_code(res_get, 200)
        print(res_get.status_code)
        print('Список статей найден')
        token = json.loads(res_get.text)
        print(list(token))

    def test_created_lst_stat(self):
        res_post1 = Avtorizacia.avrorizacia_user()
        check_post = res_post1.json()
        res = check_post.get("access")
        res_post = CreatedLstPost.created_lst_posts_user(res)
        lst_stat = res_post.text
        print(res_post.json())

        Posts_user.check_status_code(res_post, 201)
        print(res_post.status_code)
        print('Статья создана')
        token = json.loads(res_post.text)
        print(list(token))

    def test_get_posts_id(self):
        res_post1 = Avtorizacia.avrorizacia_user()
        check_post = res_post1.json()
        res = check_post.get("access")
        res_post = CreatedLstPost.created_lst_posts_user(res)
        lst_stat = res_post.json()
        res_id = lst_stat.get("id")
        get_id = GetLstPostId.lst_posts_user_id(res, res_id)
        Posts_user.check_status_code(get_id, 200)
        print(get_id.json())

        Posts_user.check_status_code(res_post, 201)
        print(res_post.status_code)
        print('Статья создана')
        token = json.loads(res_post.text)
        print(list(token))

    def test_put_posts_id(self):
        res_post1 = Avtorizacia.avrorizacia_user()
        check_post = res_post1.json()
        res = check_post.get("access")

        res_post = CreatedLstPost.created_lst_posts_user(res)
        lst_stat = res_post.json()
        res_id = lst_stat.get("id")
        res_put_id = PutLstPostId.lst_put_user_id(res, res_id)
        Posts_user.check_status_code(res_put_id, 200)
        print(res_put_id.status_code)
        Posts_user.check_json_value(res_put_id, 'title', 'December')
        print('Данное поле присутствует')

        res_patch_posts = PatchLstPostId.lst_patch_user_id(res, res_id)
        Posts_user.check_status_code(res_patch_posts, 200)
        print(res_put_id.status_code)
        Posts_user.check_json_value(res_patch_posts, 'title', 'Happy December')
        print('Данное поле Happy December присутствует')

        res_delete_posts = DeleteLstPostId.lst_delete_user_id(res, res_id)
        Posts_user.check_status_code(res_delete_posts, 204)
        print(res_delete_posts.status_code)
        print(f'Пост удален с id {res_id}')



