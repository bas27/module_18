from django.shortcuts import render

# Create your views here.

data = {
    'games':
        ['The Witcher 3: Wild Hunt', 'Grand Theft Auto V', 'The Elder Scrolls V: Skyrim']
        }
def shop(request):
    return render(request, 'fourth_task/shop.html', {'data':data})
