from django.db import models


class Avtomobile(models.Model):
    Id = models.CharField(max_length=100, blank=False)
    brand= models.TextField(max_length=1000, blank=False)
    model = models.CharField(max_length=100, blank=False)
    # year = models.IntegerField(blank=False, default=2000)

    def __str__(self) -> str:
        return self.title