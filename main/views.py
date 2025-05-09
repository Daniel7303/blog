from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from . models import Post, Comment
from . import forms 
from django.contrib import messages
from django.db.models import Q 
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
# from .forms import CreateComment
from django.core.exceptions import PermissionDenied




# Create your views here.

name = "Django Challenger"


def hero(request):
    return render(request, 'main/hero.html')


def home(request):
    query = request.GET.get('query')
    
    # Filtered posts that are not drafts
    post_list = Post.objects.filter(is_draft=False).order_by('-created_at')
    
    paginator = Paginator(post_list, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if query:
        posts = post_list.filter(Q(title__icontains=query) | Q(content__icontains=query))
        messages.info(request, f"{posts.count()} result(s) found for '{query}'")
    else:
        posts = post_list

    return render(request, 'main/home.html', {
        'posts': posts,
        'page_obj': page_obj,
    })



def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.views += 1
    post.save(update_fields=['views'])
    comments = post.comments.all()
    if request.method == 'POST' and request.user.is_authenticated:
        commentform = forms.CreateComment(request.POST)
        if commentform.is_valid():
            comment = commentform.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('posts:detail', slug= slug)
    else:
        commentform = forms.CreateComment()

    return render(request, 'main/post_detail.html', {'post': post, 'form': commentform, 'comments': comments},)


@login_required
def create_post(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            
            post.save()
            messages.success(request, f'post created succesfully')
        return redirect('posts:home')
    else:
        form = forms.CreatePost()
    
    return render(request, 'main/form.html', {'form': form})


def edit_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user != post.author:
        raise PermissionDenied
        # return HttpResponseForbidden("You are not allowed to edit this post.")
    if request.method == 'POST':
        edit = forms.CreatePost(request.POST, request.FILES, instance=post)
        if edit.is_valid:
            edit.save()
            messages.info(request, 'Post updated successfully')
        
            return redirect('posts:home')
        
    else:
        edit = forms.CreatePost(instance=post)
    return render(request, 'main/edit_post.html', {'edit': edit, 'post': post})



def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user != post.author:
        return HttpResponseForbidden('You are not allowed to delete this post. ')
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, f'"{post.title}" was deleted successfully' )
        return redirect('posts:home')
    
    return render(request, 'main/confirm_delete.html', {'post': post})
        

def posts_by_category(request, category):
    filtered_posts = Post.objects.filter(category=category)
    categories = Post.objects.values_list('category', flat=True).distinct()
    # return redirect('posts.category')
    return render(request, 'main/category.html', {'posts': filtered_posts, 'categories': categories})

def like_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect("posts:detail", slug=slug)



@login_required
def draft_posts(request):
    drafts = Post.objects.filter(author=request.user, is_draft=True).order_by('-created_at')
    return render(request, 'main/user_dashboard.html', {'drafts': drafts})


def comment_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all()
    if request.method == 'POST' and request.user.is_authenticated:
        commentform = forms.CreateComment(request.POST)
        if commentform.is_valid():
            comment = commentform.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('posts:detail', slug= slug)
    else:
        commentform = forms.CreateComment()
    return render(request, 'main/post_detail.html', {'post': post, 'form': commentform, 'comments': comments})


