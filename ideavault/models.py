from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.CharField(max_length=255)
    
class Contributor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    is_mentor = models.BooleanField(default=False)
    is_sponsor = models.BooleanField(default=False)

class Project(models.Model):
    name = models.CharField(max_length=255)
    overview = models.TextField()
    images = models.ImageField(upload_to='project_images/', blank=True, null=True)
    necessary_links = models.URLField()
    funds_needed = models.DecimalField(max_digits=10, decimal_places=2)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='created_projects')
    # collaborators = models.ManyToManyField(UserProfile, related_name='collaborated_projects', blank=True)
    mentors = models.ManyToManyField(Contributor, related_name='mentored_projects', blank=True)
    sponsors = models.ManyToManyField(Contributor, related_name='sponsored_projects', blank=True)

# class CollaborationRequest(models.Model):
#     student = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='collaboration_requests')
#     project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='collaboration_requests')
#     message = models.TextField()
#     is_accepted = models.BooleanField(default=False)
