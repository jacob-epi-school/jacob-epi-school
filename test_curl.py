import requests
import datetime
user = 'jacob-epi-school'
# repo = 'jacob-epi-school.github.io'
currentFile = 'jacob.html'

commitIds = []

dateSubmitted = '2021-06-14 04:40:02'
dateSubmitted = datetime.datetime.strptime(dateSubmitted, "%Y-%m-%d %H:%M:%S")
r = requests.get('https://api.github.com/users/'+user+'/repos')
repos = []
requestedRepos = r.json()
for repo in requestedRepos:
    repos.append(repo['name'])
finalDict = {}
for repo in repos:
    if(repo != None):
        c = requests.get('https://api.github.com/repos/'+user+'/'+repo+'/commits')
        commit = c.json()
        treeURL = commit[0]['commit']['tree']['url']
        if(treeURL != None):
            t = requests.get(treeURL+'?recursive=1')
            paths = t.json()
            if(paths != None):
                fileNames = []
                for path in paths['tree']:
                    fileNames.append(path['path'])
                finalDict.update({repo: fileNames})
print(finalDict)
for key in finalDict.keys():
    for name in finalDict[key]:
        print(name)
    print()
# commits = r.json()
# if(len(commits) < 2):
#     # ignore because 1 or less commits
#     print("Initial commit, don't care about dates")
# else:
#     index = 0
#     for commit in commits:
#         # if commit['commit']['author']['date'] > dateSubmitted:
#         dateCommited= commit['commit']['author']['date']
#         date = datetime.datetime.strptime(dateCommited, "%Y-%m-%dT%H:%M:%SZ")
#         if(date > dateSubmitted):
#             # print('commit date was greater at date: ' + str(date))
#             # print(commit['commit'].keys())
#             commitIds.append(dict({'commit': [str(index), str(date), commit['html_url'], commit['commit']['message']]}))
#             index = index + 1
#     print("There has been " + str(index) + " commits since submission with the commits being:")
#     i = 0
#     for commit in commitIds:
#         print(commit['commit'])
#         # i += 1
#     # url = commitIds[0][0][1]
#     # r = requests.get(url, allow_redirects=True)
#     # # print(r.content)