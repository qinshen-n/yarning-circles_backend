# from rest_framework import serializers
# from django.apps import apps

# class CourseSerializer(serializers.ModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.username')
#     likes_count = serializers.SerializerMethodField()

#     class Meta:
#         model = apps.get_model ('courses.Course')
#         fields = '__all__'


# class CourseDetailSerializer(CourseSerializer):
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.course_content = validated_data.get('course_content', instance.course_content)
#         instance.category = validated_data.get('category', instance.category)
#         instance.image = validated_data.get('image', instance.image)
#         instance.is_open = validated_data.get('is_open', instance.is_open)
#         instance.save()
#         return instance




# class CommentSerializer(serializers.ModelSerializer):
#     user = serializers.ReadOnlyField(source='user.id')
#     likes_count = serializers.SerializerMethodField()

#     class Meta:
#         model = apps.get_model('courses.Comment')
#         fields = '__all__'

#     def update (self, instance, validated_data):
#         instance.content = validated_data.get('content', instance.content)
#         instance.save()
#         return instance