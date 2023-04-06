# Reorganize tasks into folders

from glob import glob
import json
from tqdm import tqdm
import requests
import json
from todoist_api_python.api import TodoistAPI
from tqdm import tqdm
import os

files = glob("projects/*.json")
os.makedirs("out", exist_ok=True)

tasks_json = []

for filename in tqdm(files): 
    task = None
    with open(filename, "r") as file:
        project = json.load(file)
        project['path'] = local_paths[project['id']]
        project['id'] = project['path']

    with open(filename, "w") as file:
        json.dump(project, file)