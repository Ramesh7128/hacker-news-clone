from django.db import models
from .sentiment import calculate_sentiment

# Create your models here.
class Story(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    title = models.TextField(blank=False, null=False)
    author = models.CharField(max_length=255)
    score = models.IntegerField(default=0)
    link = models.URLField()
    timestamp = models.IntegerField()
    order_no = models.IntegerField(blank=True)
    sentiment_score = models.FloatField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    # def calculate_sentiment(self, title):
    #     return 0

    def save(self, *args, **kwargs):
        print("function called")
        self.sentiment_score = calculate_sentiment(self.title)
        super(Story, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = "stories"

    

    
    

