from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Post
from .forms import PostForm


def home(request):
    search_query = request.GET.get('q', '').strip()
    selected_tag = request.GET.get('tag', '').strip()
    selected_sort = request.GET.get('sort', 'newest').strip()

    if selected_sort == 'oldest':
        sort_order = 'created_at'
    elif selected_sort == 'title':
        sort_order = 'title'
    else:
        sort_order = '-created_at'
        selected_sort = 'newest'

    posts = Post.objects.order_by(sort_order)

    if search_query:
        posts = posts.filter(
            Q(title__icontains=search_query)
            | Q(author__icontains=search_query)
            | Q(tag__icontains=search_query)
            | Q(content__icontains=search_query)
        )

    if selected_tag:
        posts = posts.filter(
            tag=selected_tag
        )

    tags = (
        Post.objects
        .values_list('tag', flat=True)
        .distinct()
        .order_by('tag')
    )

    show_latest_three = (
        not search_query
        and not selected_tag
        and selected_sort == 'newest'
    )

    if show_latest_three:
        posts = posts[:3]

    return render(
        request,
        "blog/home.html",
        {
            "posts": posts,
            "search_query": search_query,
            "selected_tag": selected_tag,
            "tags": tags,
            "selected_sort": selected_sort,
            "show_latest_three": show_latest_three,
        }
    )


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()

    return render(
        request,
        "blog/create.html",
        {"form": form}
    )


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    return render(
        request,
        "blog/detail.html",
        {"post": post}
    )


def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=post.id)

    else:
        form = PostForm(instance=post)

    return render(
        request,
        "blog/edit.html",
        {
            "form": form,
            "post": post,
        }
    )


def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        post.delete()
        return redirect('home')

    return render(
        request,
        "blog/delete.html",
        {
            "post": post,
        }
    )
