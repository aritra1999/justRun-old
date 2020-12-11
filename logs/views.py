from django.shortcuts import render

from .models import Submission

def log_view(request):
    subs = Submission.objects.all().order_by('-timestamp')
    submissions = subs[:10]
    total_submissions = subs.count()
    correct_submission = subs.filter(verdict="success").count()
    error_submission = subs.filter(verdict="error").count()
    context = {
        'submissions': submissions,
        'total': total_submissions,
        'correct': correct_submission,
        'error': error_submission,
    }
    return render(request, 'logs/log.html', context)

