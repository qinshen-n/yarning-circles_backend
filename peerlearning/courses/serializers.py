from rest_framework import serializers
from django.apps import apps
from django.db.models import Avg
from .models import (
    CircleMeeting,
    MeetingRSVP,
    CircleMilestone,
    MilestoneCompletion
)

class CourseSerializer(serializers.ModelSerializer):  ###ModelSerializer is DJango REST framework class that provides a way to create serializers based on Django models.
    owner = serializers.ReadOnlyField(source='owner.username') ### My model has owner field which is a ForeignKey to the User model. DRF automaticlly give owner id but by using source = 'owner.username' we are telling DRF to use the username field of the related User model instead of the default id. Shows owners username instead of id.
    owner_id = serializers.ReadOnlyField(source='owner.id')
    likes_count = serializers.SerializerMethodField() ### This doesnt have ForeignKey but we want to show the count of likes for each course. So we use SerializerMethodField to define a custom method that will return the count of likes.
    average_rating = serializers.SerializerMethodField() ### Kept for backward compatibility; now prefers course.rating_average.
    rating_count = serializers.SerializerMethodField()
    user_has_liked = serializers.SerializerMethodField()  # Add this field
    
    class Meta: ###
        model = apps.get_model('courses.Course') ### model tells DRF to serializer which model to use for this serializer.
        fields = '__all__' ### fields = '__all__' tells DRF to include all fields of the model in the serializer. It includes my custom fields such as owner, likes count, average_rating as well.
        read_only_fields = ('owner', 'views_count', 'completions', 'created_at', 'updated_at')

    def get_likes_count(self, obj): ### Custom method to get the count of likes for a course. obj is the course instance being serialized.
        return obj.likes.count()   ###obj.likes reverse relationship defined in the Like model related_name='likes'. We use count() method to get the total number of likes for the course. 
    
    def get_average_rating(self, obj):
        # Prefer the denormalized field if present
        if hasattr(obj, 'rating_average') and obj.rating_average is not None:
            return float(obj.rating_average)
        avg = obj.ratings.aggregate(Avg('score'))['score__avg']
        return round(avg, 2) if avg is not None else None

    def get_rating_count(self, obj):
        if hasattr(obj, 'rating_count') and obj.rating_count is not None:
            return obj.rating_count
        return obj.ratings.count()
    
    def get_user_has_liked(self, obj):
        """Check if the current user has liked this course"""
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.likes.filter(author=request.user).exists()
        return False

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
        read_only_fields = ['course']


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

class RatingSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = apps.get_model('courses.Rating')
        fields = ['id', 'course', 'user', 'score', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

    # Serializer for CircleMeeting model
class CircleMeetingSerializer(serializers.ModelSerializer):
    # Read-only fields that show related data
    created_by = serializers.ReadOnlyField(source='created_by.username')

    # Calculated fields
    rsvp_yes_count = serializers.SerializerMethodField()
    rsvp_maybe_count = serializers.SerializerMethodField()
    rsvp_no_count = serializers.SerializerMethodField()
    user_rsvp_status = serializers.SerializerMethodField()
    attendees = serializers.SerializerMethodField()
    
    class Meta:
        model = CircleMeeting
        fields = [
            'id', 'circle', 'title', 'description', 'datetime', 
            'duration_minutes', 'meeting_type', 'online_link', 
            'physical_location', 'created_by', 'created_at',
            'rsvp_yes_count', 'rsvp_maybe_count', 'rsvp_no_count',
            'user_rsvp_status', 'attendees'
        ]
        read_only_fields = ['id', 'circle', 'created_by', 'created_at']

    def get_rsvp_yes_count(self, obj):
        # Count how many people RSVP'd 'yes'
        return obj.rsvps.filter(status='yes').count()
    
    def get_rsvp_maybe_count(self, obj):
        # Count how many people RSVP'd 'maybe'
        return obj.rsvps.filter(status='maybe').count()
    
    def get_rsvp_no_count(self, obj):
        # Count how many people RSVP'd 'no'
        return obj.rsvps.filter(status='no').count()
    
    def get_user_rsvp_status(self, obj):
        # Get current user's RSVP status (yes/maybe/no or None)
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            rsvp = obj.rsvps.filter(user=request.user).first()
            return rsvp.status if rsvp else None
        return None
    
    def get_attendees(self, obj):
        # Get list of usernames who RSVP'd 'yes'
        return list(
            obj.rsvps.filter(status='yes')
            .values_list('user__username', flat=True)
        )
    

# Serializer for MeetingRSVP model
class MeetingRSVPSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    meeting_title = serializers.ReadOnlyField(source='meeting.title')
    
    class Meta:
        model = MeetingRSVP
        fields = [
            'id', 'meeting', 'meeting_title', 'user', 
            'status', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

# Serializer for CircleMilestone model
class CircleMilestoneSerializer(serializers.ModelSerializer):
    # Calculated fields
    completion_count = serializers.SerializerMethodField()
    completion_percentage = serializers.SerializerMethodField()
    user_completed = serializers.SerializerMethodField()
    completed_by = serializers.SerializerMethodField()

    class Meta:
        model = CircleMilestone
        fields = [
            'id', 'circle', 'title', 'description', 'order', 'created_at',
            'completion_count', 'completion_percentage', 
            'user_completed', 'completed_by'
        ]
        read_only_fields = ['id', 'circle', 'created_at']
    
    def get_completion_count(self, obj):
        # How many users completed this milestone
        return obj.completions.count()
    
    def get_completion_percentage(self, obj):
        # Percentage of enrolled users who completed this
        
        # Get all unique users who have completions in this circle
        all_completions = MilestoneCompletion.objects.filter(
            milestone__circle=obj.circle
        ).values('user').distinct().count()

        # If no one has started, return 0
        if all_completions == 0:
            return 0
        
        # Calculate percentage
        completed = obj.completions.count()
        return round((completed / all_completions) * 100) if all_completions > 0 else 0
    
    def get_user_completed(self, obj):
        # Did the current user complete this milestone?
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.completions.filter(user=request.user).exists()
        return False
    
    def get_completed_by(self, obj):
        # List of usernames who completed this milestone
        return list(
            obj.completions.values_list('user__username', flat=True)
        )

# Serializer for MilestoneCompletion model
class MilestoneCompletionSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    milestone_title = serializers.ReadOnlyField(source='milestone.title')

    class Meta:
        model = MilestoneCompletion
        fields = ['id', 'milestone', 'milestone_title', 'user', 'completed_at']
        read_only_fields = ['id', 'user', 'completed_at']