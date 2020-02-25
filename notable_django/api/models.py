from django.db import models


# Create your models here.
class InputData(models.Model):
    max_occured_sublocation = models.CharField(max_length=20)
    total_alarm_duration = models.FloatField()
    bucket_size = models.IntegerField()
    hourly_timestamp = models.CharField(max_length=20)

    def __str__(self):
        return '{}, {}, {}, {}, {}, {}, {}'.format(self.max_occured_sublocation,\
        self.total_alarm_duration, self.bucket_size, self.day_of_week,\
        self.day_of_month, self.month_of_year, self.hour)
