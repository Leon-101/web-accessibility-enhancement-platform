import json

from django import forms
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from app01.models import *
from app01.utils.encrypt import md5


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)


class RegisterModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', "password", "email"]

    # def clean_username(self):
    #     username = self.cleaned_data.get("username")
    #     if len(username) < 2:
    #         self.add_error("username","用户名不够长")
    #     return username

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)


@csrf_exempt
def login(request):
    if request.method == "GET":
        # print(settings.BASE_DIR)
        # print(settings.STATIC_URL)
        # print(settings.STATICFILES_DIRS)
        return HttpResponse("o")
    form = LoginForm(data=json.loads(request.body))
    if form.is_valid():
        obj = User.objects.filter(**form.cleaned_data).first()
        if not obj:
            return JsonResponse({"msg": "用户名或密码错误"}, status=400)
        request.session["info"] = {"username": form.cleaned_data["username"]}
        return JsonResponse({"msg": "登录成功"}, status=200)
    else:
        return JsonResponse({"msg": "用户名或密码为空"}, status=400)


@csrf_exempt
def register(request):
    form = RegisterModelForm(data=json.loads(request.body))
    if form.is_valid():
        form.save()
        request.session["info"] = {"username": form.cleaned_data.get("username")}
        return JsonResponse({"username": form.cleaned_data.get("username"), "msg": "注册成功"}, status=200)
    return JsonResponse({"errors": form.errors}, status=400)
