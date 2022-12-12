from django.shortcuts import render, redirect
from post.forms import PostForm
from post.models import Post
from django.contrib.auth import authenticate, login


# Create your views here.

def postformview(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ("/")
        return render (request, "posts/postform.html", context)
    else:
        form = PostForm
        context ={"form":form}
        return render(request, "posts/postform.html", context)


def posts(request):
    posts = Post.objects.all().order_by("date_created")
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

def postdetail(request, id):
    postdetail = Post.objects.get(id=id)
    comment = postdetail.comment.all()
    total_comment = comment.count()
    context = {"postdetail":postdetail, "comment":comment, "total_comment":total_comment}
    return render(request, "posts/postdetail.html", context)


