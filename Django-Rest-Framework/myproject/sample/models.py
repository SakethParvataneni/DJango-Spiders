from django.db import models

class URL(models.Model):
    url = models.URLField()
    spider_name = models.CharField(max_length=100)
    priority = models.IntegerField()
    scrape_result = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
