from django import forms
from .models import Movie, Rating

# Django Model Form 
# Model Form 
# 1. Model Form 클래스를 상속받아 사용
# 2. 메타 데이터로 Model 정보를 건네주면, ModelForm이 자동으로 field에 맞춰 input을 생성해준다.
class MovieForm(forms.ModelForm):
    title = forms.CharField(
        max_length=10, 
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class' : 'title',
                'placeholder' : '제목을 입력해주세요~',
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class' : 'content',
                'placeholder' : '내용을 입력해주세욥',
                'rows' : 5,
                'cols' : 30,
            }
        )
    )
    # 메타 데이터 -> 데이터의 데이터
    # ex > 사진 한장 -> 촬영 장비 이름, 촬영 환경 등 사진 한장에 대한 데이터 
    class Meta:
        model = Movie
        fields = ('title', 'content', 'poster',)

class RatingForm(forms.ModelForm):
    score = forms.FloatField(
        required=False, 
        max_value=5, min_value=0, 
        widget=forms.NumberInput(
            attrs={
                'id': 'score', 
                'step': "0.01"
            }
        )
    )

    content=forms.CharField(
        label="한줄평",
        widget=forms.Textarea(
            attrs={
                'class' : 'content',
                'placeholder' : '한줄평을 작성해주세요.',
                'rows' : 1,
                'cols' : 100,

            }
        )
    )
    class Meta:
        model = Rating
        fields = ('score', 'content', )
