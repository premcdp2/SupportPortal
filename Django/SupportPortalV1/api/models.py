from django.db import models

#  My models are here.

class Activity(models.Model):
    activities = models.CharField(max_length=30)

    def __str__(self):
        return "Activities are : {}".format(self.activities)

class WindowsActivity(models.Model):
    w_activities = models.CharField(max_length=30)


