from django.db import models
import datetime
from django.utils import timezone

class newsStory(models.Model):
    heading = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date of publication')
    news_story_text = models.CharField(max_length=10000)

    def __str__(self):
        return self.heading
        return self.news_story_text

    def published_recent(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)