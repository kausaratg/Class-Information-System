from django.db import models

# Create your models here.
class ClassGroup(models.Model):
    group = models.CharField(max_length=50)

    def __str__(self):
        return self.group

class Post(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    group = models.ForeignKey(ClassGroup, on_delete = models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    update_post = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
