from django.db import models
from common.models import CommonModel

# Create your models here.


class Calender(CommonModel):
    today_complete = models.BooleanField(default=False)  # 해당 운동을 오늘 했는가
    workouts = models.ManyToManyField(
        "workouts.WorkOut",
        related_name="calenders",
    )
    users = models.ForeignKey(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="calenders",
    )

    def __str__(self):
        return f"{(self.created_at)}"
