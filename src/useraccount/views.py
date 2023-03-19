from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from useraccount.forms import UserSignupForm, UserProfileForm, UserEditForm
from useraccount.models import Profile, User
from django.http import HttpResponseRedirect


# Create your views here.
User = get_user_model()


class UserLoginView(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True


class SignupView(CreateView):
    model = User
    form_class = UserSignupForm
    template_name = "register.html"
    success_url = reverse_lazy("posts:posthome")


@login_required
def user_profile(request, user, id):
    user = get_object_or_404(User, username=user, id=id)
    print(user)

    profile = get_object_or_404(Profile, user=user)
    print(profile.profile_picture)

    return render(
        request,
        "profile.html",
        {"users": user, "profile": profile},
    )


@login_required
def user_profile_edit(request, id):
    user = get_object_or_404(User, id=id, username=request.user)
    print(user)
    user_profiles = get_object_or_404(Profile, user__id=id)
    print(user_profile)
    # user_profile = Profile.objects.filter(id=id)
    # user = User.objects.filter(id=id)
    # print("LEngth", user[0].user.username)
    # for i in user:
    #     print("asdasdasd", i.about)
    # print("user rohsan", user[0])

    # # try:
    # #     Posts.objects.get(id=postid)
    # # except Posts.DoesNotExist:
    # #     raise Http404()  import HTTp404 first

    form = UserProfileForm(
        request.POST or None, request.FILES or None, instance=user_profiles
    )
    userss = UserEditForm(request.POST or None, request.FILES or None, instance=user)
    if form.is_valid() and userss.is_valid():
        userss.save()
        form.save()
        return HttpResponseRedirect(
            reverse(
                "user:userprofile",
                args=(
                    user.username,
                    user.id,
                ),
            )
        )

    return render(request, "profile_edit.html", {"form": form, "user": userss})
