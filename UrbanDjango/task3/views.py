from django.shortcuts import render

# Create your views here.

data = {
    1:{'name': 'The Witcher 3: Wild Hunt', 'description': 'Классная игра'},
    2:{'name': 'Grand Theft Auto V', 'description': 'Классная игра'},
    3:{'name': 'The Elder Scrolls V: Skyrim', 'description': 'Классная игра'},
}
def shop(request):
    return render(request, 'third_task/shop.html', {'data':data})
