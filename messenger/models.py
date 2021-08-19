from django.db import models
from django.contrib.auth import get_user_model

class Message(models.Model):
    sender = models.ForeignKey(get_user_model(), on_delete = models.CASCADE, related_name = "sender", default = "")
    receiver = models.ForeignKey(get_user_model(), on_delete = models.CASCADE, related_name = "receiver", default = "")
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]