import json
import jinja2
import os
import requests
from com.jira.restclient.GetProjects import *
from com.jira.restclient.Utils import *

class CreateIssueForProject:

    def cutsomerInput(self):
        inputData = {}
        getProject = GetProjects()
        projects = getProject.getProjects()

        if len(projects) != 0:


            f = True
            while f == True:
                getProject.printProjects(projects)
                key = input("input key for project")
                if getProject.projectKeyInList(key, projects) == True:
                    # if any(projectID in d for d in projects):
                    f = False
                    inputData.update({"key": key})
                    summary = input("input labale for this jira ")
                    inputData.update({"summary": summary})
                    description = input("input description for this jira  ")
                    inputData.update({"description": description})
                    issuetypes = getProject.getCreateIssueType(key)



                    t = True
                    while t == True:
                        getProject.printIssueTypes(issuetypes)
                        issuetype = input("input issue type for this jira  ")
                        if issuetype in issuetypes:
                            inputData.update({"issuetype": issuetype})
                            t = False
                        else:
                            print("please check issue type")
                    assignee = input("input assignee")
                    inputData.update({"assignee": assignee})

                else:
                    print("You entered wrong project Key")

        else:
            print("There is no project in JIRA")

        return inputData

    def createPayload(self,inputData):
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        param = '''{
                  "fields": {
                    "project": {
                      "key": "{{ key }}"
                    },
                    "summary": "{{ summary }}",
                    "description": "{{ description }}",
                    "issuetype": {
                      "name": "{{ issuetype }}"
                      },
                    "assignee": {
                      "name": "{{ assignee }}"
                    }
                  }
                }'''
        t = jinja2.Template(param)
        result = t.render(inputData)
        return result

    def crateIssue(self, data):
        util = Utils()
        res = util.restPOST("/rest/api/2/issue", data)
        return res.json()
        #print(res.json())
    def printCreatedIssue(self,params):
        print("issue ID {id} and issue Key {key} is created".format(id=params['id'],key=params['key']))





'''
t = CreateIssueForProject()
dataFromCU = t.cutsomerInput()
data = t.createPayload(dataFromCU)
res = t.crateIssue(data)
t.printCreatedIssue(res)
'''
'''
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        #print(ROOT_DIR)

        inputData = {}
        key = input("input key for project")
        inputData.update({"key":key})
        summary = input("input labale for this jira ")
        inputData.update({"summary":summary})
        description = input("input description for this jira  ")
        inputData.update({"description":description})
        issuetype = input("input issue type for this jira  ")
        inputData.update({"issuetype":issuetype})
        assignee = input("input assignee")
        inputData.update({"assignee":assignee})
        '''
       # param =
'''
{
          "fields": {
            "project": {
              "key": "{{ key }}"
            },
            "summary": "{{ summary }}",
            "description": "{{ description }}",
            "issuetype": {
              "name": "{{ issuetype }}"
              },
            "assignee": {
              "name": "{{ assignee }}"
            }
          }
        }
'''

'''
        t = jinja2.Template(param)
        result = t.render(inputData)
        
        
        util = Utils()
        res = util.restPOST("/rest/api/2/issue",result)
        print(res.json())

'''