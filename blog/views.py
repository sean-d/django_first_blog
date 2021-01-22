from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from .models import BlogPost
from .forms import BlogPostModelForm


def blog_post_list_view(request):
    qs = BlogPost.objects.all()
    template_name = "blog/list.html"
    context = {"object_list": qs}
    return render(request, template_name, context)


def blog_post_detail_view(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/detail.html'
    context = {"post": post}
    return render(request, template_name, context)

# it's a good idea not to let randos post things, update things, or delete things.
# @staff_member_required to the rescne.


@staff_member_required
def blog_post_create_view(request):
    form = BlogPostModelForm(request.POST or None)
    if form.is_valid():
        # authed user is author.
        form.user = request.user
        form.save()
        form = BlogPostModelForm()
    template_name = "blog/form.html"
    context = {"title": "Create new blog post", "form": form}
    return render(request, template_name, context)


@staff_member_required
def blog_post_update_view(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    form = BlogPostModelForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
    template_name = 'blog/form.html'
    context = {"title": "Update {}".format(post.title), "form": form}
    return render(request, template_name, context)


@staff_member_required
def blog_post_delete_view(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/delete.html'
    context = {"post": post}
    if request.method == "POST":
        post.delete()
    return render(request, template_name, context)
