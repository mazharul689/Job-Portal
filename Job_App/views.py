from django.shortcuts import render, redirect
from django.contrib.auth import login,logout
from django.contrib import messages
from .models import *
from .forms import *

def registerPage(req):
    if req.method == 'POST':
        form = RegisterForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req, 'Registration Completed')
            return redirect('login')
    form = RegisterForm()
    data = {
        'form': form,
        'title': 'Register Form',
        'btn': 'Register'
    }
    return render(req, 'pages/authform.html',data)


def loginPage(req):
    if req.method == 'POST':
        form = AuthForm(req,req.POST)
        if form.is_valid():
            user = form.get_user()
            login(req,user)
            messages.success(req, 'Login Successfull')
            return redirect('dashboard')
    form = AuthForm()
    data = {
        'form': form,
        'title': 'Login Form',
        'btn': 'Login'
    }
    return render(req, 'pages/authform.html',data)

def recruiterprofilePage(req):
    try:
        user = RecruiterProfileModel.objects.get(user = req.user)
    except RecruiterProfileModel.DoesNotExist:
        user = RecruiterProfileModel.objects.create(user = req.user)
    if req.method == 'POST':
        form = RPForm(req.POST, instance = user)
        if form.is_valid():
            form.save()
            messages.success(req, 'Recruiter Profile Updated')
            return redirect('dashboard')
    form = RPForm(instance = user)
    data = {
        'form': form,
        'title': 'Recruiter Profile Update Form',
        'btn': 'Update'
    }
    return render(req, 'pages/baseform.html',data)


def jobseekerprofilePage(req):
    try:
        user = JobseekerProfileModel.objects.get(user = req.user)
    except JobseekerProfileModel.DoesNotExist:
        user = JobseekerProfileModel.objects.create(user = req.user)
    if req.method == 'POST':
        form = JSPForm(req.POST, req.FILES, instance = user)
        if form.is_valid():
            form.save()
            messages.success(req, 'Jobseeker Profile Updated')
            return redirect('dashboard')
    form = JSPForm(instance = user)
    data = {
        'form': form,
        'title': 'Jobseeker Profile Update Form',
        'btn': 'Update'
    }
    return render(req, 'pages/baseform.html',data)


def jobpostPage(req):
    if req.user.user_type == 'recruiter':
        try:
            user = RecruiterProfileModel.objects.get(user = req.user)
        except RecruiterProfileModel.DoesNotExist:
            messages.warning(req, 'Update profile first!')
            return redirect('recruiter')
        if req.method == 'POST':
            form = JobpostForm(req.POST, req.FILES)
            if form.is_valid():
                data = form.save(commit=False)
                data.user = user
                data.save()
                form.save_m2m()
                messages.success(req, 'Job posted successfully')
                return redirect('dashboard')
        form = JobpostForm()
        data = {
            'form': form,
            'title': 'Job Post Form',
            'btn': 'Save'
        }
    return render(req, 'pages/baseform.html',data)

def editjobpostPage(req, id):
    if req.user.user_type == 'recruiter':
        job = JobpostModel.objects.get(id = id)
        if req.method == 'POST':
            form = JobpostForm(req.POST, req.FILES, instance = job)
            if form.is_valid():
                form.save()
                messages.success(req, 'Job post updated successfully')
                return redirect('dashboard')
        form = JobpostForm(instance = job)
        data = {
            'form': form,
            'title': 'Edit Job Post',
            'btn': 'Update'
        }
    return render(req, 'pages/baseform.html',data)

def deletejobpostPage(req,id):
    job = JobpostModel.objects.get(id = id)
    job.delete()
    return redirect('jobs')

