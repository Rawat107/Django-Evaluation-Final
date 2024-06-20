from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import UserProfile, Task
from .serializers import UserProfileSerializer, TaskSerializer

# Create your views here.

class UserProfileCreateView(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [AllowAny]

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter tasks for the logged-in user
        return Task.objects.filter(user=self.request.user)

    @action(detail=False, methods=['post'])
    def complete_task(self, request):
        task_id = request.data.get('task_id')
        screenshot = request.data.get('screenshot')

        try:
            task = Task.objects.get(id=task_id, user=request.user)
            task.status = 'completed'
            task.screenshot = screenshot
            task.save()

            # Update user's total points
            user_profile = UserProfile.objects.get(user=request.user)
            user_profile.total_point += task.app.points
            user_profile.save()

            return Response(TaskSerializer(task).data, status=status.HTTP_200_OK)
        except Task.DoesNotExist:
            return Response({'error': 'Task not found or not assigned to user'}, status=status.HTTP_404_NOT_FOUND)
