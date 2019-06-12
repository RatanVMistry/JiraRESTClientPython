from com.jira.restclient.GetIssuesFromProject import *
from com.jira.restclient.GetProjects import *

def selectOptaion():
    print("What you want to do today ?")
    print("1 - List projects and project details")
    print("2 - Issues and Issue Details from Project")
    op = int(input("Enter number : "))
    #return op
    if(op == 1):
        getProject = GetProjects()
        projects = getProject.getProjects()
        getProject.printProjects(projects)
        projectID= input("Select project for detail : ")
        if projectID in projects:
            projectDetail = getProject.getProjectById(projectID)
            getProject.printProjectByID(projectDetail)
        else:
            print("There is no project Id in list")
    else:

        getProject = GetProjects()
        #getIssues = GetIssueFromProject()
        projects = getProject.getProjects()
        print(projects)
        getProject.printProjects(projects)
        projectID = int(input("Select project for issue in that projet  : "))

        t = True
        while t == True:
            getIssueFromProjecrt = GetIssueFromProject()
            issueList = getIssueFromProjecrt.getIssueFromProject(projectID)
            if (len(issueList) > 0):
                getIssueFromProjecrt.printIssuesFromProject(issueList)
                issueID = input("Select issue ID : ")
                issue = getIssueFromProjecrt.getIssueDetails(issueID)
                getIssueFromProjecrt.printIssueDetails(issue)
                t1 = input("Do you want another issue detail ?? Y/N ")
                if (t1.lower() == 'n'):
                    t = False
            else:
                print("There is no issue in this project")
                t = False




        print("Done")
selectOptaion()