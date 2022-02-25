from django.db import models


class Items(models.Model):
    item_name = models.CharField(max_length=120)
    item_desc = models.CharField(max_length=120)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default="shorturl.at/gzR34")

    def __str__(self):
        return self.item_name
