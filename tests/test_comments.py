from utils.api_get_comments import LstComments
from utils.http_methods import Http_methods
from utils.api_autorizacia import Avtorizacia
from utils.checking import Posts_user
from utils.api_post_created_posts import CreatedLstPost
from utils.api_post_comments import CreatedComments
from utils.api_put_comments import CreatedPutComments
from utils.api_get_comments_id import GetCommentsId
from utils.api_patch_comments import CreatedPatchComments
from utils.api_delete_comments import DeletedComments
import json

class TestPosts:
    def test_lst_stat(self):
        res_post = Avtorizacia.avrorizacia_user()
        check_post = res_post.json()
        res = check_post.get("access")
        res_get = LstComments.lst_comments_user(res)
        lst_stat = res_get.text
        print(res_get.json())

        Posts_user.check_status_code(res_get, 200)
        print(res_get.status_code)
        print('Список комментраев получен')
        token = json.loads(res_get.text)
        print(list(token))

    def test_created_comments(self):
        res_post = Avtorizacia.avrorizacia_user()
        check_post = res_post.json()
        res = check_post.get("access")
        res_post_2 = CreatedLstPost.created_lst_posts_user(res)
        check_post_2 = res_post_2.json()
        ids = check_post_2.get("id")
        res_posts = CreatedComments.created_comments(res, ids)
        lst_stat = res_posts.text
        print(res_posts.json())
        Posts_user.check_status_code(res_posts, 201)
        print(res_posts.status_code)
        print('Комментарий создан')


    def test_created_put_comments(self):
        res_post = Avtorizacia.avrorizacia_user()
        check_post = res_post.json()
        res = check_post.get("access")
        res_post_2 = CreatedLstPost.created_lst_posts_user(res)
        check_post_2 = res_post_2.json()
        ids = check_post_2.get("id")
        res_post_3 = CreatedComments.created_comments(res, ids)
        check_post_3 = res_post_3.json()
        ids2 = check_post_3.get("id")
        res_put = CreatedPutComments.created_put_comments(res, ids2)
        lst_stat = res_put.json()
        id_res_get = lst_stat.get("id")
        print(res_put.json())
        Posts_user.check_status_code(res_put, 200)
        print(res_put.status_code)
        print('Комментарий изменен')

        get_id = GetCommentsId.get_id_comments(res, id_res_get)
        res_get_id2 = get_id.json()
        Posts_user.check_status_code(get_id, 200)
        print(f'Комментарий {res_get_id2}')

        patch_comments = CreatedPatchComments.created_patch_comments(res, id_res_get)
        res_patch_comments = patch_comments.json()
        res_patch_comments1 = res_patch_comments.get("text")
        Posts_user.check_status_code(patch_comments, 200)
        Posts_user.check_json_value(patch_comments, 'text', 'Hello my friends')
        print(f'Поле post изменено {res_patch_comments1}')

        delete_comments = DeletedComments.delete_comments(res, id_res_get)
        Posts_user.check_status_code(delete_comments, 204)
        print('Комментарий удален')





