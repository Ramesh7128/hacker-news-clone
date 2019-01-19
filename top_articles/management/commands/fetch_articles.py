from django.core.management.base import BaseCommand
from top_articles import cron_articles
from top_articles.models import Story
from django.db.utils import IntegrityError
import logging

class Command(BaseCommand):
    help = "Runs the cron script to update the articles"

    def handle(self, *args, **kwargs):
        top_articles = cron_articles.main()
        for idx, article in enumerate(top_articles):
            try:
                Story.objects.create(
                    id=article['id'],
                    title=article['title'],
                    author=article['by'],
                    score=article['score'],
                    order_no=idx,
                    timestamp=article['time'],
                    link=article['url']
                )
            except IntegrityError:
                story = Story.objects.get(id=article['id'])
                story.order_no = idx
                story.save()
            except Exception as error:
                logger.info(error)
                

            