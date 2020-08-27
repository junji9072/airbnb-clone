from django.shortcuts import render
from . import models

# 함수명은 반드시 urls 이름과 동일해야 합니다.
def all_rooms(request):
    # now = datetime.now()
    # hungry = True
    # return render(request, "all_rooms.html", context={"now": now, "hungry": hungry})
    all_rooms = models.Room.objects.all()
    # rooms/home은 함수와 이름이 동일할 필요는 없지만 템플릿 폴더안 이름과 반드시 동일해야합니다.
    # context 이름은 변수와 동일할 필요는 없지만 templates에서는 변수명이 반드시 동일해야합니다.
    return render(request, "rooms/home.html", context={"potato": all_rooms})

