from django.db import models
from django.contrib.auth.models import User, AnonymousUser


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.title

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if isinstance(instance, AnonymousUser):
            return None
        return representation
