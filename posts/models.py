from django.db import models

POST_IMPORTANCE = (
    ('Very Important','Content very important'),
    ('Even Important','Content moderately important'),
    ('Not Impotant','Casual post, low importance')
)

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    author = models.CharField(max_length= 20)
    importance = models.CharField(choices=POST_IMPORTANCE, default='Even Important', max_length = 100)
    date = models.DateField(auto_now_add=True)

    # class Meta:
    #     ordering = ('-date',)

    def __str__(self):
        return f"{self.title}"

    def cut_article(self):
        return self.content[:50] + " ..."


class Vote(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    reason = models.TextField()
