from django.db import models

# Create your models here.
from django.db import models


class JsonData(models.Model):
    # song title
    Date = models.DateField(),
    Open = models.FloatField(max_length=5),
    High = models.FloatField(max_length=5),
    Low = models.FloatField(max_length=5),
    Close =  models.FloatField(max_length=5),
    Shares_Traded = models.IntegerField(max_length=10),
    Turnover_Crs = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return "{} - {}".format(self.Date, self.High)