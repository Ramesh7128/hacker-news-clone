from django.core.management.base import BaseCommand
from top_articles import cron_articles
from top_articles.models import Story
from django.db.utils import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
import logging
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Runs the cron script to update the articles"

    def handle(self, *args, **kwargs):
        top_articles, articlesId_list, newarticlesID_list = cron_articles.main()
        articleID_map = dict(zip(newarticlesID_list, top_articles))
        Story.objects.exclude(id__in=articlesId_list).delete()
        for index, id in enumerate(articlesId_list):
            if id in articleID_map:
                article = articleID_map[id]
                try:
                    Story.objects.create(
                        id=article['id'],
                        title=article['title'],
                        author=article['by'],
                        score=article['score'],
                        order_no=index,
                        timestamp=article['time'],
                        link=article['url']
                    )
                except IntegrityError:
                    logger.error("Intergrity error for id:{0}".format(id))
                except KeyError:
                    logger.error("Key error for id:{0}".format(id))
            else:
                try:
                    story = Story.objects.get(id=id)
                    story.order_no = index
                    story.save()
                except ObjectDoesNotExist:
                    logger.error("Story not found for id:{0}".format(id))
                except IntegrityError:
                    story = Story.objects.get(order_no=index)
                    story.order_no = None
                    story.save()
                    story = Story.objects.get(id=id)
                    story.order_no = index
                    story.save()




                

            