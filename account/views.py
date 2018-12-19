from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from .forms import LoginForm,RegistrationForm,UserProfileForm,UserInfoForm,UserForm
from django.contrib.auth.decorators import login_required
from .models import UserInfo,UerProfile
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect


@login_required(login_url='/account/login/')

# Create your views here.
def user_login(request):
    if request.method=="POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd["username"],password=cd["password"])
            if user:
                login(request,user)
                return HttpResponse("授权通过，登录成功！欢迎光临")
            else:
                return HttpResponse("账号或密码错误，登录失败")
        else:
            return HttpResponse("Invalid login")
    if request.method=="GET":
        login_form=LoginForm();
        return render(request,"account/login.html",{"form":login_form})

#注册账号
def register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        userinfo_form = UserInfoForm(request.POST)
        if user_form.is_valid() * userprofile_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            new_profile = userprofile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()
            new_userinfo = userinfo_form.save(commit=False)
            new_userinfo.user=new_user
            new_userinfo.save()
            return HttpResponse("注册成功")
        else:
            return HttpResponse("注册失败")
    else:
        user_form = RegistrationForm()
        userprofile_form = UserProfileForm()
        return render(request, "account/register.html", {"form": user_form, "profile": userprofile_form})
#个人信息显示
def myself(request):
    user = User.objects.get(username=request.user.username)
    userprofile = UerProfile.objects.get(user=user)
    userinfo = UserInfo.objects.get(user=user)
    return render(request,"account/myself.html",{"user":user,"userinf":userinfo,"userprofile":userprofile})

#个人信息编辑
def myself_edit(request):
    user=User.objects.get(username=request.user.username)
    userprofile = UerProfile.objects.get(user=request.user)
    userinfo = UserInfo.objects.get(user=request.user)
    if request.method=="POST":
        
    else:





