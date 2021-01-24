from django.shortcuts import render
from .models import SearchQuery
from blog.models import BlogPost


def search_view(request):
    query = request.GET.get("get-some", None)
    user = None
    if request.user.is_authenticated:
        user = request.user
    context = {"query": query}
    if query is not None:
        # creates object in the db for future use
        SearchQuery.objects.create(user=user, query=query)
        # creates object to pass to view for use
        blog_list = BlogPost.objects.search(query=query)
        context["blog_list"] = blog_list
    return render(request, "searching/view.html", context)
