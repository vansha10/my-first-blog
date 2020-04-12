from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    likers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likers')
    dislikers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='dislikers')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def add_like(self, request):
        if (self.likers.all().filter(id=request.user.id).exists()):
            # already liked
            self.likes -= 1
            self.likers.remove(request.user) 
            self.save()
        else:
            self.likes += 1
            self.likers.add(request.user) 
            self.save()
    def add_dislike(self, request):
        if (self.dislikers.all().filter(id=request.user.id).exists()):
            self.dislikes -= 1
            self.dislikers.remove(request.user)
            self.save()
        else:
            self.dislikes += 1
            self.dislikers.add(request.user) 
            self.save()

        
class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text