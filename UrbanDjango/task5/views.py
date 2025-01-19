from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

users = []
info = {}

def sign_up_by_django(request):
    return render(request, 'sign_up_by_django.html')


def sign_up_by_html(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        age = request.POST.get('age')
        users.append(username)
        info[username] = password, age
        return HttpResponse('Форма успешно отправлена')
    
    print(f"Name: {username}")
    print(f"Name: {password}")
    print(f"Name: {age}")

    return render(request, 'fifth_task/registration_page.html')