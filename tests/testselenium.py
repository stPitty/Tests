from yandex.yaauthbyselen import yandex_auth
import pytest

with open('/Users/rup/Work/BTC/Rules.txt') as file:
    file.readline().strip('\n')
    my_login = file.readline().strip('\n')
    my_pass = file.readline().strip('\n')
browser_driver_path = '/Users/rup/Downloads/py-homeworks-advanced-master/chromedriver'

class TestYaAuth():

    @pytest.mark.parametrize("login, passw, f_name, l_name", [
        [my_login, my_pass, 'Петр', 'Станкин']
    ])
    def test_ya_auth(self, login, passw, f_name, l_name):
        assert yandex_auth(login, passw, browser_driver_path) == (f_name, l_name)
