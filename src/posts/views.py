from django.shortcuts import render, get_object_or_404
from posts.models import Posts
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from posts.forms import PostsForm
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse


# Create your views here.
@login_required
def post_list(request):
    posts = Posts.objects.all().order_by("-id")
    return render(request, "list_posts.html", {"post": posts})


@login_required
def post_add_view(request):
    form = PostsForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        rep = form.save(commit=False)
        rep.created_by = request.user
        rep.save()
        return HttpResponseRedirect(reverse("posts:postslist"))
    return render(
        request, "add_post.html", {"form": form}
    )  # the dictionary key is passed in form in html file


@login_required
def post_edit_view(request, postid):
    post = get_object_or_404(Posts, id=postid)
    # try:
    #     Posts.objects.get(id=postid)
    # except Posts.DoesNotExist:
    #     raise Http404()  import HTTp404 first
    form = PostsForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("posts:posts"))

    return render(request, "add_post.html", {"form": form})


@login_required
def post_delete_view(request):
    postid = request.POST.get("postsid")
    posts = get_object_or_404(Posts, id=postid)
    posts.delete()
    return HttpResponseRedirect(reverse("posts:postslist"))


@login_required
def post_home(request):
    posts = Posts.objects.all().order_by("-id")

    paginator = Paginator(posts, per_page=4)
    page_number = request.GET.get("page")
    try:
        page_obj = paginator.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = paginator.page(paginator.num_pages)
    return render(request, "allpost.html", {"form": page_obj})


@login_required
def post_detail_view(request, postid):
    post = get_object_or_404(Posts, id=postid)
    return render(request, "post_detail.html", {"form": post})
