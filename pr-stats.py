import argparse
import requests
import json
import getpass
username = str(input("Enter your GitHub username: "))
password = getpass.getpass(prompt='Enter your password: ')


def ArgParser():
    parser = argparse.ArgumentParser(description='Pull Requests Statistics')
    parser.add_argument("-v", "--version",
                        action='version',
                        help="Shows program's version",
                        version="0.0.1")
    parser.add_argument("-r", "--repository",
                        required=True,
                        dest='repository',
                        help='Repository name user/repository',
                        default='alenaPy/devops_lab')
    parser.add_argument("-m", "--merged",
                        action='store_true',
                        help='Statistics about merged/closed rate.')
    parser.add_argument("-c", "--created",
                        action='store_true',
                        help='Pull requests creation date')
    parser.add_argument("-l", "--labels",
                        action='store_true',
                        help='Labels in repository')
    parser.add_argument("-la", "--attached",
                        action='store_true',
                        help='Labels attached to pull request')
    parser.add_argument("-p", "--pushed",
                        action='store_true',
                        help='Time when pull request was pushed')
    return parser.parse_args()


def Pulls(arg):
    r = Parse("pulls")

    for item in r.json():
        res = ""
        if arg.merged:
            res += " " + Merge(item)
        if arg.created:
            res += " " + Create(item)
        if arg.attached:
            res += " " + Attached(item)
        if arg.pushed:
            res += " " + Pushed(item)
        print(item.get("head").get("label") + res)


def Create(item):
    date, time = item.get("created_at").split("T")
    return "Created at " + time[:-1] + " " + date


def Pushed(item):
    if item.get("state") == 'open':
        date, time = item.get("head").get("repo").get("pushed_at").split("T")
        return "Pushed at " + time[:-1] + " " + date
    else:
        return "Pull Request was closed"


def Attached(item):
    labels = item.get("labels")
    if labels:
        return "Labels attached: " + labels[0]['name']
    else:
        return "No labels attached"


def Labels():
    r = Parse("labels")
    res = "Labels at repository:"
    print(res)
    for item in r.json():
        res = item.get("name")
        print(res)


def State(item):
    state = "State: \033[92m" + item.get("state") + "\033[0m"
    if item.get("state") == 'open':
        return state
    else:
        return state + " Closed at:" + item.get('closed_at')


def Merge(item):
    merged = item.get('merged_at')
    if merged:
        date, time = item.get('merged_at').split("T")
        return "Merged at " + time[:-1] + " " + date + " " + State(item)
    else:
        return "Not merged " + State(item)


def Parse(url):
    if url == 'pulls':
        request_url = "https://api.github.com/repos/" + arg.repository + "/pulls?&per_page=100"
        payload = {"state": "all", "auth": [username, password]}
    elif url == "labels":
        request_url = "https://api.github.com/repos/" + arg.repository + "/labels"
        payload = {"auth": [username, password]}

    r = requests.get(request_url, params=payload)

    if r.status_code == 200:
        return r
    else:
        print("\033[91mERROR:\033[0m", r.json().get('message'))
        exit()

arg = ArgParser()

if arg.merged or arg.created or arg.attached or arg.pushed:
    Pulls(arg)
if arg.labels:
    Labels()
