import requests

class ApiClient:

    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def register_user(self, email, password):
        payload = {
            "email": email,
            "password": password,
            "confirm_password": password
        }
        response = requests.post(f"{self.url}/register", headers=self.headers, json=payload)
        return response