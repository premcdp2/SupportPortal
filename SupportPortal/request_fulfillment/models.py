from django.db import models
from django.utils import timezone

class New_services(models.Model):
    service_name = models.CharField(max_length=20)
    add_time = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return "Activity Name: {}, added : {}".format(self.service_name, self.add_time)