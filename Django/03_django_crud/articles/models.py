from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

# Create your models here.
# django.db의  models에서 상속 받아서 사용한다.
class Article(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()

    # 원래 대로 라면, 새로운 필드를 추가하고 나면, makemigrations 할때, 
    # 어떤 값을 넣을 것인지 Django 가 물어본다. 기본적으로 blank = False이기 때문이다.
    # blank=True : '빈 문자열' 이 들어가도 된다.
    # image = models.ImageField(blank=True)
    image = ProcessedImageField(
        processors=[Thumbnail(200,300)],    # 처리할 작업
        format='JPEG',              # 이미지 포맷
        options={                   # 각종 추가 옵션
            'quality' : 90
        },
        upload_to = 'articles/image' # 저장 위치
        # 실제 경로 : MEDIA_ROOT/articles/image
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 객체 표시 형식 수정
    def __str__(self):
        return f'[{self.pk}] : {self.title} '

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Model Level 에서 MetaData 설정
    class Meta:
        ordering = ['-pk',]

    # 객체 표시 형식 수정
    def __str__(self):
        return self.content