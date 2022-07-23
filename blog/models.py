from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now = True)

    # author : 외래키 구현 시 작성 예정
    
    def __str__(self):
        return f'[{self.pk}] {self.title}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'