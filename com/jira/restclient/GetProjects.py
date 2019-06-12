from com.jira.restclient.Utils import *

#username = input("Enter Username = ")
#password = getpass("Enter Passwrod = ")
#endpoint = input("Enter URL of Jira = ")
#http://35.227.179.83:8080
'''
username= "admin"
password = "Welcome2cliqr!"
endpoint= "35.227.179.83:8080"

def restGETCall(username, password, endpoint, path):
    return requests.get("http://" + endpoint + path, auth=HTTPBasicAuth(username, password), verify=False)
'''
class GetProjects:

    def getProjects(self):
        path = "/rest/api/2/project"
        util = Utils()
        res = util.restGETCall(path)
        #res = requests.get("http://" + endpoint +"/rest/api/2/project", auth=HTTPBasicAuth(username, password), verify=False)
        '''
        for i in range(len(res.json())):

            print("ID = {id} -> KEY = {key} ->  NAME = {name}".format(id = res.json()[i]['id'],key = res.json()[i]['key'], name = res.json()[i]['name']))
        '''
        return res.json()

    def getProjectById(self, projectID):
        path = "/rest/api/2/project/{id}".format(id=projectID)
        util = Utils()
        res = util.restGETCall(path)
        return res.json()
        #print(res.json())
        #res = requests.get("http://" + endpoint +"/rest/api/2/project", auth=HTTPBasicAuth(username, password), verify=False)
        #print("ID = {id} -> KEY = {key} ->  NAME = {name}".format(id = res.json()['id'],key = res.json()['key'], name = res.json()['name']))

    def printProjects(self, projectList):
        for i in range(len(projectList)):
            print("ID = {id} -> KEY = {key} ->  NAME = {name}".format(id=projectList[i]['id'], key=projectList[i]['key'], name=projectList[i]['name']))

    def printProjectByID(self,projectDetail):
        print("ID = {id} -> KEY = {key} ->  NAME = {name}".format(id=projectDetail['id'], key=projectDetail['key'], name=projectDetail['name']))

#project = GetProjects()
#projectList = project.getProjects()
#project.printProjects(projectList)

#getProjects()
#projectID = input("Select Project ID = ")
#projectDetail = project.getProjectById(projectID)
#project.printProjectByID(projectDetail)
