
from django.shortcuts import render, get_object_or_404

from .models import Blog

def all_blogs(request):
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog_app/all_blogs.html', {'blogs':blogs})


def detail(request, id):
    blog = get_object_or_404(Blog, pk=id)
    return render(request, 'blog_app/details.html',{'blog':blog})