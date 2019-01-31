from django.core.management.base import BaseCommand
from top_articles import cron_articles
from top_articles.models import Story, Category
from django.db.utils import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
import logging
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Runs the cron script to update the articles"

    def article_update(self, url, category_type):
        top_articles, articlesId_list, newarticlesID_list = cron_articles.main(
            url)
        articleID_map = dict(zip(newarticlesID_list, top_articles))
        Story.objects.exclude(id__in=articlesId_list).delete()
        for index, id in enumerate(articlesId_list):
            print(index, id, category_type)
            if id in articleID_map:
                article = articleID_map[id]
                try:
                    if (category_type == "top"):
                        story = Story(
                            id=article['id'],
                            title=article['title'],
                            author=article['by'],
                            score=article['score'],
                            top_order_no=index,
                            timestamp=article['time'],
                            link=article['url']
                        )
                        story.save()
                        category, created = Category.objects.get_or_create(
                            category='top'
                        )
                        category.story.add(story)
                    elif (category_type == "new"):
                        story = Story(
                            id=article['id'],
                            title=article['title'],
                            author=article['by'],
                            score=article['score'],
                            new_order_no=index,
                            timestamp=article['time'],
                            link=article['url']
                        )
                        story.save()
                        category, created = Category.objects.get_or_create(
                            category='new'
                        )
                        category.story.add(story)

                except IntegrityError:
                    if (category_type == "top"):
                        story = Story.objects.get(top_order_no=index)
                        story.top_order_no = None
                        story.save()
                        story = Story(
                            id=article['id'],
                            title=article['title'],
                            author=article['by'],
                            score=article['score'],
                            top_order_no=index,
                            timestamp=article['time'],
                            link=article['url']
                        )
                        story.save()
                        category, created = Category.objects.get_or_create(
                            category='top'
                        )
                        category.story.add(story)
                    elif (category_type == 'new'):
                        story = Story.objects.get(new_order_no=index)
                        story.new_order_no = None
                        story.save()
                        story = Story(
                            id=article['id'],
                            title=article['title'],
                            author=article['by'],
                            score=article['score'],
                            new_order_no=index,
                            timestamp=article['time'],
                            link=article['url']
                        )
                        story.save()
                        category, created = Category.objects.get_or_create(
                            category='new'
                        )
                        category.story.add(story)

                    logger.error("Intergrity error for id:{0}".format(id))
                except KeyError:
                    logger.error("Key error for id:{0}".format(id))
                except Exception as error:
                    logger.error(error)
            else:
                try:
                    story = Story.objects.get(id=id)
                    if (category_type == "top"):
                        story.top_order_no = index
                    elif (category_type == "new"):
                        story.new_order_no = index
                    story.save()
                except ObjectDoesNotExist:
                    logger.error("Story not found for id:{0}".format(id))
                except IntegrityError:
                    if (category_type == "top"):
                        story = Story.objects.get(top_order_no=index)
                        story.top_order_no = None
                        story.save()
                    elif (category_type == "new"):
                        story = Story.objects.get(new_order_no=index)
                        story.new_order_no = None
                        story.save()
                    story = Story.objects.get(id=id)
                    if (category_type == "top"):
                        story.top_order_no = index
                    elif (category_type == "new"):
                        story.new_order_no = index
                    story.save()
                except Exception as error:
                    logger.error(error)

    def handle(self, *args, **kwargs):
        self.article_update(
            'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty',
            'top'
        )
        self.article_update(
            'https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty',
            'new'
        )