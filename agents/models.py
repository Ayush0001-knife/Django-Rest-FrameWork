from django.db import models

# Create your models here.
class Agent(models.Model):
      agent_id = models.CharField(max_length=10, unique=True)
      agent_name = models.CharField(max_length=100)
      designation = models.CharField(max_length=100)

      def __str__(self):
            return self.agent_name
