from django.http import JsonResponse
from django.shortcuts import render

import signal
from .utils import (
    run_code,
    signal_handler,
    round_off,
    Timeout
)

def home_view(request):
    context = {
        "title": "Editor"
    }

    return render(request, 'home/home.html', context)


def run(request):
    if request.method == "POST":

        verdict, message, output, time, memory = run_code(
            request.POST.get('code'), request.POST.get('input'), request.POST.get('language')
        )

        response = {
            'verdict': verdict,
            'message': message,
            'time': round_off(time),
            'output': output,
            'memory': round_off(memory)
        }

        return JsonResponse(response)
    else:
        return JsonResponse({"error", "Invalid Request!", None, None, None})

