from django.shortcuts import render
from django.http import HttpResponse

rooms = [
    {"id": 1, "name": "Python", "likes": "Let’s learn Python from basics to advanced"},
    {"id": 2, "name": "JavaScript", "likes": "Learn JS and build interactive websites"},
    {"id": 3, "name": "Django", "likes": "Master Django for full-stack web development"}
]


def home(req):
    context = {'rooms':rooms}
    return render(req,'base/home.html',context)

def room(req,pk):
    room = None
    for i in rooms:
        if i['id']==int(pk):
            room=i

    context={'room':room}
    
    return render(req,'base/room.html',context)
