from com.jira.restclient.DeleteIssueFromProject import *
from com.jira.restclient.GetIssuesFromProject import *
from com.jira.restclient.GetProjects import *
from com.jira.restclient.CreateIssueForProject import *
def selectOptaion():
    f = True
    while f == True:
        print("What you want to do today ?")
        print("1 - List projects and project details")
        print("2 - Issues and Issue Details from Project")
        print("3 - Creare a issue ")
        print("4 - Delete issue from project ")

        op = int(input("Enter number : "))
        #return op
        getProject = GetProjects()
        getIssueFromProjecrt = GetIssueFromProject()
        deletIssueFromProject = DeleteIssueFromProject()

        if(op == 1):

            projects = getProject.getProjects()

            if len(projects) != 0 :
                getProject.printProjects(projects)
                projectID= input("Select project for detail : ")
                if getProject.projectIDInList(projectID,projects) == True:
            #if any(projectID in d for d in projects):
                    projectDetail = getProject.getProjectById(projectID)
                    getProject.printProjectByID(projectDetail)
                else:
                    print("You entred wrong project ID")

            else:
                print("There is no project in JIRA")


        elif(op == 2):

            #getProject = GetProjects()
            #getIssues = GetIssueFromProject()
            projects = getProject.getProjects()



            if len(projects) != 0:
                getProject.printProjects(projects)
                projectID = input("Select project for issue in that projet  : ")
                if getProject.projectIDInList(projectID,projects) == True:
                    t = True
                    while t == True:

                        issueList = getIssueFromProjecrt.getIssueFromProject(projectID)

                        if len(issueList) > 0:
                            getIssueFromProjecrt.printIssuesFromProject(issueList)
                            issueID = input("Select issue ID : ")
                            if getIssueFromProjecrt.issueIDinIssueList(issueID,issueList)== True:
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

        elif(op == 3):
            t = CreateIssueForProject()
            dataFromCU = t.cutsomerInput()
            data = t.createPayload(dataFromCU)
            res = t.crateIssue(data)
            t.printCreatedIssue(res)

        else:
            projects = getProject.getProjects()
            if len(projects) != 0:
                getProject.printProjects(projects)
                projectID = input("Select project for issue in that projet  : ")
                if getProject.projectIDInList(projectID, projects) == True:
                    issueList = getIssueFromProjecrt.getIssueFromProject(projectID)
                    if len(issueList) > 0:
                        getIssueFromProjecrt.printIssuesFromProject(issueList)
                        issueID = input("Select issue ID : ")
                        if getIssueFromProjecrt.issueIDinIssueList(issueID, issueList) == True:
                            deletIssueFromProject.deleteIssue(issueID)
                        else:
                            print("wrong Issue ID please enter correct one ")

                    else:
                        print("There is no issue in this project")
                else:
                    print("No project for this ID")
            else:
                print("There is no project in JIRA")

        run = input("Do you want to run again ??? (Y/N)")
        if (run.lower() == 'n'):
            f = False
selectOptaion()