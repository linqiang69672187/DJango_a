from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from .forms import LoginForm,RegistrationForm,UserProfileForm,UserInfoForm,UserForm
from django.contrib.auth.decorators import login_required
from .models import UserInfo,UerProfile
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.conf.urls import url



# Create your views here.
@login_required(login_url='/account/login/')
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
        user_form = UserForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        userinfo_form = UserInfoForm(request.POST)
        if userinfo_form.is_valid()*userprofile_form.is_valid()*userinfo_form.is_valid():
            use_cd=user_form.cleaned_data
            userprofile_cd=userprofile_form.cleaned_data
            userinfo_cd=userinfo_form.cleaned_data
            print(use_cd["email"])
            user.email = use_cd["email"]
            userprofile.birth = userprofile_cd["birth"]
            userprofile.phone = userprofile_cd["phone"]
            userinfo.school = userinfo_cd["school"]
            userinfo.company = userinfo_cd["company"]
            userinfo.profession = userinfo_cd["profession"]
            userinfo.address = userinfo_cd["address"]
            userinfo.aboutme = userinfo_cd["aboutme"]
            user.save()
            userprofile.save()
            userinfo.save()
            return  HttpResponseRedirect("/account/my_information/")
    else:
        user_form = UserForm(instance=request.user)
        userprofile_form = UserProfileForm(initial={"birth":userprofile.birth,"phone":userprofile.phone})
        userinfo_form = UserInfoForm(initial={"school":userinfo.school,"company":userinfo.company,"profession":userinfo.profession,"address":userinfo.address,"aboutme":userinfo.aboutme})
        return render(request,"account/myself_edit.html",{"user_form":user_form,"userprofile":userprofile_form,"userinf":userinfo_form})

@login_required(login_url='/account/login/')
def my_image(request):
    if request.method=="POST":
        img = request.POST["img"]
        userinfo = UserInfo.objects.get(user=request.user.id)
        userinfo.photo = img
        userinfo.save()
        return  HttpResponse(1)
    else:
        return render(request,'account/imagecrop.html')




