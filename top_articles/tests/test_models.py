from django.test import TestCase
from ..models import Story


class PuppyTest(TestCase):
    """ Test module for Story model """

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

    def test_story(self):
        story = Story.objects.get(id='32323')
        self.assertEqual(
            story.author, "ramesh")