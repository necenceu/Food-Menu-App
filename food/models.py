from django.db import models

# Create your models here.

class Item(models.Model):

    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image_url = models.URLField(max_length=2048, default='https://media.istockphoto.com/id/1193057179/vector/photo-coming-soon-image-icon-vector-illustration-isolated-on-white-background-no-website.jpg?s=612x612&w=0&k=20&c=ewySSAlHhs8A97rqdS2sFrvExzs24k70n0uXeNC7peM=')
