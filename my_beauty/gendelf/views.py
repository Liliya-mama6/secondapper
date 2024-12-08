from django.shortcuts import render

# Create your views here.
def shop(request):
    games=['Saper', 'Pasans']
    context = {'games':games}
    return render(request, 'shop.html', context)