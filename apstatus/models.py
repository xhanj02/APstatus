from django.db import models

# Create your models here.
class ips(models.Model):
    name = models.CharField(max_length=30, blank=True)
    ip = models.CharField(primary_key=True, max_length=15, blank=True)
    t11 = models.IntegerField(blank=True, null=True, default=2, editable=False)
    t10 = models.IntegerField(blank=True, null=True, default=2, editable=False)
    t9 = models.IntegerField(blank=True, null=True, default=2, editable=False)
    t8 = models.IntegerField(blank=True, null=True, default=2, editable=False)
    t7 = models.IntegerField(blank=True, null=True, default=2, editable=False)
    t6 = models.IntegerField(blank=True, null=True, default=2, editable=False)
    t5 = models.IntegerField(blank=True, null=True, default=2, editable=False)
    t4 = models.IntegerField(blank=True, null=True, default=2, editable=False)
    t3 = models.IntegerField(blank=True, null=True, default=2, editable=False)
    t2 = models.IntegerField(blank=True, null=True, default=2, editable=False)
    t1 = models.IntegerField(blank=True, null=True, default=2, editable=False)
    t0 = models.IntegerField(blank=True, null=True, default=2, editable=False)

    class Meta:
        db_table = 'ips'
