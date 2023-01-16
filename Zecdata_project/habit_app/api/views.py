from rest_framework import viewsets
from habit_app.models import HabitModel
from .serializer import HabitSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated


class HabitApi(viewsets.ModelViewSet):
    queryset = HabitModel.objects.all()
    serializer_class = HabitSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]