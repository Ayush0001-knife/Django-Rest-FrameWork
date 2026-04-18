from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from django.urls import include



router = DefaultRouter()
router.register('agents',views.AgentViewSet,basename='agent')



urlpatterns=[
      path('students/',views.studentView),
      path('students/<int:id>/',views.studentDetailView),

      path('employees/',views.Employees.as_view()),
      path('employees/<int:id>/',views.EmployeeDetail.as_view()),

      path('workers/',views.Workers.as_view()),
      path('workers/<int:pk>/',views.WorkerDetail.as_view()),

      path('bots/',views.Bots.as_view()),
      path('bots/<int:pk>/',views.BotDetail.as_view()),

      # For viewsets
      path('',include(router.urls)),

      path('blogs/',views.Blogs.as_view()),
      # path('blogs/<int:pk>/',include.BlogsDetail.as_view()),
      path('comments/',views.Comments.as_view()),
      # path('comments/<int:pk>/',include.CommentsDetail.as_view()),
] 