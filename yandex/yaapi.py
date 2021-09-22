import requests


class Yadisk_API:

    def __init__(self, token):
        self.token = token
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
        self.url = "https://cloud-api.yandex.net/v1/disk"

    def get_info(self):
        response = requests.get(self.url, headers=self.headers)
        return response

    def get_files(self, path=' '):
        params = {'path': path}
        response = requests.get(self.url+'/resources', headers=self.headers, params=params)
        return response

    def make_dir(self, path):
        params = {'path': path}
        response = requests.put(self.url+'/resources', headers=self.headers, params=params,)
        return response

    def rm_dir(self, path):
        params = {'path': path}
        response = requests.delete(self.url+'/resources', headers=self.headers, params=params,)
        return response
