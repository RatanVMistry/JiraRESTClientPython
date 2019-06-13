import json
import requests
from getpass import getpass
from requests.auth import HTTPBasicAuth


class Utils:

    def __init__(self):
        f = open("/Users/ratmistr/JiraRestClient/com/jira/restclient/auth.json", 'r')
        try:
            data = json.load(f)
            #return data
        except ValueError as e:
            print
            "Incorrect json format"
            print
            e
            exit()
        finally:
            f.close()
        self.username= data['username']
        self.password = data['password']
        self.endpoint= data['endPoint']



    def restGETCall(self, path):
        return requests.get("http://" + self.endpoint + path, auth=HTTPBasicAuth(self.username, self.password), verify=False)
    def restDELETECall(self, path):
        return requests.delete("http://" + self.endpoint + path, auth=HTTPBasicAuth(self.username, self.password), verify=False)