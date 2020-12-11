from django.db import models


class Submission(models.Model):
    language = models.CharField(max_length=10, null=True, blank=True)
    verdict = models.CharField(max_length=10, null=True, blank=True)
    message = models.CharField(max_length=100, null=True, blank=True)
    time_taken = models.CharField(max_length=10, null=True, blank=True)
    mem_used = models.CharField(max_length=10, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.language)

