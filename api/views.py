from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from students.models import Student
from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status,mixins,generics,viewsets
from rest_framework.views import APIView
from employee.models import Employee
from .serializers import EmployeeSerializer
from workers.models import Worker
from bot.models import Bot
from .serializers import WorkerSerializer
from .serializers import BotSerializer
from agents.models import Agent
from .serializers import AgentSerializer




# Function Based View
@api_view(['GET','POST'])
def studentView(request):
      if(request.method == "GET"):
            students = Student.objects.all()
            serializer = StudentSerializer(students, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
      elif(request.method == "POST"):
            serializer = StudentSerializer(data=request.data)
            if serializer.is_valid():
                  serializer.save()
                  return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
      
# Function Based View
@api_view(['GET','PUT','DELETE'])
def studentDetailView(request, id):
      try:
            student = Student.objects.get(pk=id)
      except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

      if request.method == 'GET':
            serializer = StudentSerializer(student)
            return Response(serializer.data,status=status.HTTP_200_OK)

      elif request.method == 'PUT':
            serializer = StudentSerializer(student, data=request.data)
            if serializer.is_valid():
                  serializer.save()
                  print(serializer.data)
                  return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
      
      elif request.method == 'DELETE':
            student.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)



# Class Based View
class Employees(APIView):
      def get(self,request):
            employees = Employee.objects.all()
            serializer = EmployeeSerializer(employees,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
      
      def post(self,request):
            employee = request.data
            serializer = EmployeeSerializer(data=employee)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# Class Based View
class EmployeeDetail(APIView):
      def get_object(self, id):
            try:
                  return Employee.objects.get(pk=id)
            except Employee.DoesNotExist:
                  raise Response(status=status.HTTP_404_NOT_FOUND)
            
      def get(self, request, id):
            employee = self.get_object(id)
            serializer = EmployeeSerializer(employee)
            return Response(serializer.data,status=status.HTTP_200_OK)

      def put(self, request, id):
            employee = self.get_object(id)
            serializer = EmployeeSerializer(employee, data=request.data)
            if serializer.is_valid():
                  serializer.save()
                  return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

      def delete(self, request, id):
            employee = self.get_object(id)
            employee.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


# Mix Based View
class Workers(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
      
      queryset=Worker.objects.all()
      serializer_class = WorkerSerializer   
      
      def get(self,request):
            return self.list(request)
      
      def post(self,request):
            return self.create(request)


# Mixins Based View
class WorkerDetail(mixins.DestroyModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,generics.GenericAPIView):

      queryset=Worker.objects.all()
      serializer_class = WorkerSerializer   

      def get(self,request,pk):
            return self.retrieve(request,pk)
      
      def put(self,request,pk):
            return self.update(request,pk)
      
      def delete(self,request,pk):
            return self.destroy(request,pk)
      

# Generic Based View
class Bots(generics.ListCreateAPIView):   # ListAPIView for listing all bots, CreateAPIView for creating a new bot and we can use only one Api View to do both of their functionality which is ListCreateAPIView
      queryset=Bot.objects.all()
      serializer_class = BotSerializer  

# Generic Based View
class BotDetail(generics.RetrieveAPIView,generics.DestroyAPIView,generics.UpdateAPIView):
      queryset=Bot.objects.all()
      serializer_class = BotSerializer  
      lookup_field='pk'    # To search the data by primary key


# Viewset Based using ----- >    viewsets.ViewSet
class AgentViewSet(viewsets.ViewSet):
      
      def list(self,request):
            queryset=Agent.objects.all()
            serializer=AgentSerializer(queryset,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)

      def create(self,request):
            serializer=AgentSerializer(data=request.data)
            if(serializer.is_valid()):
                  serializer.save()
                  return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


      def retrieve(self,request,pk=None):
           agent = get_object_or_404(Agent,pk=pk)
           serializer=AgentSerializer(agent)
           return Response(serializer.data,status=status.HTTP_200_OK)


