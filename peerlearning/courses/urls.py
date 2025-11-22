from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.CourseListCreate.as_view()),
    path('courses/<int:pk>/', views.CourseDetail.as_view()),
    path('courses/<int:pk>/comments/', views.CommentList.as_view()),
    path('courses/<int:pk>/likes/', views.LikeList.as_view()),
    path('courses/features/', views.FeaturedCourses.as_view()),
]