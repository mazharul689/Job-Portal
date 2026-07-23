from django.urls import path
from .views import *
urlpatterns = [
    path('',loginPage,name='login'),
    path('register/',registerPage,name='register'),
    path('logout/',logoutPage,name='logout'),
    path('changepassword/',passChangePage,name='changepassword'),
    path('recruiter/',recruiterprofilePage,name='recruiter'),
    path('jobseeker/',jobseekerprofilePage,name='jobseeker'),
    path('addskill/',addSkillsPage,name='addskill'),
    path('jobpost/',jobpostPage,name='jobpost'),
    path('editjobpost/<int:id>',editjobpostPage,name='editjobpost'),
    path('deletejob/<int:id>',deletejobpostPage,name='deletejob'),
    path('jobs/',joblistPage,name='jobs'),
    path('appliedjobs/',appliedjobPage,name='appliedjobs'),
    path('dashboard/',dashboardPage,name='dashboard'),
    path('apply/<int:id>',applyjobPage,name='apply'),
    path('shortlisted/<int:id>',applicationstatusShortlistedPage,name='shortlisted'),
    path('pending/<int:id>',applicationstatusPendingPage,name='pending'),
    path('rejected/<int:id>',applicationstatusRejectedPage,name='rejected'),
    path('applicationmanagement/',appliedjobmanagementPage,name='applicationmanagement'),
    
]
