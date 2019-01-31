from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import JsonResponse

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from top_articles.models import Story
from top_articles.serializers import StorySerializer

# Create your views here.
@api_view(['GET',])
def top_stories_list(request):
    """
    List top stories.
    """
    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
        story = Story.objects.filter(categories__category='top').order_by('top_order_no')
        print("length",len(story))
        page = request.GET.get('page', 1)
        print("page", page)
        paginator = Paginator(story, 20)
        startIndex = 0
        endIndex = 0
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()
        if data.start_index():
            start_index = data.start_index()
        if data.end_index():
            end_index = data.end_index()
        serializer = StorySerializer(
            data, context={'request': request}, many=True)
        return Response(
            {
                'data': serializer.data,
                'count': paginator.count,
                'numpages': paginator.num_pages,
                'startIndex': start_index,
                'endIndex': end_index,
                'nextlink': '/api/topstories/?page=' + str(nextPage),
                'prevlink': '/api/topstories/?page=' + str(previousPage)
            }
        )


@api_view(['GET',])
def new_stories_list(request):
    """
    List new stories.
    """
    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
        story = Story.objects.filter(categories__category='new').order_by('new_order_no')
        print("length",len(story))
        page = request.GET.get('page', 1)
        print("page", page)
        paginator = Paginator(story, 20)
        startIndex = 0
        endIndex = 0
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()
        if data.start_index():
            start_index = data.start_index()
        if data.end_index():
            end_index = data.end_index()
        serializer = StorySerializer(
            data, context={'request': request}, many=True)
        return Response(
            {
                'data': serializer.data,
                'count': paginator.count,
                'numpages': paginator.num_pages,
                'startIndex': start_index,
                'endIndex': end_index,
                'nextlink': '/api/newstories/?page=' + str(nextPage),
                'prevlink': '/api/newstories/?page=' + str(previousPage)
            }
        )

