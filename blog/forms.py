from django import forms
from .models import BlogPost


class BlogPostForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)


class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ["title", "slug", "image", "content", "publish_date"]

    def clean_title(self, *args, **kwargs):
        # if blog post is new, instance is None. Otherwise, it's the title of the post as per __str__
        instance = self.instance
        title = self.cleaned_data.get("title")
        # iexact == case insensitive
        qs = BlogPost.objects.filter(title__iexact=title)
        if instance != None:
            # remove item being updated from queryset so the title can remain unchanged.
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise forms.ValidationError(
                "Title already exists. Please use another one.")
        return title
