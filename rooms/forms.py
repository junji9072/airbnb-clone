from django import forms
from django_countries.fields import CountryField
from . import models


class SearchForm(forms.Form):

    city = forms.CharField(initial="Anywhere")  # forms도 모델에 있는 것처럼 fields를 가지고 있습니다.
    country = CountryField(default="KR").formfield()  # 기본으로 KR로 설정했습니다.
    room_type = forms.ModelChoiceField(
        required=False, empty_label="Any kind", queryset=models.RoomType.objects.all()
    )  # --로 나오는게 싫으므로 ! 아무것도 선택 안될시 값을 넣어줬습니다.
    price = forms.IntegerField(required=False)
    guests = forms.IntegerField(required=False)
    bedrooms = forms.IntegerField(required=False)
    beds = forms.IntegerField(required=False)
    baths = forms.IntegerField(required=False)
    instant_book = forms.BooleanField(required=False)
    superhost = forms.BooleanField(required=False)
    amenities = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.Amenity.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )  # 기본 멀티 체크박스는 보기 지저분 하기 때문에 widget을 사용해서 보기 편하게 바꿔줍니다.
    facilities = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.Facility.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
