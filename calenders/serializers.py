from rest_framework import serializers
from .models import Calender
from workouts.serializers import WorkOutSerializer
from users.serializers import UserSimpleSerializer


class CalenderSerializer(serializers.ModelSerializer):
    workouts = WorkOutSerializer(
        many=True,
        read_only=True,
    )
    user = UserSimpleSerializer(
        read_only=True,
    )

    class Meta:
        model = Calender
        fields = "__all__"
