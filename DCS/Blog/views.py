from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required()
def PostDetailView(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']

            try:
                parent = form.cleaned_data['parent']
            except:
                parent = None

            new_comment = Comment(post=post, content=content, author=request.user, parent=parent)
            new_comment.save()

            return redirect('post_detail', pk)
    else:
        form = CommentForm()

    context = {
        "post": post,
        "comments": comments,
        "form": form
    }

    return render(request, 'blog/post_detail.html', context=context)
