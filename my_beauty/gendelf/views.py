from django.shortcuts import render

# Create your views here.
def shop(request):
    context={'games':['Saper', 'Pasans']}
    return render(request, 'shop.html')