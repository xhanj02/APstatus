from django.db import models

# Create your models here.
class ips(models.Model):
    ip = models.CharField(primary_key=True, max_length=15, blank=True)
    t11 = models.IntegerField(blank=True, null=True, default=2)
    t10 = models.IntegerField(blank=True, null=True, default=2)
    t9 = models.IntegerField(blank=True, null=True, default=2)
    t8 = models.IntegerField(blank=True, null=True, default=2)
    t7 = models.IntegerField(blank=True, null=True, default=2)
    t6 = models.IntegerField(blank=True, null=True, default=2)
    t5 = models.IntegerField(blank=True, null=True, default=2)
    t4 = models.IntegerField(blank=True, null=True, default=2)
    t3 = models.IntegerField(blank=True, null=True, default=2)
    t2 = models.IntegerField(blank=True, null=True, default=2)
    t1 = models.IntegerField(blank=True, null=True, default=2)
    t0 = models.IntegerField(blank=True, null=True, default=2)

    class Meta:
        db_table = 'ips'
