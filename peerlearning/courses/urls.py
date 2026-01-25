from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.CourseListCreate.as_view()),
    path('courses/<int:pk>/', views.CourseDetail.as_view()),
    path('courses/<int:pk>/comments/', views.CommentList.as_view()),
    path('courses/<int:pk>/likes/', views.LikeList.as_view()),
    path('courses/<int:pk>/ratings/', views.CourseRatingListCreate.as_view()),
    path('courses/features/', views.FeaturedCourses.as_view()),
    path('courses/image-url/', views.PresignedURLCreate.as_view()),

    # Circle meetings
    path('courses/<int:pk>/meetings/', views.CircleMeetingList.as_view(), name='circle-meetings'),
    path('meetings/<int:meeting_id>/', views.CircleMeetingDetail.as_view(), name='meeting-detail'),
    path('meetings/<int:meeting_id>/rsvp/', views.CircleMeetingRSVP.as_view(), name='meeting-rsvp'),
    
    # Circle Progress
    path('courses/<int:pk>/milestones/', views.CircleMilestoneList.as_view(), name='circle-milestones'),
    path('milestones/<int:milestone_id>/complete/', views.CircleMilestoneComplete.as_view(), name='milestone-complete'),
]