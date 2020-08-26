from django.db import models
from core import models as core_models

# Create your models here.
class Review(core_models.TimeStampedModel):
    """ Review Model Definition """

    review = models.TextField()
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    # 유저는 리뷰를 쓰는 사람이며 1명이여야 하므로 FK를 써줍니다.
    user = models.ForeignKey(
        "users.User", related_name="reviews", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", related_name="reviews", on_delete=models.CASCADE
    )

    """
    def __str__(self):
        return self.room.country 
        FK에 접근 가능하게 해서 room과 연결된 
        모델의 값을 가져오게 해줍니다. 장고에서는 쿼리문 쓰지 않아도
        알아서 가져와줍니다. 이게 장고 relationship 장점입니다.
        
    """

    def __str__(self):
        return f"{self.review} - {self.room}"  # 파이썬 포맷팅을 통해서 리뷰와 이름을 보여줍니다.

    def rating_average(self):  # 커스텀 함수를 모델에 적용해서 사이트 전체에 적용될 수 있도록 합니다.
        avg = (
            self.accuracy
            + self.communication
            + self.cleanliness
            + self.location
            + self.check_in
            + self.value
        ) / 6
        return round(avg, 2)  # 소수점 자리가 너무 많아서 round함수를 통해서 소수점 2자리 까지만 보여주도록 합니다.

    rating_average.short_description = "Avg."
