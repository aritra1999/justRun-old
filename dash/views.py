from django.http import JsonResponse
from django.shortcuts import render

from .utils import round_off
from .run import run_code
from logs.models import Submission

def home_view(request):
    context = {
        "title": "Editor"
    }

    return render(request, 'home/home.html', context)

# Run APi Endpoint
def run(request):
    if request.method == "POST":
        # runcode(code:str, input:str, language)
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