def dashboardPage(req):
    if req.user.user_type == 'recruiter':
        try:
            recruiter = RecruiterProfileModel.objects.get(user = req.user)
        except:
            messages.warning(req,'Profile Update First')
            return redirect('recruiter')
        jobs = JobpostModel.objects.filter(user = recruiter)
        job_len = JobpostModel.objects.filter(user = recruiter).__len__ or 0
        appliedjobs = ApplyModel.objects.filter(recruiter = recruiter).__len__ or 0
        jobid = None
        totalpending = ApplyModel.objects.filter(status = 'shortlisted').__len__ or 0
        totalshortlisted = ApplyModel.objects.filter(status = 'pending').__len__ or 0
        totalrejected = ApplyModel.objects.filter(status = 'rejected').__len__ or 0
    elif req.user.user_type == 'jobseeker':
        try:
            seeker = JobseekerProfileModel.objects.get(user = req.user)
        except:
            messages.warning(req,'Profile Update First')
            return redirect('jobseeker')
        jobs = JobpostModel.objects.all()
        jobid = ApplyModel.objects.filter(user = seeker).values_list("job_id", flat=True)
        appliedjobs = 0
        job_len = 0
        totalpending = 0
        totalshortlisted = 0
        totalrejected = 0
    con = {
        'jobs': jobs,
        'appliedjobs': appliedjobs,
        'job_len': job_len,
        'jobid': jobid,
        'totalpending': totalpending,
        'totalshortlisted': totalshortlisted,
        'totalrejected': totalrejected
    }
    return render(req, 'pages/dashboard.html',con)

def applyjobPage(req,id):
    
    if req.user.user_type == 'jobseeker':
        try:
            user = JobseekerProfileModel.objects.get(user = req.user)
        except JobseekerProfileModel.DoesNotExist:
            messages.warning(req, 'Update profile first!')
            return redirect('jobseeker')
        job = JobpostModel.objects.get(id = id)
        ApplyModel.objects.create(
            user = user,
            recruiter = job.user,
            job = job,
            status = 'pending'
        )
        messages.success(req,'Applid in the job')
    return redirect('jobs')


def joblistPage(req):
    if req.user.user_type == 'recruiter':
        try:
            recruiter = RecruiterProfileModel.objects.get(user = req.user)
            jobid = None
        except:
            messages.warning(req,'Profile Update First')
            return redirect('recruiter')
        jobs = JobpostModel.objects.filter(user = recruiter)
        skills = None
    elif req.user.user_type == 'jobseeker':
        seeker = JobseekerProfileModel.objects.get(user = req.user)
        if seeker:
            skills = seeker.skill_set.all() or 'No Skill Added'
            if skills != 'No Skill Added':
                jobs = JobpostModel.objects.filter(skill_set__in = skills).distinct()
                jobid = list(ApplyModel.objects.filter(user = seeker).values_list("job_id", flat=True)) or None
            else:
                jobs = None
                jobid = None
        
    con = {
        'jobs': jobs,
        'skills': skills,
        'jobid': jobid
    }
    return render(req,'pages/joblist.html',con)



def appliedjobPage(req):
    if req.user.user_type == 'jobseeker':
        user = JobseekerProfileModel.objects.get(user = req.user)
        allappliedjobs = ApplyModel.objects.filter(user = user)
        con ={
            'allappliedjobs': allappliedjobs
        }
        return render(req, 'pages/appliedjoblist.html', con)
    else:
        return redirect('dashboard')
    
def appliedjobmanagementPage(req):
    if req.user.user_type == 'recruiter':
        user = RecruiterProfileModel.objects.get(user = req.user)
        appliedjobs = ApplyModel.objects.filter(recruiter = user)
        con = {
            'appliedjobs': appliedjobs
        }
    return render(req,'pages/applicationmanagement.html',con)

def applicationstatusShortlistedPage(req,id):
    if req.user.user_type == 'recruiter':
        application = ApplyModel.objects.get(id=id)
        application.status = 'shortlisted'
        application.save()
        messages.success(req,'Status Updated')
    return redirect('applicationmanagement')

def applicationstatusPendingPage(req,id):
    if req.user.user_type == 'recruiter':
        application = ApplyModel.objects.get(id=id)
        application.status = 'pending'
        application.save()
        messages.success(req,'Status Updated')
    return redirect('applicationmanagement')

def applicationstatusRejectedPage(req,id):
    if req.user.user_type == 'recruiter':
        application = ApplyModel.objects.get(id=id)
        application.status = 'rejected'
        application.save()
        messages.success(req,'Status Updated')
    return redirect('applicationmanagement')

def logoutPage(req):
    logout(req)
    return redirect('login')

def addSkillsPage(req):
    if req.method == 'POST':
        form = SkillsForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req, 'Skill Added')
    form = SkillsForm()
    data = {
        'form': form,
        'title': 'Add Skill Form',
        'btn': 'Add'
    }
    return render(req, 'pages/baseform.html',data)