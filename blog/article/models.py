from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=128, unique=True)
    content = models.TextField()
    pubDateTime = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-pubDateTime', )
    
    
class Comment(models.Model):
    article = models.ForeignKey(Article)
    content = models.CharField(max_length=128)
    
    def __str__(self):
        return self.article.title + '-' + str(self.id)