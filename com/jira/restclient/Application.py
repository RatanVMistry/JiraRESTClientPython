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

        if len(projects) != 0 :
            projectID= input("Select project for detail : ")
            projectsIDList = []
            for i in range(len(projects)):
                projectsIDList.append(projects[i]['id'])
            if projectID in projectsIDList:
        #if any(projectID in d for d in projects):
                projectDetail = getProject.getProjectById(projectID)
                getProject.printProjectByID(projectDetail)
            else:
                print("You entred wrong project ID")

        else:
            print("There is no project in JIRA")


    else:

        getProject = GetProjects()
        #getIssues = GetIssueFromProject()
        projects = getProject.getProjects()

        getProject.printProjects(projects)

        if len(projects) != 0:
            projectID = input("Select project for issue in that projet  : ")
            projectsIDList = []
            for i in range(len(projects)):
                projectsIDList.append(projects[i]['id'])

            if projectID in projectsIDList:
                t = True
                while t == True:
                    getIssueFromProjecrt = GetIssueFromProject()
                    issueList = getIssueFromProjecrt.getIssueFromProject(projectID)

                    if len(issueList) > 0:
                        getIssueFromProjecrt.printIssuesFromProject(issueList)
                        issueID = input("Select issue ID : ")
                        issueIdList = []
                        for i in range(len(issueList)):
                            issueIdList.append(issueList[i]['id'])
                        if issueID in issueIdList:
                            issue = getIssueFromProjecrt.getIssueDetails(issueID)
                            getIssueFromProjecrt.printIssueDetails(issue)
                            t1 = input("Do you want another issue detail ?? Y/N ")
                            if (t1.lower() == 'n'):
                                t = False
                        else:
                            print("wrong Issue ID please enter correct one ")
                            t1 = input("Do you want another issue detail ?? Y/N ")
                            if (t1.lower() == 'n'):
                                t = False
                    else:
                        print("There is no issue in this project")
                        t = False
            else:
                print("No project for this ID")
        else:
            print("There is no project in JIRA")



    print("Done")
selectOptaion()