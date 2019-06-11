from com.jira.restclient import Utils, GetIssuesFromProject, GetProjects


def deleteIssue(issueID):
    path = "/rest/api/2/issue/{id}".format(id=issueID)
    res = Utils.restDELETECall(path)
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
GetProjects.getProjects()
projectID = input("enter Project id")
GetIssuesFromProject.getIssueFromProject(projectID)
issue = input("Enter issue Id for delete.")
deleteIssue(issue)