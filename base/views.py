from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

# rooms = [
#     {"id": 1, "name": "Python", "likes": "Let’s learn Python from basics to advanced"},
#     {"id": 2, "name": "JavaScript", "likes": "Learn JS and build interactive websites"},
#     {"id": 3, "name": "Django", "likes": "Master Django for full-stack web development"}
# ]


def home(req):
    rooms=Room.objects.all()
    context = {'rooms':rooms}
    return render(req,'base/home.html',context)

def room(req,pk):
    room = Room.objects.get(id=pk)

    context={'room':room}
    
    return render(req,'base/room.html',context)
