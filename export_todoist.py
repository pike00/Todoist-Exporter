# Export Todoist

import requests
import json
from todoist_api_python.api import TodoistAPI
from tqdm import tqdm
import config

BASE_URL = "https://api.todoist.com/rest/v2/"
HEADERS = {"Authorization": f"Bearer {config.bearer_token}"}

projects = requests.get(BASE_URL + "projects", headers=HEADERS).json()

tasks = requests.get(BASE_URL + "tasks", headers=HEADERS).json()

for project in projects: 
    print(f"# {project['name']}")

    cur_tasks = [task for task in tasks if task['project_id'] == project['id']]
    for task in cur_tasks:
        print()

# for task in tqdm(tasks): 
#     project = [project for project in projects if project['id'] == task['project_id']]
#     task['project'] = project


#     comments = requests.get(f"{BASE_URL}comments?task_id={task['id']}", headers=HEADERS).json()
#     task['comments'] = comments

#     # with open(f"tasks/{task['id']}.json","w", encoding="utf-8") as file:
#     #     json.dump(task, file)

#     tasks_json.append(task)

# with open(f"../tasks.json", "w") as file:
#     json.dump(tasks_json,file)