# from django.db import models
# from django.contrib.auth import get_user_model 

# class Course(models.Model):
#     title = models.CharField(max_length=255)
#     course_content = models.TextField()
#     CATEGORY_CHOICES = [
#         ('math', 'Mathematics'),
#         ('science', 'Science'),
#         ('history', 'History'),
#         ('art', 'Art'),
#         ('technology', 'Technology'),
#     ]
#     category = models.CharField(max_length=50, choices=CATEGORY_CHOICES , default='math')
#     owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='courses')
#     created_at = models.DateTimeField(auto_now_add=True)
#     image=models.URLField(blank=True, null=True)
#     is_open = models.BooleanField(default=True)
#     date_created = models.DateTimeField(auto_now_add=True)
#     owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='owned_courses')

#     def __str__(self):
#         return self.title

# class Comment(models.Model):
#     content = models.TextField()
#     course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='comments')
#     author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='course_comments')
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'Comment by {self.author} on {self.course}'
    
#     class Like(models.Model):
#         user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comment_likes')
#         comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='likes')
#         created_at = models.DateTimeField(auto_now_add=True)    
