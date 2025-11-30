from rest_framework import serializers
from django.apps import apps
from django.db.models import Avg

class CourseSerializer(serializers.ModelSerializer):  ###ModelSerializer is DJango REST framework class that provides a way to create serializers based on Django models.
    owner = serializers.ReadOnlyField(source='owner.username') ### My model has owner field which is a ForeignKey to the User model. DRF automaticlly give owner id but by using source = 'owner.username' we are telling DRF to use the username field of the related User model instead of the default id. Shows owners username instead of id.
    likes_count = serializers.SerializerMethodField() ### This doesnt have ForeignKey but we want to show the count of likes for each course. So we use SerializerMethodField to define a custom method that will return the count of likes.
    average_rating = serializers.SerializerMethodField() ### Similar to likes_count, we want to show average rating for each course based on the related comments. We will define a method to calculate the average rating.
    
    class Meta: ###
        model = apps.get_model('courses.Course') ### model tells DRF to serializer which model to use for this serializer.
        fields = '__all__' ### fields = '__all__' tells DRF to include all fields of the model in the serializer. It includes my custom fields such as owner, likes count, average_rating as well.
        read_only_fields = ('owner', 'views_count', 'completions', 'created_at', 'updated_at')

    def get_likes_count(self, obj): ### Custom method to get the count of likes for a course. obj is the course instance being serialized.
        return obj.likes.count()   ###obj.likes reverse relationship defined in the Like model related_name='likes'. We use count() method to get the total number of likes for the course. 
    
    def get_average_rating(self, obj):
        avg = obj.comments.aggregate(Avg('rating'))['rating__avg']
        return round(avg, 2) if avg is not None else None

class CourseDetailSerializer(CourseSerializer): ### Inheriting from CourseSerializer to reuse its fields and methods.We created it in the above class.
    ### We could the below however, we are going to use for loop to make it more dynamic.

    #### def update(self, instance, validated_data):
    ####     instance.title = validated_data.get('title', instance.title)
    ####     instance.course_content = validated_data.get('course_content', instance.course_content)
    ####     instance.category = validated_data.get('category', instance.category)
    ####     instance.image = validated_data.get('image', instance.image)
    ####     instance.is_open = validated_data.get('is_open', instance.is_open)
    ####     instance.save()
    ####     return instance

    def update(self, instance, validated_data): ### update is a special DRF method that is called when we want to update an existing instance of a model. instance is the existing course object that we want to update, validated_data is the data that has been validated by the serializer.
        excluded_fields = {'owner', 'created_at', 'updated_at'} ### We dont want to update these fields.
        for field, value in validated_data.items(): ### Loop through each field and its corresponding value in the validated data.
            if field not in excluded_fields: ### Check if the field is not in the excluded fields.
                setattr(instance, field, value) ### setattr is a built-in Python function that sets the value of an attribute of an object. Here we are setting the value of the field on the instance to the new value from validated_data.
        instance.save() ### After updating all the fields, we call instance.save() to save the changes to the database.
        return instance ### Finally, we return the updated instance.

class CommentSerializer(serializers.ModelSerializer): ### Serializer for the Comment model. serializers.ModelSerializer is a DRF class that provides a way to create serializers based on Django models.
    author = serializers.ReadOnlyField(source='author.username') ### author field is a ForeignKey to the User model. By using source='author.username' we are telling DRF to use the id field of the related User model instead of the default representation.
    rating = serializers.IntegerField(min_value=1, max_value=5, required=False) ### rating field is an optional field that allows users to rate the course from 1 to 5. We use IntegerField with min_value and max_value validators to ensure the rating is within the specified range.
    
    class Meta:
        model = apps.get_model('courses.Comment') ### model tells DRF which model to use for this serializer. 
        fields = '__all__' ### fields = '__all__' tells DRF to include all fields of the model in the serializer. It includes my custom fields such as author and likes_count as well.


    ### Similar to course detail serializer, we can create a update method to allow updating comments. 
    def update (self, instance, validated_data):        
        instance.content = validated_data.get('content', instance.content)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.save()
        return instance
    
class LikeSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    course = serializers.ReadOnlyField(source='course.id')
    
    class Meta:
        model = apps.get_model('courses.Like')  # Use apps.get_model instead
        fields = ['id', 'author', 'course', 'created_at']
        read_only_fields = ['id', 'author', 'course', 'created_at']
