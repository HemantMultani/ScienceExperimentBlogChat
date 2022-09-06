from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import Room, Message


def chat_home(request, exp):
    return render(request, 'chat_home.html', {'experiment_name': exp})


def room(request, room):
    room_details = Room.objects.get(name=room)
    username = request.GET.get('username')
    return render(request, 'room.html', {
        'room': room,
        'username': username,
        'room_details': room_details,
    })


def checkview(request, exp):
    room = exp
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)


def send(request):
    username = request.POST['username']
    room_id = request.POST['room_id']
    message = request.POST['message']

    new_message = Message.objects.create(
        text=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')


def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})
