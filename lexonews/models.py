from django.db import models
from django.utils import timezone

class Article(models.Model):
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        verbose_name="höfundur",
        )
    headline = models.CharField(
        "fyrirsögn",
        max_length=200,
        )
    text = models.TextField("Meginmál")
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.headline
