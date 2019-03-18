from social_django.utils import psa
from requests.exceptions import HTTPError
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from rest_framework import status
from .renderers import UserJSONRenderer

from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView
from .serializers import RegisterationSerializer, UserSerializer, LoginSerializer

from rest_framework import status
from django.http import JsonResponse

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from top_articles.models import Story
from top_articles.serializers import StorySerializer
from top_articles.search import StoryIndex
from top_articles.models import Story

# Create your views here.


class TopStoriesList(APIView):
    permission_classes = (AllowAny,)
    serializer_class = StorySerializer

    def get(self, request, *args, **kwargs):
        data = []
        nextPage = 1
        previousPage = 1
        story = Story.objects.filter(
            categories__category='top').order_by('top_order_no')
        print("length", len(story))
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


@api_view(['GET', ])
@permission_classes([AllowAny])
def new_stories_list(request):
    """
    List new stories.
    """
    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
        story = Story.objects.filter(
            categories__category='new').order_by('new_order_no')
        print("length", len(story))
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


@api_view(['GET', ])
@permission_classes([AllowAny])
def articles_search(request):
    """
    search stories from elastic search.
    """
    if request.method == 'GET':
        query = request.GET['q']
        print(query)
        ids = []
        if query:
            try:
                story = StoryIndex.search()
                print(query)
                story = story.query('match', title=query)
                story = story[:100]
                response = story.execute()
                response_dict = response['hits']['hits']
                print(len(response_dict))
                response_dict = [x['_source'] for x in response_dict]
                serializer = StorySerializer(
                    response_dict, context={'request': request}, many=True)
                return Response(
                    {
                        'data': serializer.data,
                    }
                )
            except Exception as error:
                print(error)


class SocialSerializer(serializers.Serializer):
    """
    Serializer which accepts an OAuth2 access token.
    """
    access_token = serializers.CharField(
        allow_blank=False,
        trim_whitespace=True,
    )


@api_view(http_method_names=['POST'])
@permission_classes([AllowAny])
@psa()
def exchange_token(request, backend):
    """
    Exchange an OAuth2 access token for one for this site.
    This simply defers the entire OAuth2 process to the front end.
    The front end becomes responsible for handling the entirety of the
    OAuth2 process; we just step in at the end and use the access token
    to populate some user identity.
    The URL at which this view lives must include a backend field, like:
        url(API_ROOT + r'social/(?P<backend>[^/]+)/$', exchange_token),
    Using that example, you could call this endpoint using i.e.
        POST API_ROOT + 'social/facebook/'
        POST API_ROOT + 'social/google-oauth2/'
    Note that those endpoint examples are verbatim according to the
    PSA backends which we configured in settings.py. If you wish to enable
    other social authentication backends, they'll get their own endpoints
    automatically according to PSA.
    ## Request format
    Requests must include the following field
    - `access_token`: The OAuth2 access token provided by the provider
    """
    serializer = SocialSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # set up non-field errors key
        # http://www.django-rest-framework.org/api-guide/exceptions/#exception-handling-in-rest-framework-views
        try:
            nfe = settings.NON_FIELD_ERRORS_KEY
        except AttributeError:
            nfe = 'non_field_errors'

        try:
            # this line, plus the psa decorator above, are all that's necessary to
            # get and populate a user object for any properly enabled/configured backend
            # which python-social-auth can handle.
            print('checkagain')
            user = request.backend.do_auth(
                serializer.validated_data['access_token'])
        except HTTPError as e:
            # An HTTPError bubbled up from the request to the social auth provider.
            # This happens, at least in Google's case, every time you send a malformed
            # or incorrect access key.
            return Response(
                {'errors': {
                    'token': 'Invalid token',
                    'detail': str(e),
                }},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if user:
            if user.is_active:
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key})
            else:
                # user is not active; at some point they deleted their account,
                # or were banned by a superuser. They can't just log in with their
                # normal credentials anymore, so they can't log in with social
                # credentials either.
                return Response(
                    {'errors': {nfe: 'This user account is inactive'}},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        else:
            # Unfortunately, PSA swallows any information the backend provider
            # generated as to why specifically the authentication failed;
            # this makes it tough to debug except by examining the server logs.
            return Response(
                {'errors': {nfe: "Authentication Failed"}},
                status=status.HTTP_400_BAD_REQUEST,
            )


class RegisterationAPIView(APIView):
    # Allow any user with/without authentication to hit this endpoint.
    permission_classes = (AllowAny,)
    serializer_class = RegisterationSerializer
    renderer_classes = (UserJSONRenderer,)

    def post(self, request):
        print(request.data)
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):

    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserRetreiveUpdateView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        """
        Returns the user in a json serializable manner.
        """
        serializer = self.serializer_class(request.user)
        print("this is method handling")
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        serializer_data = request.data.get('user', {})
        serializer = self.serializer_class(
            request.user, data=serializer_data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserArticleStarredViews(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        """
        returns all starred articles by the user.
        """
        user = request.user
        story = Story.objects.filter(starred_user=user)
        page = request.GET.get('page', 1)
        nextPage = 1
        previousPage = 1
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
                'nextlink': '/api/starred/?page=' + str(nextPage),
                'prevlink': '/api/starred/?page=' + str(previousPage)
            }
        )

    def post(self, request, *args, **kwargs):
        """
        Update the article starred.
        """
        article_id = request.data.get('articleID', '')
        if article_id:
            user = request.user
            if Story.objects.filter(starred_user=user, pk=article_id).exists():
                story = Story.objects.get(pk=article_id)
                story.starred_user.remove(user)
            else:
                story = Story.objects.get(pk=article_id)
                story.starred_user.add(user)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
