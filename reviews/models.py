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
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE
    )  # 유저는 리뷰를 쓰는 사람이며 1명이여야 하므로 FK를 써줍니다.
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    """
    def __str__(self):
        return self.room.country 
        FK에 접근 가능하게 해서 room과 연결된 
        모델의 값을 가져오게 해줍니다. 장고에서는 쿼리문 쓰지 않아도
        알아서 가져와줍니다. 이게 장고 relationship 장점입니다.
        
    """

    def __str__(self):
        return f"{self.review} - {self.room}"  # 파이썬 포맷팅을 통해서 리뷰와 이름을 보여줍니다.
