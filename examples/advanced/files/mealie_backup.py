#!/usr/bin/env python3
import os
import json
from zipfile import ZipFile
import requests

# get token
token = os.getenv("MEALIE_TOKEN")
api_url = os.getenv("MEALIE_API_URL")
datadir = os.getenv("MEALIE_DATADIR")
headers = { "Authorization": f"Bearer {token}" }

def get_name(response):
    if response.status_code == 200:
        n = response.json()
        name = n['imports'][0]['name']
        return name
    return None

def get_old_backups(response):
    names=[]
    for n in response.json()['imports'][6:]:
        names.append(n['name'])
    return names

def clean_old_backups(names):
    for n in names:
        print(f"removing old backup {n}")
        r = requests.delete(api_url + f"admin/backups/{n}", headers=headers, timeout=5)
        if r.status_code == 200:
            print("Success")

def get_filetoken(name):
    f = requests.get(api_url + f"admin/backups/{name}", headers=headers, timeout=5)
    if f.status_code == 200:
        return f.json()['fileToken']
    return None

# Create backup
requests.post(api_url + 'admin/backups', headers=headers, timeout=5)
# Get backup list
backup = requests.get(api_url + 'admin/backups', headers=headers, timeout=5)
name = get_name(backup)
filetoken = get_filetoken(name)

download = requests.get(api_url + f"utils/download?token={filetoken}", timeout=5)
open(name, "wb").write(download.content)

with ZipFile(name, 'r') as z:
    z.extractall(path=datadir)

# Cleanup
clean_old_backups(get_old_backups(backup))
