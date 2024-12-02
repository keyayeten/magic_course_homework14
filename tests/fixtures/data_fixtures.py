import pytest
from utils.api_get_posts import LstPost
from utils.api_autorizacia import Avtorizacia

@pytest.fixture
def get_post_fix():
    posts = LstPost()
    res1 = Avtorizacia.avrorizacia_user()
    res_id = res1.json()
    res_ids = res_id.get('access')
    res = LstPost.lst_posts_user(res_ids)
    return res

def test_get_posts(get_post_fix):
    res = get_post_fix
    assert res.status_code == 200
