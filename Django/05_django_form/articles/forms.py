from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(
        max_length=40, 
        # HTML TAG 와 동일
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