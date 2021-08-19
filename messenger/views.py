from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import message
from django.utils import timezone
from .models import Message
from .views import *
from .forms import MessageForm
# Create your views here.

def receive_m(request):
    chats = Message.objects.filter(receiver = request.user)
    return render(request, 'm_received.html', {'chats':chats})

def send_m(request):
    chats = Message.objects.filter(sender = request.user)
    return render(request, 'm_send.html', {'chats':chats})

def detail_m(request, id):
    chat = get_object_or_404(Message, pk = id)
    return render(request, 'm_detail.html', {'chat':chat})

def new_m(request):
    if request.method == 'POST':
        chatform = MessageForm(request.POST, request.FILES)
        if chatform.is_valid():
            chat = chatform.save(commit = False)
            chat.pub_date = timezone.now()
            chat.sender = request.user
            chat.save()
        return redirect('messenger:detail_m', chat.id)
    else:
        chatform = MessageForm()
        return render(request, 'm_new.html', {'chatform':chatform})

def delete_m(request, id):
    delete_message = Message.objects.get(id = id)
    delete_message.delete()
    return redirect('messenger:received_m')
