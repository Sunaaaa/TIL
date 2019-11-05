from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50)
    title_en = models.CharField(max_length=60)
    audience = models.IntegerField()
    open_date = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    watch_grade = models.CharField(max_length=10)
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()

class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Model Level 에서 MetaData 설정
    # 정렬
    class Meta:
        ordering = ['pk',]

    # 객체 표시 형식 수정
    def __str__(self):
        return self.content

