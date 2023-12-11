from django.db import models
# Create your models here.
from datetime import datetime
class  Blackcoffer(models.Model):
    end_year=models.IntegerField(max_length=5,null=True,blank=True)
    intensity=models.IntegerField(max_length=5,null=True,blank=True)
    sector=models.CharField(max_length=100,null=True,blank=True)
    topic=models.CharField(max_length=100,null=True,blank=True)
    insight=models.TextField(null=True,blank=True)
    url=models.URLField(max_length=250,null=True,blank=True)
    region=models.CharField(max_length=100,null=True,blank=True)
    start_yaer=models.IntegerField(max_length=5,null=True,blank=True)
    impact=models.IntegerField(max_length=5,null=True,blank=True)
    added=models.CharField(max_length=42,null=True,blank=True)
    published=models.CharField(max_length=42,null=True,blank=True)
    country=models.CharField(max_length=100,null=True,blank=True)
    relevance=models.IntegerField(max_length=5,null=True,blank=True)
    pestle=models.CharField(max_length=100,null=True,blank=True)
    source=models.CharField(max_length=100,null=True,blank=True)
    title=models.TextField(null=True,blank=True)
    likelihood=models.IntegerField(max_length=5,null=True,blank=True)
    @property
    def added_datetim(self):
        if self.added:
            return datetime.strptime(self.added,"%B, %d %Y %H:%M:%S")
        return None
    @property
    def published_datetim(self):
        if self.published:
            return datetime.strptime(self.published,"%B, %d %Y %H:%M:%S")
        return None
    # def __str__(self):
    #     return self.title