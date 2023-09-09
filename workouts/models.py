from django.db import models
from common.models import CommonModel

# Create your models here.


class WorkOut(CommonModel):
    name = models.CharField(max_length=50)  # 운동 이름

    class WorkOutMethodChoices(models.TextChoices):  # 운동 방법
        BODY_WEIGHT = ("body_weight", "맨몸 운동")
        FREE_WEIGHT = ("free_weight", "프리웨이트")
        MACHINES = ("machines", "머신 운동")

    class ClassificationChoices(models.TextChoices):  # 분류
        BUST = ("bust", "상반신")
        LOWER_BODY = ("lower_body", "하반신")
        CHEST = ("chest", "가슴")
        BACK = ("back", "등")
        THIGH = ("thigh", "허벅지")
        SHOULDER = ("shoulder", "어깨")
        ARM = ("arm", "팔")
        CORE = ("core", "코어")
        CALF = ("calf", "종아리")

    workoutmethod = models.CharField(
        max_length=15,
        choices=WorkOutMethodChoices.choices,
        default=WorkOutMethodChoices.BODY_WEIGHT,
    )
    classification = models.CharField(
        max_length=15,
        choices=ClassificationChoices.choices,
        default=ClassificationChoices.BUST,
    )

    def __str__(self):
        return self.name
