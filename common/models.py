from django.db import models


# Create your models here.
class CommonModel(models.Model):
    """Common Model Definition"""

    created_at = models.DateField(
        auto_now_add=True,
    )
    updated_at = models.DateField(
        auto_now=True,
    )

    class Meta:
        abstract = True  # DB에는 Migration이 되지 않고 다른 모델에서 상속받아 사용할 수 있도록 설정
