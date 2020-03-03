from django.db import models


class Newzhaopin(models.Model):
    position = models.CharField(max_length=50, blank=True, null=True)
    minsalary = models.FloatField(blank=True, null=True)
    avgsalary = models.FloatField(blank=True, null=True)
    maxsalary = models.FloatField(blank=True, null=True)
    link = models.CharField(max_length=100, blank=True, null=True)
    workspace = models.CharField(max_length=60, blank=True, null=True)
    publish = models.CharField(max_length=60, blank=True, null=True)
    comname = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'newzhaopin'
