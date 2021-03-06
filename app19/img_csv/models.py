from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=130)
    phone = models.CharField(max_length=150, unique=True)
    profile = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'profile'
