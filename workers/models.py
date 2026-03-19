from django.db import models

# Create your models here.
class Worker(models.Model):
      worker_id = models.CharField(max_length=10, unique=True)
      worker_name = models.CharField(max_length=100)
      designation = models.CharField(max_length=100)

      def __str__(self):
            return self.worker_name