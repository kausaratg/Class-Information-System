from django.shortcuts import render, redirect, HttpResponseRedirect
from post.forms import PostForm
from post.models import Post, Comment
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse



# Create your views here.

def postformview(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ("posts")
        return render (request, "posts/postform.html", context)
    else:
        form = PostForm
        context ={"form":form}
        return render(request, "posts/postform.html", context)


def posts(request):
    posts = Post.objects.all().order_by("-date_created")
    context = {"posts":posts}
    return render(request, "posts/posts.html", context)


def loginuser(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("posts")
        return redirect("loginuser")
    return render(request, "posts/loginuser.html")

def logout_user(request):
    logout(request)
    return redirect('index')

def postdetail(request, pk):
    postdetail = Post.objects.get(pk=pk)
    comments = postdetail.comments.all()
    total_comment = comments.count()
    if request.method == "POST":
        comment = request.POST['comment']
        newcomment = Comment.objects.create(comment=comment, post=postdetail)
        newcomment.save()
        return HttpResponseRedirect(reverse("postdetail", args=[postdetail.id]))
    context = {"postdetail":postdetail, "comments":comments, "total_comment":total_comment}
    return render(request, "posts/postdetail.html", context)

