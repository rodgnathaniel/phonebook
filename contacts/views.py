from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

from .models import State

import json

# from .models import Game, Mode, State

import json

def home_view(request):

    return render(request, "contacts/phonebook.html", {})

def save_contact(request):
    
    data = json.loads(request.body)
    new_name = data['new_name']
    new_phone = data['new_phone']
    new_email = data['new_email']

                
    state = State(new_name=newname, new_phone=new_phone, new_email=new_email)
    state.save()
    return HttpResponse('hi')