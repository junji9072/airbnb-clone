from django.db import models  # 장고와 관련된 패키지를 import 합니다.
from django.urls import reverse
from django_countries.fields import CountryField  # 외부 패키지를 import 합니다.
from core import models as core_models  # 내가 만들 패키지를 import 합니다.


class AbstractItem(
    core_models.TimeStampedModel
):  # roomtypes등등 여러가지 추상 아이템들을 위해 만들었습니다.
    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    # RoomType이라는 다른 이름 붙인 것은 DB에 다른 필드가 들어가도록 하게 만들었습니다.


class RoomType(AbstractItem):
    """ RoomType Object Definition """

    class Meta:
        verbose_name = "Room Type"  # 이름을 지정해 주지 않으면 자동으로 소문자로 변경됩니다.
        # ordering = ["created"] 오래된 항목이 상단에 위치하도록 정렬합니다.name으로 알파벳 순으로 정렬 가능합니다.


class Amenity(AbstractItem):

    """ Amenity Model Definition """

    class Meta:
        verbose_name_plural = "Amenities"  # 옵션을 주지 않으면 모델 이름을 그대로 씁니다.


class Facility(AbstractItem):

    """ Facility Model Definition """

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):

    """ HouseRule Model Definition """

    class Meta:
        verbose_name = "House Rule"


class Photo(core_models.TimeStampedModel):

    """ Photo Model Definition """

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="room_photos")
    room = models.ForeignKey(
        "Room", related_name="photos", on_delete=models.CASCADE
    )  # room을 삭제하면 사진도 삭제 되야 하므로 on_delete 옵션을 줍니다.

    def __str__(self):
        return self.caption


# Create your models here.
class Room(core_models.TimeStampedModel):

    """ Room Model Definition """

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()  # Decimal로 하면 소수점 첫째짜리 까지 표시되지만 필요없습니다.
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(
        "users.User", related_name="rooms", on_delete=models.CASCADE
    )  # 방은 오직 1명의 호스트만 존재합니다. on_delete 옵션은 1:N 관계를 가지는 FK만을 위한 것입니다.
    room_type = models.ForeignKey(
        "RoomType", related_name="rooms", on_delete=models.SET_NULL, null=True
    )
    amenities = models.ManyToManyField("Amenity", related_name="rooms", blank=True)
    facilities = models.ManyToManyField("Facility", related_name="rooms", blank=True)
    house_rules = models.ManyToManyField("HouseRule", related_name="rooms", blank=True)

    """장고에 있는 모든 class들이 가지고 있는 하나의 method가 바로 string method 입니다.
    파이썬이 class를 발견하면 class를 마치 string처럼 보여주며 이 method를 파이썬에서 __str__로 표시해줍니다.
    모든 파이썬 class는 str을 가지고 있습니다. 어떤 방인지 알기 위해 여기서 str을 사용합니다. """

    def __str__(self):
        return self.name

    # save를 overide 해서 self를 통해 self.city에 새로 바뀌는 내용이 오고 다시 바꿔서 저장을 합니다.
    def save(self, *args, **kwargs):  # args(arguments) kwargs(keyword arguments)
        self.city = str.capitalize(self.city)  # 첫글자가 대문자로 바뀌도록 했습니다.
        super().save(*args, **kwargs)  # 어드민 뿐만 아니라 모든 곳에서 모델을 수정생성시에도 적용 됩니다.

    def get_absolute_url(self):
        return reverse("rooms:detail", kwargs={"pk": self.pk})

    def total_rating(self):  # room이 reviews를 가지고 있습니다.
        all_reviews = self.reviews.all()
        all_ratings = 0
        # for review in all_reviews:
        #    all_ratings += review.rating_average()
        # return all_ratings / len(all_reviews) 0으로 나눠지지 않는 에러가 나므로 수정합니다.
        if len(all_reviews) > 0:  # 이 조건을 넣어서 에러를 수정합니다.
            for review in all_reviews:
                all_ratings += review.rating_average()
            return round(all_ratings / len(all_reviews), 2)
        return 0

