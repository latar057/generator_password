from django.shortcuts import render
import random

def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):
    characters = list('abcdefghijklmnopqrsyuvwxyz')
    length = int(request.GET.get('length', 12))

    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSYUVWXYZ')

    if request.GET.get('numbers'):
        characters.extend('0123456789')

    if request.GET.get('special'):
        characters.extend('!@#$%^&*()_-')

    thepassword = ''
    for i in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {
        'password': thepassword
    })

# Используется фреймворк bootstrap
# https://getbootstrap.com/docs/4.4/getting-started/introduction/