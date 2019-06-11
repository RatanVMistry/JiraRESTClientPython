import json
import requests
from getpass import getpass
from requests.auth import HTTPBasicAuth


class Utils:

    def __init__(self):
        self.username= "admin"
        self.password = "Welcome2cliqr!"
        self.endpoint= "35.227.179.83:8080"

    def restGETCall(self, path):
        return requests.get("http://" + self.endpoint + path, auth=HTTPBasicAuth(self.username, self.password), verify=False)
    def restDELETECall(self, path):
        return requests.delete("http://" + self.endpoint + path, auth=HTTPBasicAuth(self.username, self.password), verify=False)