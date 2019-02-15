from django.db import models
from joins.models import t_acct

# Create your models here.

class t_assets(models.Model):
    rootid = models.ForeignKey(t_acct, on_delete=models.CASCADE, null=True, blank=True )
    name = models.CharField(max_length=120, default='')
    serial_no = models.CharField(max_length=120, default='')
    department = models.CharField(max_length=120, default='office')
    zone = models.CharField(max_length=120, default='IOC')
    equip_type = models.CharField(max_length=120, default='')
    user = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)
    updated = models.DateTimeField(auto_now_add = False, auto_now=True)

    def __unicode__(self):
        return 't_assets{}'.format(self.id)  