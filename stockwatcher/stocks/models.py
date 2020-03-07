from django.db import models


class Stock(models.Model):
    company = models.TextField(max_length=200)

    def __str__(self):
        return self.company


class Quote(models.Model):
    high = models.FloatField()
    low = models.FloatField()
    volume = models.IntegerField()
    open = models.FloatField()
    close = models.FloatField()
    time_stamp = models.DateTimeField()
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.time_stamp} {self.open} {self.close} {self.high} {self.low} {self.volume}'
