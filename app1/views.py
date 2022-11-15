from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse, JsonResponse


def home(request):
    # print('line 5')
    return render(request, 'home.html')

def room(request, room):
    username=request.GET.get('username')
    # room_details=Room.objects.get(name=room)
    room_details=Room.objects.filter(name=room)
    # print('line 8')
    # print(room_details.values())
    return render(request, 'room.html',{
        'username' : username,
        'room' : room, 
        'room_details' : room_details
    })

def  checkroom(request):
    room=request.POST['room-name-input']
    username=request.POST['user-name-input']
    print(username)
    if Room.objects.filter(name=room).exists():
        return redirect('/' + room + '/?username=' + username )  
    else:
        new_room=Room.objects.create(name=room)
        new_room.save()
        return redirect('/' + room + '/?username=' + username )  

def send(request):
    message=request.POST['message']
    username=request.POST['username']
    room=request.POST['room']
    # print(username)
    # print(room) 
    new_msg = Message.objects.create(value=message, user=username, room=room)
    new_msg.save()
    return HttpResponse('message sent successfully')

def getMessages(request, room):
    roomObj = Room.objects.get(name=room)
    messages=Message.objects.filter(room = roomObj)
    # print(messages)
    return JsonResponse({
        'messages' : list(messages.values())
    })
