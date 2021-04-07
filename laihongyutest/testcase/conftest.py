import pytest


# conftest.py
@pytest.fixture(scope='session')
def get_userid():
    token = 'qeehfjejwjwjej11sss@22'
    print('获取到token:%s' % token)
    return token
