from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Blog, Author
from blog.forms import BlogForm


def all_blogs(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'blogs.html', context)


# def create_blog(request):
#     form = BlogForm()
#     if request.method == 'POST':
#         print(request.POST)
#         title = request.POST.get('title')
#         desc = request.POST['description']
#         author = Author.objects.get(id=request.POST.get('author'))
#         form = BlogForm(request.POST)
#         if form.is_valid():
#             Blog.objects.create(title=title, description=desc, author=author)
#             return redirect('blogs')
#     return render(request, "create.html", locals())

def create_blog(request):
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs')
    return render(request, "create.html", locals())


def detail_blog(request, pk):
    blog = Blog.objects.get(id=pk)
    return render(request, "detail.html", locals())


def edit_blog(request, pk):
    edit_blog = get_object_or_404(Blog, pk=pk)
    form = BlogForm(instance=edit_blog)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=edit_blog)
        if form.is_valid():
            form.save()
            return redirect('blogs')
    return render(request, "edit.html", locals())


def delete_blog(request, pk):
    edit_blog = get_object_or_404(Blog, pk=pk)
    edit_blog.delete()
    return redirect("blogs")





