from .models import Course, Comment, Like ### imports my models from models.py
from .serializers import CourseSerializer, CourseDetailSerializer, CommentSerializer, LikeSerializer ### imports my serializers from serializers.py
from rest_framework.views import APIView ### imports APIView from rest_framework. This allows me to create class-based views that handle HTTP requests.Get, Post, Put, Delete
from rest_framework.response import Response ### imports Response from rest_framework. This is used to return HTTP responses with data and status codes.
from django.http import Http404 ### imports Http404 exception from django.http. This is used to raise a 404 error when an object is not found.
from rest_framework import status, permissions, viewsets ### status gives me HTTP status codes like HTTP_200_OK, permissions allows me to set access control, viewsets allows me to create viewsets for my models.
from .permissions import IsOwnerOrReadOnly ### imports custom permission class from permissions.py
from rest_framework.permissions import IsAuthenticated ### imports IsAuthenticated permission class from rest_framework.permissions
from django.shortcuts import get_object_or_404 ### imports get_object_or_404 shortcut from django.shortcuts. This is used to retrieve an object or raise a 404 error if not found.
from django.db.models import Avg ### imports Avg aggregation function from django.db.models. This is used to calculate the average rating for courses.

class CourseListCreate(APIView): ### created a class-based view for listing and creating courses. We use APIView as the base class, therefore we need to define get and post methods.
    permission_classes = [permissions.AllowAny] ### sets the permission classes for this view. Only authenticated users can create courses, but anyone can view the list of courses.
    ### defines the get method to handle GET requests.
    def get(self, request, format=None):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    #### defines the post method to handle POST requests.
    def post(self, request, format=None):
        serializer = CourseSerializer(data=request.data)        
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseDetail(APIView): ### created a class-based view for retrieving, updating, and deleting a specific course.
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] ### sets the permission classes for this view. Only authenticated users can update or delete courses, but anyone can view course details.
    ### helper method to get the course object or raise 404 if not found.
    def get_object(self, pk):
        try: 
            course = Course.objects.get(pk=pk) ### tries to get the course object by primary key (pk).
            self.check_object_permissions(self.request, course) ### checks if the user has permission to access this course. It uses the check_object_permissions method provided by APIView which is isOwnerOrReadOnly in this case.
            return course ### returns the course object if found and permissions are valid.
        except Course.DoesNotExist: ### if the course does not exist, it raises Http404 exception.
            raise Http404 ### raises a 404 error if the course is not found.
    #### defines the get method to handle GET requests for a specific course.
    def get(self, request, pk, format=None):
        course = self.get_object(pk) ### load the course and check permissions.
        serializer = CourseDetailSerializer(course) ### serializes the course object using CourseDetailSerializer.
        return Response(serializer.data) ### returns the serialized data in the response.
    ### defines the put method to handle PUT requests for updating a specific course.
    def put(self, request, pk):
        course = self.get_object(pk) ### load the course and check permissions.
        serializer = CourseDetailSerializer(instance=course, data=request.data , partial=True)### creates a serializer instance with the existing course object and the new data from the request. partial=True allows partial updates.
        if serializer.is_valid(): ### checks if the provided data is valid according to the serializer's validation rules.
            serializer.save() ### saves the updated course object to the database.
            return Response(serializer.data) ### returns the serialized data in the response.
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) ### if the data is not valid, it returns the validation errors with a 400 Bad Request status.
    ### defines the delete method to handle DELETE requests for deleting a specific course.
    def delete(self, request, pk):
        course = self.get_object(pk) ### load the course and check permissions.
        course.delete() ### deletes the course object from the database.
        return Response(status=status.HTTP_204_NO_CONTENT) ### returns a 204 No Content response indicating successful deletion.

class CourseViewSet(viewsets.ModelViewSet): ### created a viewset for the Course model. This provides default implementations for CRUD( get, post,put,delete) operations.
    queryset = Course.objects.all() ### defines the queryset for this viewset, which includes all Course objects.This tells the viewset which data to operate on. Every action will be performed on this queryset unless overridden. Basicallly, it fetches all Course records from the database.
    serializer_class = CourseSerializer ### specifies the serializer class to be used for serializing and deserializing Course objects.
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly] ### sets the permission classes for this viewset. Only authenticated users can modify courses, and only the owner of a course can edit or delete it.

class CommentList(APIView): ### created a class-based view for listing and creating comments.
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] ### sets the permission classes for this view. Only authenticated users can create comments, but anyone can view the list of comments.
    ### defines the get method to handle GET requests.
    def get(self, request, format=None):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    ### defines the post method to handle POST requests.
    def post(self, request, pk):
        course=get_object_or_404(Course, pk=pk) ### retrieves the course object by primary key (pk) or raises 404 if not found.
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user , course=course)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

class LikeList(APIView): ### created a class-based view for listing and creating likes.
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] ### sets the permission classes for this view. Only authenticated users can create likes, but anyone can view the list of likes.
    ### defines the get method to handle GET requests.
    def get(self, request, format=None):
        likes = Like.objects.all()
        serializer = LikeSerializer(likes, many=True)
        return Response(serializer.data)
    ### defines the post method to handle POST requests.
    def post(self, request, pk):
        course=get_object_or_404(Course, pk=pk) ### retrieves the course object by primary key (pk) or raises 404 if not found.
        if Like.objects.filter(author=request.user, course=course).exists():
            return Response({"detail": "You have already liked this course."}, status=status.HTTP_406_NOT_ACCEPTABLE)
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user, course=course)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FeaturedCourses(APIView):
    permission_classes = [permissions.AllowAny] ### allows any user to access this view.
    def get(self, request):
        courses=Course.objects.all()
        featured_courses = courses.annotate(avg_rating=Avg('comments__rating')).order_by('-avg_rating')[:5]
        serializer = CourseSerializer(featured_courses, many=True)
        return Response(serializer.data)
#the end