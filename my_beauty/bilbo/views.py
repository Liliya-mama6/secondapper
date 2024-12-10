from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

users = ['Anton', 'Sasha', 'Roma', 'Alena']


def i1(request):
    global users
    info={}
    if request.method == 'POST':
        name = request.POST.get('name')
        if name in users:
            info['error'] ='This user yet was'
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        if str(password) != str(repeat_password):
            info['error'] ='Wrong password'
        age = int(request.POST.get('age'))
        s = {}
        if age < 18:
            info['error'] = 'you are baby'
        return HttpResponse('all was successful')
    return render(request, 'test.html')


from .forms import User


def i2(request):
    info={}
    global form, users
    if request.method == 'POST':
        form = User(request.POST)
        s=[]
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            s.append(name)
            s.append(age)
            s.append(password)
            s.append(repeat_password)
        if s[0] in users:
            info['error'] = 'This user yet was'
        if s[2]!=s[3]:
            info['error'] ='wrong password'
        if int(s[1])<18:
            info['error'] ='you are baby'
        return HttpResponse('all was successful')
    else:
        form = User()
    return render(request, 'test.html', {'form': form})
