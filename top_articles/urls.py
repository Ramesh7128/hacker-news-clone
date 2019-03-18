from django.conf.urls import url
from .views import (
    RegisterationAPIView,
    UserRetreiveUpdateView,
    UserArticleStarredViews,
    LoginAPIView,
    articles_search,
    TopStoriesList,
    new_stories_list
)

app_name = 'top_articles'

urlpatterns = [
    url(r'^articles_search/?$', articles_search),
    url(r'^topstories/?$', TopStoriesList.as_view()),
    url(r'^newstories/?$', new_stories_list, name='get_all_new_stories'),
    url(r'^users/?$', RegisterationAPIView.as_view()),
    url(r'^users/login/?$', LoginAPIView.as_view()),
    url(r'^user', UserRetreiveUpdateView.as_view()),
    url(r'^starred', UserArticleStarredViews.as_view()),
]


