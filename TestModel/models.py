from django.db import models

class t_user(models.Model):
    name = models.CharField(max_length = 20)