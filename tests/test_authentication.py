from utils.api_registracia import Ragister
from utils.api_autorizacia import Avtorizacia
from utils.checking import Posts_user

class Test_user():
    # def test_reg(self):
    #     res_post = Ragister.register_user()
    #     check_post = res_post.json()
    #     # Posts_user.check_status_code(res_post, 201)
    #     print(res_post.status_code)
    #     print('Регистрация прошла успешна')

    def test_avtorizacia_user(self):
        res_post = Avtorizacia.avrorizacia_user()
        check_post = res_post.json()
        Posts_user.check_status_code(res_post, 200)
        print(res_post.status_code)
        print('Авторизация прошла успешна')


