from django.db import models
from django.contrib.auth import get_user_model 
from django.core.validators import MinValueValidator, MaxValueValidator ### For rating field in comments to limit 1 to 5

class Course(models.Model):
    title = models.CharField(max_length=255) ####We have stated 10 words but it may need some adjustment. This is something that need to be checked later.
    brief_description = models.CharField(max_length=500) ####We have stated  max 50 words. Will work on later.
    course_content = models.TextField() ###This is the main body of the course where all the lessons will be written.
    CATEGORY_CHOICES = [
        ('science and technology', 'Science and Technology'),
        ('arts and crafts', 'Arts and Crafts'),
        ('reading and writing', 'Reading and Writing'),
        ('music and musical instruments', 'Music and Musical Instruments'),
        ('languages', 'Languages'),
        ('health and wellness', 'Health and Wellness'),
        ('business and finance', 'Business and Finance'),
        ('personal development', 'Personal Development'),
        ('other', 'Other'),
    ] ### This is the list of categories for the courses. It will be drop down menu in the frontend.Might be multiple choice or radio button. To be checked later.
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES , default='arts and crafts') #### Default value to be changed later.
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='courses') #### The user who created the course.
    participants = models.ManyToManyField(
        get_user_model(),
        related_name = "join_courses",
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True) ### The date and time when the course was created.
    updated_at = models.DateTimeField(auto_now=True) ### The date and time when the course was last updated. It might be hard to track this in the frontend.Nice to have feature.
    image=models.URLField(blank=True, null=True) ### URL for the course image. Optional field for now. Trying to change this with upload feature later.
    is_open = models.BooleanField(default=True) ### To indicate if the course is open for enrollment or not.
    max_students = models.PositiveIntegerField(null=True, blank=True) ### Maximum number of students allowed to enroll in the course. Optional field.   
    
    ### More features can be added later as per the requirements.
    ### Below this line is totally optional and can be removed if not needed.###
    DIFFICULTY_LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]
    difficulty_level = models.CharField(max_length=20, choices=DIFFICULTY_LEVEL_CHOICES, default='beginner') ### Difficulty level of the course.
    duration_in_hours = models.PositiveIntegerField(null=True, blank=True) ### Duration of the course in hours. 
    learning_objectives = models.TextField(blank=True) ### Learning objectives of the course.
    enrollment_end = models.DateTimeField(null=True, blank=True)
    views_count = models.PositiveIntegerField(default=0)
    completions = models.PositiveIntegerField(default=0)
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft') ### Status of the course.
    rating_count = models.PositiveIntegerField(default=0)
    rating_average = models.DecimalField(max_digits=3, decimal_places=2, default=0)  ### e.g., 4.25

### Circle Meetings ###
# WHO & WHEN; Schedule sync meetings for peer learning circles
class CircleMeeting(models.Model):
    circle = models.ForeignKey(
        'Course',
        on_delete=models.CASCADE,
        related_name='meetings'
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    datetime = models.DateTimeField() 
    duration_minutes = models.PositiveIntegerField(default=60)

    MEETING_TYPE_CHOICES = [
        ('online', 'Online'),
        ('hybrid', 'Hybrid'),
        ('in-person', 'In Person'),
    ]
    meeting_type = models.CharField(
        max_length=20,
        choices=MEETING_TYPE_CHOICES,
        default='online'
    )
    # Location Field
    online_link = models.URLField(blank=True, help_text="Zoom/Teams/Meet link")
    physical_location =models.CharField(
        max_length=300,
        blank=True,
        help_text="Physical address if hybrid or in-person"
    )
    
    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='created_meetings'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['datetime'] # Show upcoming meetings first

    def __str__(self):
        return f"{self.circle.title} - {self.title} ({self.datetime.strftime('%Y-%m-%d %H:%M')})"

### Meeting RSVPs
class MeetingRSVP(models.Model):
    meeting = models.ForeignKey(
        CircleMeeting,
        on_delete=models.CASCADE,
        related_name='rsvps'
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='meeting_rsvps'
    )

    RSVP_CHOICES = [
        ('yes', 'Yes'),
        ('maybe', 'Maybe'),
        ('no', 'No'),
    ]
    status = models.CharField(max_length=10, choices=RSVP_CHOICES, default='yes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('meeting', 'user') #Unique together constraint
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.meeting.title} ({self.status})"

### Circle Milestones ###
class CircleMilestone(models.Model):
    circle = models.ForeignKey(
        'Course', 
        on_delete=models.CASCADE, 
        related_name='milestones'
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)  # For sorting
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order']  # Display in the order facilitator sets
        unique_together = ('circle', 'order')  # No duplicate order numbers
    
    def __str__(self):
        return f"{self.circle.title} - Milestone {self.order}: {self.title}"

### Milestone Completions ###
class MilestoneCompletion(models.Model):
    milestone = models.ForeignKey(
        CircleMilestone,
        on_delete=models.CASCADE,
        related_name='completions'
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='milestone_completions'
    )
    completed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('milestone', 'user')
        ordering = ['-completed_at']

    def __str__(self):
        return f"{self.user.username} completed {self.milestone.title}"

class Comment(models.Model):
    content = models.TextField()
    course = models.ForeignKey("Course", on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveSmallIntegerField(null=True, blank=True, validators=[ MinValueValidator(1), MaxValueValidator(5)]) ### Optional rating field from 1 to 5.

class Like(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='likes')
    course = models.ForeignKey("Course", on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('author', 'course') ### To ensure a user can like a course only once.    

class Rating(models.Model):
    course = models.ForeignKey("Course", on_delete=models.CASCADE, related_name="ratings")
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="course_ratings")
    score = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        unique_together = ("user", "course")

class CircleBadge(models.Model):
    BADGE_TYPE_CHOICES = [
        ('circle_complete', 'Circle Complete'),
        ('first_milestone', 'First Milestone'),
        ('all_milestones', 'All Milestones Complete'),
        ('helpful_contributor', 'Helpful Contributor'),
        ('perfect_attendance', 'Perfect Attendance'),
    ]
    
    badge_type = models.CharField(
        max_length=50,
        choices=BADGE_TYPE_CHOICES
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='circle_badges'
    )
    circle = models.ForeignKey(
        'Course',
        on_delete=models.CASCADE,
        related_name='badges_earned'
    )
    earned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-earned_at'] # Show newest first
        unique_together = ('user', 'circle', 'badge_type')
    
    def __str__(self):
        return f"{self.user.username} - {self.get_badge_type_display()} ({self.circle.title})"
    
    @property
    def badge_icon(self):
        """Return emoji icon for badge type"""
        icons = {
            'circle_complete': '🏆',
            'first_milestone': '🌱',
            'all_milestones': '⭐',
            'helpful_contributor': '💬',
            'perfect_attendance': '📅',
        }
        return icons.get(self.badge_type, '🎖️')