from django import forms
from . import models


class LoginForm(forms.Form):

    email = forms.EmailField()  # username과 email은 동일하도록 설정합니다.
    password = forms.CharField(widget=forms.PasswordInput)
    """
    존재하는 이메일인지 확인하려면 method 이름은 반드시 clean_이어야 합니다.
    clean method를 만들어주고 아무것도 return하지 않으면 그 field를 지우는게 결과물 입니다.
    """

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return (
                    self.cleaned_data
                )  # clean method를 사용한다면 무조건 cleaned_data를 return해줘야 합니다.
            else:
                # clean()을 사용하면 field에 직접 에러를 추가해야 합니다.
                self.add_error("password", forms.ValidationError("Password is wrong"))
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("User does not exist"))

