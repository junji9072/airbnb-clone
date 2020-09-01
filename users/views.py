from django.views import View
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from . import forms

""" # Create your views here. class 기반으로 그냥 view를 만듭시다.
class LoginView(View):
    def get(self, request):
        form = forms.LoginForm(initial={"email": "itn@las.com"})
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("core:home"))
        return render(request, "users/login.html", {"form": form})
 """

# 로그인을 가장 쉽게 만드는 방법은 LoginView를 만드는 것입니다. 이 경우 위의 경우와 다르게 이메일이 아닌 유저이름을 씁니다. view가 필요할 시 호출합니다.
# 그래서 FormView는 form에서 인증하고 싶을 시 좋습니다.
class LoginView(FormView):
    template_name = "users/login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy(
        "core:home"
    )  # reverse는 자동으로 호출해주는데 lazy를 붙여주면 자동으로 호출하지 않습니다.
    # form이 유효한지 체크하고 super().form_valid 호출 시 success_url로 가서 다시 작동합니다.
    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


# 로그아웃 class 기반 view이고 request를 받습니다.
def log_out(request):
    logout(request)
    return redirect(reverse("core:home"))  # 로그인 되면 홈으로 보내줍니다.


""" def login_view(request): function 기반 view 입니다.
    if request.method == 'GET':
        pass
    elif request.method == 'P' """
