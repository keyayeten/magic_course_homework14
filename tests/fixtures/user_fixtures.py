import pytest

from utils.api_autorizacia import Avtorizacia

@pytest.fixture
def avt_fix():
    avtorizacia = Avtorizacia()
    res = Avtorizacia.avrorizacia_user()
    return res

def test_avt_user(avt_fix):
    res = avt_fix
    assert res.status_code == 200
    assert "refresh" in res.json()
