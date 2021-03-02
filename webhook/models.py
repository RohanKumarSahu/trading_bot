from django.db import models

class Data(models.Model):
    direction = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255, null=True)
    exchange = models.CharField(max_length=255, null=True)
    ticker = models.CharField(max_length=255, null=True)
    volume = models.IntegerField()
    time = models.TimeField()
    timenow = models.DateTimeField()

    def __str__(self):
        return self.email
