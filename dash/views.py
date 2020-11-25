from django.http import JsonResponse
from django.shortcuts import render

from .utils import run_code

def home_view(request):
    context = {
        "title": "Editor"
    }

    return render(request, 'home/home.html', context)


def run(request):
    if request.method == "POST":
        code = request.POST.get('code')
        input = request.POST.get('input')
        language = request.POST.get('language')

        verdict, message, output, time, memory = run_code(code, input, language)
        if time is not None:
            time = round(time / 100, 3),
        else:
            time = 0.00

    response = {
        'verdict': verdict,
        'message': message,
        'time': time,
        'output': output,
        'memory': 243
    }

    return JsonResponse(response)

