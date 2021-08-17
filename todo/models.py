from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.fields.related import ManyToManyField

# Create your models here.
class Todo(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    isCompleted = models.BooleanField(default=False)
    like = ManyToManyField(get_user_model(), related_name='like', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    todo_date = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']