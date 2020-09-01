from django.views.generic import ListView, DetailView, View
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models, forms

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


""" def search(request):
    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)
    country = request.GET.get("country", "KR")
    room_type = int(request.GET.get("room_type", 0))
    price = int(request.GET.get("price", 0))
    guests = int(request.GET.get("guests", 0))
    bedrooms = int(request.GET.get("bedrooms", 0))
    beds = int(request.GET.get("beds", 0))
    baths = int(request.GET.get("baths", 0))
    instant = bool(request.GET.get("instant", False))
    superhost = bool(request.GET.get("superhost", False))
    s_amenities = request.GET.getlist("amenities")
    s_facilities = request.GET.getlist("facilities")

    form = {
        "city": city,
        "s_room_type": room_type,
        "s_country": country,
        "price": price,
        "guests": guests,
        "bedrooms": bedrooms,
        "beds": beds,
        "baths": baths,
        "s_amenities": s_amenities,
        "s_facilities": s_facilities,
        "instant": instant,
        "superhost": superhost,
    }

    room_types = models.RoomType.objects.all()
    amenities = models.Amenity.objects.all()
    facilities = models.Facility.objects.all()

    choices = {
        "countries": countries,
        "room_types": room_types,
        "amenities": amenities,
        "facilities": facilities,
    }

    filter_args = {}

    if city != "Anywhere":
        filter_args["city__startswith"] = city

    filter_args["country"] = country

    if room_type != 0:
        filter_args["room_type__pk"] = room_type

    if price != 0:
        filter_args["price__lte"] = price

    if guests != 0:
        filter_args["guests__gte"] = guests

    if bedrooms != 0:
        filter_args["bedrooms__gte"] = bedrooms

    if beds != 0:
        filter_args["beds__gte"] = beds

    if baths != 0:
        filter_args["baths__gte"] = baths

    if instant is True:
        filter_args["instant_book"] = True

    if superhost is True:
        filter_args["host__superhost"] = True

    if len(s_amenities) > 0:
        for s_amenity in s_amenities:
            filter_args["amenities__pk"] = int(s_amenity)

    if len(s_facilities) > 0:
        for s_facility in s_facilities:
            filter_args["facilities__pk"] = int(s_facility)

    rooms = models.Room.objects.filter(**filter_args)

    return render(request, "rooms/search.html", {**form, **choices, "rooms": rooms}) """


class SearchView(View):
    """ SearchView Definition """

    def get(self, request):

        country = request.GET.get("country")

        if country:
            # 어떠한 데이터를 가지고 확인하는 작업을 합니다.
            form = forms.SearchForm(request.GET)
            # 만약 문제가 없는 데이터라면 아래 코드 블럭을 실행합니다.
            if form.is_valid():
                # form안에서 cleaned_data 즉 정리된 데이터를 가지고 올 수 있습니다.
                city = form.cleaned_data.get("city")
                country = form.cleaned_data.get("country")
                room_type = form.cleaned_data.get("room_type")
                price = form.cleaned_data.get("price")
                guests = form.cleaned_data.get("guests")
                bedrooms = form.cleaned_data.get("bedrooms")
                beds = form.cleaned_data.get("beds")
                baths = form.cleaned_data.get("baths")
                instant_book = form.cleaned_data.get("instant_book")
                superhost = form.cleaned_data.get("superhost")
                amenities = form.cleaned_data.get("amenities")
                facilities = form.cleaned_data.get("facilities")

                filter_args = {}

                if city != "Anywhere":
                    filter_args["city__startswith"] = city

                filter_args["country"] = country

                if room_type is not None:
                    filter_args["room_type"] = room_type

                if price is not None:
                    filter_args["price__lte"] = price

                if guests is not None:
                    filter_args["guests__gte"] = guests

                if bedrooms is not None:
                    filter_args["bedrooms__gte"] = bedrooms

                if beds is not None:
                    filter_args["beds__gte"] = beds

                if baths is not None:
                    filter_args["baths__gte"] = baths

                if instant_book is True:
                    filter_args["instant_book"] = True

                if superhost is True:
                    filter_args["host__superhost"] = True

                for amenity in amenities:
                    filter_args["amenities"] = amenity

                for facility in facilities:
                    filter_args["facilities"] = facility

                qs = models.Room.objects.filter(**filter_args).order_by(
                    "-created"
                )  # paginator는 정렬되어 있어야 하므로 queryset을 정렬해줍니다.

                paginator = Paginator(qs, 10, orphans=5)

                page = request.GET.get("page", 1)

                rooms = paginator.get_page(page)

                return render(
                    request, "rooms/search.html", {"form": form, "rooms": rooms}
                )

        else:
            form = (
                forms.SearchForm()
            )  # 데이터를 확인하는 과정없이 빈 form을 가져올 시 쓰이는데, 첫 form을 가져와야 할 시 씁니다.
        return render(
            request, "rooms/search.html", {"form": form}
        )  # 사람들이 url로 장난칠 가능성이 있기에 render로 방지해 줍니다.

