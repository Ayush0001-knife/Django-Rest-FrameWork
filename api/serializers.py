from rest_framework import serializers
from students.models import Student
from employee.models import Employee
from workers.models import Worker


class StudentSerializer(serializers.ModelSerializer):
      class Meta:
            model= Student
            fields= "__all__"

class EmployeeSerializer(serializers.ModelSerializer):
      class Meta:
            model = Employee  
            fields = '__all__'

class WorkerSerializer(serializers.ModelSerializer):
      class Meta:
            model =  Worker 
            fields =  '__all__'
          