from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    TYPE = [
        ('jobseeker','jobseeker'),
        ('recruiter','recruiter')
    ]
    user_type = models.CharField(choices=TYPE, max_length=200,null=True)
    def __str__(self):
        return self.username

class RecruiterProfileModel(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True)
    company_name = models.CharField(max_length=200,null=True)
    address = models.CharField(max_length=200,null=True)
    contact = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.name
    
class SkillsModel(models.Model):
    name = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name or 'No Skill'
    
class JobseekerProfileModel(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True)
    contact = models.CharField(max_length=200,null=True)
    resume = models.FileField(upload_to='media/resumes', null=True)
    address = models.CharField(max_length=200,null=True)
    skill_set = models.ManyToManyField(SkillsModel, blank=True)
    
    def __str__(self):
        return self.name
    

    
class JobpostModel(models.Model):
    user = models.ForeignKey(RecruiterProfileModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=200,null=True)
    type = models.CharField(max_length=200,null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='media/jobs', null=True)
    skill_set = models.ManyToManyField(SkillsModel, blank=True)
    
    def __str__(self):
        return self.title
    
class ApplyModel(models.Model):
    _STATUS = [
        ('pending','pending'),
        ('shortlisted','shortlisted'),
        ('rejected','rejected'),
    ]
    user = models.ForeignKey(JobseekerProfileModel, on_delete=models.CASCADE)
    recruiter = models.ForeignKey(RecruiterProfileModel, on_delete=models.CASCADE)
    job = models.ForeignKey(JobpostModel, on_delete=models.CASCADE)
    status = models.CharField(choices=_STATUS, default='pending')
    
    def __str__(self):
        return self.status
    
