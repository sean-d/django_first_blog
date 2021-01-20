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


def blog_post_create_view(request):
    form = BlogPostModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = BlogPostModelForm()
    context = {"title": "Create new blog post", "form": form}
    template_name = "blog/form.html"
    return render(request, template_name, context)


def blog_post_update_view(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/update.html'
    context = {"post": post, "form": None}
    return render(request, template_name, context)


def blog_post_delete_view(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/delete.html'
    context = {"post": post, "form": None}
    return render(request, template_name, context)
