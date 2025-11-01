from django.shortcuts import render
from . import data
from typing import Any
from django.http import HttpRequest, Http404


def blog(request):
    print('blog')
    context = {
                'title': 'Blog',
                'posts': data.posts
            }
    return render(request,
                  'blog/index.html',
                  context
    )


def exemplo(request):
    print('exemplo')
    context = {
                'text': 'Estou no exemplo do blog',
                'title': 'Página de exemplo'
            }
    return render(
        request,
        'blog/exemplo.html',
        context
        )

def post(request: HttpRequest, post_id: int):
    found_post: dict[str, Any] | None = None

    for post in data.posts:
        if post['id'] == post_id:
            found_post = post
            break

    if found_post is None:
        raise Http404('Post não existe')

    context = {
                'title': found_post['title'] + ' - ',
                'post': found_post,
            }

    return render(request,
                  'blog/post.html',
                  context
    )
