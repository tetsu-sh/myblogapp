from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 100)
    published = models.DateTimeField()
    image = models.ImageField(upload_to = "media/")
    body = MarkdownxField('本文',help_text='Markdown形式で描いてください。')

    def body_to_markdown(self):
        return markdownify(self.body)

    def __str__(self):
        return self.title

    def summary(self):
        return markdownify(self.body[:30])
