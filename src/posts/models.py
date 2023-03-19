from django.db import models
from useraccount.models import User


# Create your models here.
class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Posts(TimeStamp):

    description = models.TextField(max_length=65535, blank=True, null=True)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title
