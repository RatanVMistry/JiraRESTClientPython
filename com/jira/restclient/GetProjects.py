from com.jira.restclient.Utils import *

#username = input("Enter Username = ")
#password = getpass("Enter Passwrod = ")
#endpoint = input("Enter URL of Jira = ")
#http://35.227.179.83:8080

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

    def projectIDInList(self,projectID,projects):
        projectIDList = []
        for i in range(len(projects)):
            projectIDList.append(projects[i]['id'])
        if projectID in projectIDList:
            return True
        else:
            return False

    def projectKeyInList(self,projectKey,projects):
        projectKeyList = []
        for i in range(len(projects)):
            projectKeyList.append(projects[i]['key'])
        if projectKey in projectKeyList:
            return True
        else:
            return False

    def getCreateIssueType(self,projectKey):
        path = "/rest/api/2/issue/createmeta?projectKeys={key}".format(key=projectKey)
        util = Utils()
        res = util.restGETCall(path)
        projecsList = res.json()['projects']
        # print(projecsList)
        issueTypes = []
        for i in range(len(projecsList)):
            for j in range(len(projecsList[i]['issuetypes'])):
                issueTypes.append(projecsList[i]['issuetypes'][j]['name'])
        return issueTypes
        #print(issueTypes)
        #return res.json()
        #print(res.json())

    def printProjects(self, projectList):
        for i in range(len(projectList)):
            print("ID = {id} -> KEY = {key} ->  NAME = {name}".format(id=projectList[i]['id'], key=projectList[i]['key'], name=projectList[i]['name']))

    def printProjectByID(self,projectDetail):
        print("ID = {id} -> KEY = {key} ->  NAME = {name}".format(id=projectDetail['id'], key=projectDetail['key'], name=projectDetail['name']))

    def printIssueTypes(self,issueTypeList):
        for i in range(len(issueTypeList)):
            print(str(i+1) + " - " + issueTypeList[i])

#project = GetProjects()
#projectList = project.getProjects()
#project.printProjects(projectList)

#getProjects()
#projectID = input("Select Project ID = ")
#projectDetail = project.getProjectById(projectID)
#project.printProjectByID(projectDetail)

#projectIssuTypes = project.getCreateIssueType("OT")
#project.printIssueTypes(projectIssuTypes)
#projecsList = res['projects']
#print(projecsList)
#issueTypes = []
#for i in range(len(projecsList)):
#    for j in range(len(projecsList[i]['issuetypes'])):
#       issueTypes.append(projecsList[i]['issuetypes'][j]['name'])
#print(issueTypes)


#print(res['projects'])