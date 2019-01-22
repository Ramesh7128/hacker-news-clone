from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import JsonResponse

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from top_articles.models import Story
from top_articles.serializers import StorySerializer, StoryIndexSerializer

# haystack imports
from drf_haystack.viewsets import HaystackViewSet
from haystack.query import SearchQuerySet


# Create your views here.
@api_view(['GET',])
def stories_list(request):
    """
    List  top stories.
    """
    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
        story = Story.objects.all().order_by('order_no')
        print([st.order_no for st in story])
        page = request.GET.get('page', 1)
        paginator = Paginator(story, 30)
        try:
            data = paginator.page(story)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()
        serializer = StorySerializer(
            data, context={'request': request}, many=True)
        return Response(
            {
                'data': serializer.data,
                'count': paginator.count,
                'numpages': paginator.num_pages,
                'nextlink': '/api/stories/?page=' + str(nextPage),
                'prevlink': '/api/stories/?page=' + str(previousPage)
            }
        )

def autocomplete(request):
    print(request.GET.get('query'))
    sqs = SearchQuerySet().autocomplete(
        content_auto=request.GET.get(
            'query',
            ''))[
        :5]
    s = []
    for result in sqs:
        d = {"value": result.title, "data": result.object.url}
        s.append(d)
    output = {'suggestions': s}
    return JsonResponse(output)

class StorySearchView(HaystackViewSet):
    index_models=[Story]
    serializer_class=StoryIndexSerializer
