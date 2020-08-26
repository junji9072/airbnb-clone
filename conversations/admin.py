from django.contrib import admin
from . import models


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):

    """ Message Admin Definition """

    list_display = ("__str__", "created")  # 메시지의 시간체크를 위해 적습니다.


@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):

    """ Conversation Admin Definition """

    list_display = ("__str__", "count_messages", "count_participants")
