from glob import glob
import json
from tqdm import tqdm
import requests
import json
from todoist_api_python.api import TodoistAPI
from tqdm import tqdm
import os



files = glob("tasks/**.json")   

BASE_URL = "https://api.todoist.com/rest/v2/"
HEADERS = {"Authorization": "Bearer 82d97566b97c9dbfa781b53049ed284953cd4c99"}

tasks_json = []

for filename in tqdm(files): 
    task = None
    with open(filename, "r") as filename:
        task = json.load(filename)
        tasks_json.append(task)

projects = requests.get(BASE_URL + "projects", headers=HEADERS).json()
for project in projects:
    prefix = ""
    if project['parent_id'] is not None:
        prefix = project['parent_id'] + "/"

    dir = f"projects/{prefix}"
    os.makedirs(dir, exist_ok=True)

    project_tasks = [task for task in tasks_json if task['project_id'] == project['id']]
    project['tasks'] = project_tasks    
    
    with open(f"{dir}/{project['id']}.json", "w") as file:
        json.dump(project, file)

