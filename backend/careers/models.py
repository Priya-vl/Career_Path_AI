from django.db import models

class Career(models.Model):
    title = models.CharField(max_length=160, unique=True)
    sector = models.CharField(max_length=100)
    description = models.TextField()
    interests = models.JSONField(default=list, blank=True)
    skills = models.JSONField(default=list, blank=True)
    pathways = models.JSONField(default=list, blank=True)
    subjects = models.JSONField(default=list, blank=True)
    official_source_url = models.URLField(blank=True)
    source_verified = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
