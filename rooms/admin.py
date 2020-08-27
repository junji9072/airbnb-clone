from django.contrib import admin
from django.utils.html import mark_safe
from . import models

# Register your models here.


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """ Item Admin Definition """

    # 귀찮아도 주석 꼭 써줘야 협업시 편합니다.
    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()

    pass


"""
항목들 마다 각자 클래스를 만들어 줄 수 도 있습니다.
@admin.register(models.Facility)
class ItemAdmin(admin.ModelAdmin):
    pass
"""

# 장고가 자동적으로 FK로 relationship name과 class name이 room이기 때문에 장고가 자동으로 알고 FK를 가지고 있는 이미지를 넣습니다.
class PhotoInline(
    admin.TabularInline
):  # TabularInline 대신에 StackedInline을 쓸수도 있는데 한줄씩 나옵니다.

    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """ Room Admin Definition """

    inlines = (PhotoInline,)

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "city", "address", "price")},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths")}),
        (
            "More About the Space",
            # "classes": ("collapse",),  # 접고 펼수 있는 기능을 해줍니다. 많은 내용을 담고 있을 시 유용합니다.
            # "fields": ("amenities", "facilities", "house_rules"),
            {"fields": ("amenities", "facilities", "house_rules")},
        ),
        ("Last Details", {"fields": ("host",)}),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
    )

    # ordering = ('name','price','bedrooms') 이름이나 가격 룸 개수를 중심으로 리스트 순서를 정렬해줍니다.

    list_filter = (
        "instant_book",
        "host__superhost",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country",  # 양이 많으므로 항상 밑에 존재해야합니다.
        # "host__superhost",
        # "host__gender",장고 relationship으로 FK로 사용이 가능합니다.
    )
    """
    필터를 통해 나라별 도시별 예약별로 관리자 페이지에서 볼 수 있습니다.
    list_filter = ("instant_book", "city", "country")
    """

    """
    "city"도시의 seo 까지만 써도 검색이 가능한데, icontains라는게 기본으로 되어 있기 때문입니다. insensitive를 포함하며
    이 말은 대/소문자를 구분하지 않습니다. 정확한 검색을 위해서 = 옵션을 주도록 하겠습니다. host FK로 __로 and 조건을 걸어서 도시로
    검색이 안될 시 호스트 유저네임으로 검색 가능하도록 했습니다. 또한 ^로 startswith 옵션을 줘서 해당 열의 값이 지정한 문자열을 포함하도록 했습니다.
    """

    raw_id_fields = ("host",)  # 많은 유저를 가지게 되면 관리를 위해서 작은 버전의 user admin으로 볼 수 있도록 합니다.

    search_fields = ("=city", "^host__username")

    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )  # 이 필터는 N:N 관계에서만 작동합니다.

    def count_amenities(self, obj):  # self는 RoomAdmin 클래스이고 obj는 행을 뜻합니다.
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_description = "Photo Count"

    # count_amenities.short_description = 'hi'로 설명란을 바꿔줄 수 있습니다. functionality이므로 다른 것과 다르게 클릭 불가합니다. 장고가 함수란건 알기 때문입니다!


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Phot Admin Definition """

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(
        self, obj
    ):  # 안전한 파일이라는 것이라고 장고에게 mark_safe로 알려주고 썸네일을 불러올수 있도록 합니다.
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"
