import subprocess
import json

def open_app(name):
    apps = get_apps()
    path = apps.get(name)
    if path:
        subprocess.Popen(path)
        return f"Opening {name} app."
    else:
        return f"{name} app not found"

def get_apps():
    with open("apps.json", "r") as file:
        apps = json.load(file)
    return apps

def get_app_names():
    apps = get_apps()
    return list(apps.keys())
