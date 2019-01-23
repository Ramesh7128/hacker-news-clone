import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Story
from ..serializers import StorySerializer

client = Client()

class GetAllStoriesTest(TestCase):
    """ Test module for GET all stories API """

    def setUp(self):
        Story.objects.create(
            id="32323",
            title='New Article1',
            author='ramesh',
            order_no=1,
            score=23,
            link="http://link.com",
            timestamp=2121313
        )
        Story.objects.create(
            id="32324",
            title='New Article2',
            author='ramesh',
            order_no=2,
            score=23,
            link="http://link1.com",
            timestamp=2121313
        )
        Story.objects.create(
            id="32325",
            title='New Article3',
            author='ramesh',
            order_no=3,
            score=23,
            link="http://link2.com",
            timestamp=2121313
        )

    def test_get_all_stories(self):
        # get API response
        response = client.get(reverse('get_all_stories'))
        # get data from db
        stories = Story.objects.all()
        serializer = StorySerializer(stories, many=True)
        self.assertEqual(response.data['data'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
