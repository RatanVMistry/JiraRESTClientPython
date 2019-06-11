from com.jira.restclient.GetProjects import *
from com.jira.restclient.Utils import *

class GetIssueFromProject:

    def getIssueFromProject(self, projectId):
        path = "/rest/api/2/search?jql=project={}".format(projectId)
        util = Utils()
        res = util.restGETCall(path)
        issues = res.json()['issues']
        if(len(issues)>0):
            for i in range(len(issues)):
                print("{id} -> {key} -> {summary} ".format(id=issues[i]['id'],key=issues[i]['key'],summary=issues[i]['fields']['summary']))
        else:
            print("No issue in ")
            return 0
        #print(issues)
        #print(res.json())

    def getIssueDetails(self, issueID):
        path = "/rest/api/2/issue/{id}".format(id=issueID)
        util = Utils()
        res = util.restGETCall(path)
        issue=res.json()
        #print(issue)
        print("============= Issue detail for Issue ID {id}===================".format(id=issueID))
        print("{key} :  {summary}".format(key=issue['key'],summary=issue['fields']['summary']))
        print("Issue type : {type}".format(type=issue['fields']['issuetype']['name']))
        print("Issue creator : {creator}".format(creator=issue['fields']['creator']['name']))
        print("Issue reporter : {reporter}".format(reporter=issue['fields']['reporter']['name']))
        print("Priority : {priority}".format(priority=issue['fields']['priority']['name']))
        print("Status : {status}".format(status=issue['fields']['status']['name']))


project = GetProjects()
project.getProjects()
projectId = input("Select projcet for issues :")
t = True
while t == True:
    getIssueFromProjecrt = GetIssueFromProject()
    getIssueFromProjecrt.getIssueFromProject(projectId)

    issueID = input("Select issue ID : ")
    getIssueFromProjecrt.getIssueDetails(issueID)
    t1 = input("Do you want another issue detail ?? Y/N ")
    if(t1.lower() == 'n'):
        t = False

