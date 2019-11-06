from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    # image = ProcessedImageField(
    #     processors=[Thumbnail(200,300)],
    #     format='JPEG',
    #     options={
    #         'quality' : 90
    #     }, 
    #     upload_to = 'articles/image'
    # )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 객체 표시 형식 수정
    def __str__(self):
        return f'[{self.title}] {self.content}'