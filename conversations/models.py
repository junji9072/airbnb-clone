from django.db import models
from core import models as core_models


class Conversation(core_models.TimeStampedModel):

    """ Conversation Model Definition """

    participants = models.ManyToManyField("users.User", blank=True)

    def __str__(self):
        return str(self.created)  # str로 만들어 주지 않으면 non-string returned 에러가 발생합니다.


class Message(core_models.TimeStampedModel):

    """ Message Model Definition """

    message = models.TextField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    conversation = models.ForeignKey("Conversation", on_delete=models.CASCADE)
    # 유저가 메세지를 만들고 유저를 삭제하면 연결된 conversation도 삭제됩니다. 또한 conversation을 없애면 메시지도 없어집니다.
    def __str__(self):
        return f"{self.user} says: {self.text}"
