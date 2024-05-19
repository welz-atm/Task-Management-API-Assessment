import json
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.models import AnonymousUser
from rest_framework import viewsets, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Task
from .serializers import TaskSerializer, UserSerializer, CustomTokenObtainPairSerializer
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


def real_data(request):
    return render(request, 'task.html', {})


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        task = serializer.save(user=self.request.user)
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'task_group',
            {
                'type': 'send_notification',
                'notification': json.dumps({
                    'action': 'create',
                    'task': {
                        'id': task.id,
                        'title': task.title,
                        'description': task.description,
                        'completed': task.completed,
                    }
                })
            }
        )

    def get_queryset(self):
        user = self.request.user
        if isinstance(user, AnonymousUser):
            return Task.objects.none()
        return Task.objects.filter(user=user)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [permissions.AllowAny]
        return super().get_permissions()


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
