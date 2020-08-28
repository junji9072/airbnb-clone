from django.views.generic import ListView, DetailView
from . import models

# 함수명은 반드시 urls 이름과 동일해야 합니다.
# def all_rooms(request):
# now = datetime.now()
# hungry = True
# return render(request, "all_rooms.html", context={"now": now, "hungry": hungry})
# all_rooms = models.Room.objects.all()[0:10] 제한과 오프셋으로 sql 쿼리셋 개수를 제한 할 수 있습니다.
# rooms/home은 함수와 이름이 동일할 필요는 없지만 템플릿 폴더안 이름과 반드시 동일해야합니다.
# context 이름은 변수와 동일할 필요는 없지만 templates에서는 변수명이 반드시 동일해야합니다.
# return render(request, "rooms/home.html", context={"potato": all_rooms})
# page = request.GET.get("page", 1)   int로 정수형으로 바꿔주지 않으면 url에서 넘어온 1이 문자열로 됩니다.
# page = int(page or 1)   빈페이지로 가면 존재하는 페이지 라며 에러가 발생하는데 int에 기본 값을 주어서 해결합니다.
# page_size = 10
# limit = page_size * page
# offset = limit - page_size   항상 limit에서 빼야 합니다.
# all_rooms = models.Room.objects.all()[offset:limit]
# page_count = ceil(models.Room.objects.count() / page_size)

# return render(
#    request,
#    "rooms/home.html",
#    {
#        "potato": all_rooms,
#        "page": page,
#        "page_count": page_count,
#        "page_range": range(1, page_count),
#    },
# )
# 장고에서는 paginator를 제공하기 때문에 간단하게 생성 할 수 있습니다.

# page = request.GET.get("page", 1)
# room_list = models.Room.objects.all()  # 쿼리셋을 생성만 할 뿐 호출 전 까지는 바로 불러오지 않습니다.
# paginator = Paginator(room_list, 10, orphans=5)
# try:
#    rooms = paginator.page(int(page))
#    return render(request, "rooms/home.html", {"page": rooms})
# except EmptyPage:  모든 에러에 대한 처리를 하고 싶다면 exception이라고 쓰면 되지만 권장하는 방법은 아닙니다.


class HomeView(ListView):

    # HomeView Definition

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"


# def room_detail(request, pk): function기반 view
# try:
#     room = models.Room.objects.get(pk=pk)
#     return render(request, "rooms/detail.html", {"room": room})
# except models.Room.DoesNotExist:
#     # return redirect(reverse("core:home"))
#     raise Http404()


class RoomDetail(DetailView):

    """ RoomDetail Definition """

    model = models.Room  # class 기반은 이렇게 간단하게만 적어도 작동이 되지만 이해하기 어렵다는 단점이 있습니다.
