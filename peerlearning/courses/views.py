# from django.shortcuts import render
# from .models import Course, Comment
# from .serializers import CourseSerializer, CourseDetailSerializer, CommentSerializer
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.http import Http404
# from rest_framework import status, permissions, viewsets
# from .permissions import IsOwnerOrReadOnly
# from rest_framework.permissions import IsAuthenticated
# from django.shortcuts import get_object_or_404

# class CourseListCreate(APIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     def get(self, request, format=None):
#         courses = Course.objects.all()
#         serializer = CourseSerializer(courses, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = CourseSerializer(data=request.data)        
#         if serializer.is_valid():
#             serializer.save(owner=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# class CourseDetail(APIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     def get_object(self, pk):
#         try:
#             course = Course.objects.get(pk=pk)
#             self.check_object_permissions(self.request, course)
#             return course
#         except Course.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         course = self.get_object(pk)
#         serializer = CourseDetailSerializer(course)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         course = self.get_object(pk)
#         serializer = CourseDetailSerializer(instance=course, data=request.data , partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

#     def delete(self, request, pk):
#         course = self.get_object(pk)
#         course.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
# class courseViewSet(viewsets.ModelViewSet):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


# class CommentList(APIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     def get(self, request, format=None):
#         comments = Comment.objects.all()
#         serializer = CommentSerializer(comments, many=True)
#         return Response(serializer.data)

#     def post(self, request, pk):
#         serializer = CommentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(owner=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
    