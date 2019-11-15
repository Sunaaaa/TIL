from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
from django.conf import settings

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

    poster = ProcessedImageField(
        processors=[Thumbnail(200,300)],    # 처리할 작업
        format='JPEG',              # 이미지 포맷
        options={                   # 각종 추가 옵션
            'quality' : 90
        },
        upload_to = 'movies/image' # 저장 위치
        # 실제 경로 : MEDIA_ROOT/movies/image
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} : {self.user}'

class Rating(models.Model):
    score = models.FloatField()
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}의 평 : {self.score} 점 / {self.content}'
