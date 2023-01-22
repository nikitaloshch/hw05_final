from django.core.paginator import Paginator

MAX_POSTS = 10


def paginator_posts(request, posts):
    paginator = Paginator(posts, MAX_POSTS)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)
