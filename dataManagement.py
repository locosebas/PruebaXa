import json
import requests

with open('db.json') as file:
    data = json.load(file)

def getById(id):
    for song in data['feed']['results']:
        if song["id"]==id:
            return song
    return "song is not on the list"

def getByname(name):

    for song in data['feed']['results']:
        if song["name"]==name:
            return song
    return "song is not on the list"

def getByTop(top):
    return data['feed']['results'][top]

def top50():
    return data['feed']['results'][:50]

def deleteByTop(top):
    if  len(data['feed']['results'])+1>top:
        data['feed']['results'].pop(top)
        with open('db.json','w') as file:
            json.dump(data, file, indent=4)
        return True
    else: 
         False

def addItem(item):
    data['feed']['results'].append(item)
    with open('db.json','w') as file:
        json.dump(data, file, indent=4)
    return item

def update():
    newData = requests.get('https://rss.applemarketingtools.com/api/v2/us/music/most-played/100/songs.json').json()
    with open('db.json','w') as file:
        json.dump(newData, file, indent=4)
    return True
