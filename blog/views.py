from lib2to3.fixes.fix_input import context
from pydoc_data.topics import topics
from tempfile import template
from .models import Blog, Areas, Regions, Comment
from django.shortcuts import render, redirect, HttpResponse
from .forms import Formblog, UpdateBlogForm, FormArea, UpdateAreaForm, FormRegion, CreateCommentForm


# Create your views here.

def blog(request):
    blogs = Blog.objects.all()
    context = {
        "blogs": blogs
    }
    return render(request, 'blog.html', context)



def blog2(request):

    blogs2 = Blog.objects.all()
    context = {
        "blog2":blogs2
    }

    return render(request, 'blog_list.html', context)




def create_blog(request):
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        Blog.objects.create(

            title=title,
            body=body

        )
        return redirect('http://127.0.0.1:8000/blog/')


    form = Formblog()
    context = {
        'form':form

    }
    return render(request, 'form_blog.html', context)


def updateBlog(request, id):
    blog = Blog.objects.get(pk=id)

    if request.method == 'POST':
        form = UpdateBlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/blog/')

        return HttpResponse('error')

    form = UpdateBlogForm(instance=blog)
    context = {'form': form}
    return render(request, 'updateBlog.html', context)


def deleteBlog(request, id):
    blog = Blog.objects.get(pk=id)
    blog.delete()
    return redirect("http://127.0.0.1:8000/blog/")




def areaview(request):
    areas = Areas.objects.all()
    context = {

        'area':areas

    }

    return render(request, "Area.html", context)



def create_area(request):
    if request.method == 'POST':
        name = request.POST['name']
        about = request.POST['about']
        Areas.objects.create(

            name=name,
            about=about

        )
        return redirect('http://127.0.0.1:8000/blog/area/')


    form = FormArea()
    context = {
        'form':form
    }
    return render(request, 'form_blog.html', context)


def updateArea(request, id):
    area = Areas.objects.get(pk=id)

    if request.method == 'POST':
        form = UpdateAreaForm(request.POST, instance=area)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/blog/area/')

        return HttpResponse('error')

    form = UpdateAreaForm(instance=area)
    context = {'form': form}
    return render(request, 'updateArea.html', context)



def deleteArea(request, id):
    Area = Areas.objects.get(pk=id)
    Area.delete()
    return redirect("http://127.0.0.1:8000/blog/area/")


def RegionView(request):
    region = Regions.objects.all()
    context = {

        'regions':region

    }

    return render(request, 'Region.html', context)


def CreateRegion(request):
    if request.method == 'POST':
        user = request.POST['user']
        topic = request.POST['topic']

        Regions.objects.create(
            user=user,
            topic=topic
        )
        return redirect("http://127.0.0.1:8000/blog/regions/")

    form = FormRegion()
    context = {
        'form': form
    }
    return render(request, 'form_blog.html', context)

def commentView(request, id):
    if request.method == "POST":
        author = request.POST['author']
        text = request.POST['text']
        blog = Blog.objects.get(id=id)
        Comment.objects.create(
            blog=blog,
            author = author,
            text = text
        )
    blog = Blog.objects.get(id=id)
    comments = Comment.objects.filter(blog=blog)
    form = CreateCommentForm
    context = {
        'id': id,
        'form': form,
        'comments': comments

    }
    return render(request, "Comment.html", context)

def deleteComment(request, id):
    comment = Comment.objects.get(id=id)
    blog_id = comment.blog.id
    comment.delete()
    return redirect('comment_view', id=blog_id)




