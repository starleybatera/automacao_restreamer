from django.db import models

class Usuario(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique = True)
    password = models.CharField(max_length = 254, db_column = 'senha')

    def __str__(self):
        return self.username