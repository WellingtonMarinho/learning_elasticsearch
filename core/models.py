from django.db import models


class People(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    birthdate = models.DateField()

    def __str__(self):
        return self.name.title()

    class Meta:
        db_table = 'peoples'
