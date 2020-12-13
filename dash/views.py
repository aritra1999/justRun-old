from django.http import JsonResponse
from django.shortcuts import render

from .utils import round_off
from .run import run_code
from logs.models import Submission
import requests
import json

def home_view(request):
    context = {
        "title": "Editor"
    }

    return render(request, 'home/home.html', context)



# Run APi Endpoint
def run(request):
    if request.method == "POST":
        if request.POST.get('language') == "python":
            payload = {
                "language": request.POST.get('language'),
                "code": request.POST.get('code'),
                "input": request.POST.get('input')
            }
            url = "https://nvdk5lgoek.execute-api.ap-south-1.amazonaws.com/JustRunStage"
            r = json.loads(requests.post(url, data=json.dumps(payload)).text)
            verdict = r['verdict']
            message = r['message']
            output = r['output']
            time = r['time']
            memory = r['memory']

        else:
            verdict, message, output, time, memory = run_code(
                request.POST.get('code'), request.POST.get('input'), request.POST.get('language')
            )

        Submission.objects.create(
            language=request.POST.get('language'),
            verdict=verdict,
            message=message,
            time_taken=time,
            mem_used=memory
        ).save()

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

