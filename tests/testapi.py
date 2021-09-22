from yandex.yaapi import Yadisk_API


with open('/Users/rup/Work/BTC/Rules.txt') as file:
    token = file.readline().strip('\n')
test_session = Yadisk_API(token)
negative_session = Yadisk_API('FakeToken')


class TestYaApi():

    def test_response(self):
        assert test_session.get_info().status_code == 200

    def test_make_dir(self):
        assert test_session.make_dir('test_dir').status_code == 201

    def test_check_dir(self):
        assert test_session.get_files('test_dir').status_code == 200

    def test_rm_dir(self):
        assert test_session.rm_dir('test_dir').status_code == 204

    def test_negative_response(self):
        assert negative_session.get_info().status_code == 401

    def test_negative_rm_dir(self):
        assert test_session.rm_dir('FakeDir').status_code == 404

    def test_negative_check_dir(self):
        assert test_session.get_files('FakePath').status_code == 404
