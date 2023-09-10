from django.db import models
from common.models import CommonModel

# Create your models here.


class Calender(CommonModel):
    today_complete = models.BooleanField()  # 해당 운동을 오늘 했는가
    workouts = models.ManyToManyField(
        "workouts.WorkOut",
        related_name="calenders",
    )

    def __str__(self):
        return f"{(self.created_at)}"
