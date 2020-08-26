from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):

    """ Review Admin Definition """

    list_display = (
        "__str__",
        "rating_average",
    )  # 모델에서 만든 점수 평균을 보여줍니다. __str__을 써주면 글이 없어지는것을 방지해줍니다.
