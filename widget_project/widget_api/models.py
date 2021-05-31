from django.db import models
from django.utils import timezone


class Widget(models.Model):
    name = models.CharField(max_length=64, null=False)
    number_of_parts = models.IntegerField(null=False)
    created_date = models.DateField(auto_now_add=timezone.now())
    updated_date = models.DateField(auto_now=timezone.now())

    def save(self, *args, **kwargs):
        # since sqlite3 won't enforce the max_length=64 on the 'name'
        # field, we have to implement the save() method to call
        # clean_fields() first before saving
        self.clean_fields()
        super().save(*args, **kwargs)
