from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'second_task/func_template.html')
