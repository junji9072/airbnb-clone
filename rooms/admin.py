from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """ Item Admin Definition """

    # 귀찮아도 주석 꼭 써줘야 협업시 편합니다.
    pass


"""
항목들 마다 각자 클래스를 만들어 줄 수 도 있습니다.
@admin.register(models.Facility)
class ItemAdmin(admin.ModelAdmin):
    pass
"""


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """ Room Admin Definition """

    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ """

    pass
