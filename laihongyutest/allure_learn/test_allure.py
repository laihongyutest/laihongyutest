import allure
import pytest


def get_msg():
    return 5


@allure.feature('被测试的功能')
def test__002():
    assert get_msg() == 5


if __name__ == "__main__":
    pytest.main(['-s','test_allure.py','-q',''])
