from rest_framework import viewsets
from habit_app.models import HabitModel
from .serializer import HabitSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated


class HabitApi(viewsets.ReadOnlyModelViewSet):
    queryset = HabitModel.objects.all()
    serializer_class = HabitSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return HabitModel.objects.filter(user=user)