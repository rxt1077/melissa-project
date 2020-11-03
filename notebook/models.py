from django.db import models

class Notebook(models.Model):
    name = models.CharField(max_length=64)
    desc = models.CharField(max_length=256)
    importance = models.CharField(
        max_length=2,
        choices=[
            ('LW',"LOW"),
            ('MD',"MEDIUM"),
            ('HG',"HIGH")
       
        ]
    )
