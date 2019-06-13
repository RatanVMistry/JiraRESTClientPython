from com.jira.restclient.Utils import *
from com.jira.restclient.GetProjects import *
from com.jira.restclient.GetIssuesFromProject import *

class DeleteIssueFromProject:
    def deleteIssue(self, issueID):
        path = "/rest/api/2/issue/{id}".format(id=issueID)
        util = Utils()
        res = util.restDELETECall(path)
        ''
        if(res.status_code == 400):
            print("Error occurs.")
        elif(res.status_code == 401):
            print(" Calling user is not authenticated.")
        elif(res.status_code == 403):
            print("Calling user does not have permission to delete the issue.")
        elif(res.status_code == 404):
            print("Issue does not exist.")
        else:
            print("Issue {} was removed successfully".format(issueID))

    #print((type(res.status_code)))
'''
getProject = GetProjects()
project = getProject.getProjects()
getProject.printProjects(project)
projectID = input("enter Project id")
getIssues= GetIssueFromProject()
issues = getIssues.getIssueFromProject(projectID)
if(len(issues)>0):
    getIssues.printIssuesFromProject(issues)
    issue = input("Enter issue Id for delete.")
    deleteIssue = DeteIssue()
    deleteIssue.deleteIssue(issue)
else:
    print("there is no issues in this project")
'''