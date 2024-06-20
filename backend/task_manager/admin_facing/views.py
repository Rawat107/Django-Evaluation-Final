from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.contrib.auth.models import User
from user_facing.models import Task
from .models import App
from .serializers import AppSerializer
from .permissions import IsAdminUser
# Create your views here.

class AppViewSet(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


    def perform_create(self, serializer):
        app = serializer.save()
        users = User.objects.all()
        for user in users:
            Task.objects.create(user=user, app=app, status='pending')