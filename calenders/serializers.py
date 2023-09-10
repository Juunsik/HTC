from rest_framework import serializers
from .models import Calender
from workouts.serializers import WorkOutSerializer


class CalenderSerializer(serializers.ModelSerializer):
    workouts = WorkOutSerializer(
        many=True,
    )

    class Meta:
        model = Calender
        fields = "__all__"
