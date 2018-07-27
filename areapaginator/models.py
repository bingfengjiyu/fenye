from django.db import models

# Create your models here.


class BooktestAreainfo(models.Model):
    atitle = models.CharField(max_length=20)
    aparent = models.ForeignKey('self', db_column='aParent_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'booktest_areainfo'

