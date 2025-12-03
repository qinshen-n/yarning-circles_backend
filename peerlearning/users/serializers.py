from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    courses_created = serializers.SerializerMethodField()
    courses_liked = serializers.SerializerMethodField()
    
    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
    
    def get_courses_created(self, obj):
        from courses.serializers import CourseSerializer
        courses = obj.courses.all()  # Uses related_name='courses' from Course.owner
        return CourseSerializer(courses, many=True, context=self.context).data
    
    def get_courses_liked(self, obj):
        from courses.models import Like
        from courses.serializers import CourseSerializer
        
        likes = Like.objects.filter(author=obj).select_related('course')
        courses = [like.course for like in likes]
        return CourseSerializer(courses, many=True, context=self.context).data