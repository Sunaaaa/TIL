from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.CharField(max_length=4)

    created_at = models.DateTimeField(auto_now_add=True)

    # 객체를 표시하는 형식 Customizing
    def __str__(self):
        return f'[{self.pk}] : {self.name} | {self.age}'