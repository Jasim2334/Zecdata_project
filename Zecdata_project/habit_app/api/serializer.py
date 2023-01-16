from habit_app.models import HabitModel
from rest_framework import serializers

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitModel
        fields = '__all__'
        