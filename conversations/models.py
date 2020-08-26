from django.db import models
from core import models as core_models


class Conversation(core_models.TimeStampedModel):

    """ Conversation Model Definition """

    participants = models.ManyToManyField(
        "users.User", related_name="converstation", blank=True
    )

    def __str__(self):
        # return str(self.created)str로 만들어 주지 않으면 non-string returned 에러가 발생합니다.
        usernames = []
        for user in self.participants.all():  # 대화 참여자의 모든 유저네임 닉네임을 쿼리셋으로 불러옵니다.
            usernames.append(user.username)
        return ", ".join(
            usernames
        )  # str메소드는 배열하고 작동하지 않아서 [] 출력하므로 파이썬의 join메소드를 사용해서 string을 생성해서 리턴해줍니다.

    def count_messages(
        self,
    ):  # 이 함수는 메시지를 가지지 않지만 메세지 클래스는 FK로 related name =  messages로 가지고 있습니다.
        return self.messages.count()

    count_messages.short_description = "Number of Messages"

    def count_participants(self):
        return self.participants.count()

    count_participants.short_description = "Number of Participants"


class Message(core_models.TimeStampedModel):

    """ Message Model Definition """

    message = models.TextField()
    user = models.ForeignKey(
        "users.User", related_name="messages", on_delete=models.CASCADE
    )
    conversation = models.ForeignKey(
        "Conversation", related_name="messages", on_delete=models.CASCADE
    )

    # 유저가 메세지를 만들고 유저를 삭제하면 연결된 conversation도 삭제됩니다. 또한 conversation을 없애면 메시지도 없어집니다.
    def __str__(self):
        return f"{self.user} says: {self.message}"
