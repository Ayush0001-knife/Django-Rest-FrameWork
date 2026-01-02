from django.db import models

# Create your models here.
class Bot(models.Model):
      bot_id = models.CharField(max_length=10, unique=True)
      bot_name = models.CharField(max_length=100)
      designation = models.CharField(max_length=100)

      def __str__(self):
            return self.bot_name
