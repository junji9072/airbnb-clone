from django.db import models

# 여기서 만들어진 이 모델은 user빼고 사용됩니다. 유저 모델은 이미 로긴 로그아웃등 기능을 가지고 있기 때문입니다.
class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    # 중복 사용을 방지하기 위해서 core라는 app에서 따로 관리를 해줍니다.
    created = models.DateTimeField(auto_now_add=True)  # 새 모델 생성 시 현재 날짜와 시간을 넣어줍니다.
    updated = models.DateTimeField(auto_now=True)  # 변경 시 새로운 날짜를 넣어줍니다.

    class Meta:
        # 이 옵션을 통해 이 모델이 DB로 가는 것을 막아줍니다.
        abstract = True
