from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# admin 패널에서 이 유저를 보고 싶고 이 유저를 컨트롤하는 클래스가 바로 이것이다라는 의미입니다.
@admin.register(models.User)
# admin.site.register(models.User, CustomUserAdmin) 동일한 기능을 합니다.
class CustomUserAdmin(UserAdmin):
    """ Custom User Admin """

    list_display = ("username", "email", "gender", "language", "currency", "superhost")
    list_filter = ("language", "currency", "superhost")
    # 리스트 필터링을 해서 보고 싶을 시에 하는 옵션입니다.
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
    list_filter = UserAdmin.list_filter + ("superhost",)

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
    )
