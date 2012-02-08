import requests

from base import BaseBackend


class Backend(BaseBackend):

    def authenticate(self):
        login_url = self.config['root_url'] + 'login.html'
        response = requests.post(login_url, {'password': self.config['login_pin']})
        self.cookies = response.cookies
