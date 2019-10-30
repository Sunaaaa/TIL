from django.db import models

# Create your models here.
# django.db.models.Model 클래스를 상속받아서 모델을 정의함!
class Article(models.Model):
    # id(PK)는 인스턴스 생성과 함께 자동으로 부여된다.
    # 그래서 model을 정의할 때 따로 작성하지 않아도 된다 .

    # 컬럼 

    # CharField에서 max_length (최대 길이)는 필수 인자
    # django 내부에서 데이터 유효성 검증을 할 때 사용한다.
    title = models.CharField(max_length=30) 

    # 긴 문자열은 TextField를 사용한다.
    content = models.TextField()

    # 생성한 날짜 / 수정한 날짜
    # auto_now_add : 생성시점에 자동으로 등록 , 인스턴스 최초 생성 시각
    # auto_now : 인스턴스 최종 수정 시각 (업데이트됨)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    # 객체를 표시하는 형식 Customizing
    def __str__(self):
        return f'[{self.pk}번글] : {self.title} | {self.content}'
    