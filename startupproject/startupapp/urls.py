from django.urls import path
from startupapp import views


urlpatterns = [
    path('',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('courses/',views.courses,name="courses"),
    path('course/<id>/',views.course,name="course"),
    path('enroll/',views.enroll,name="enroll"),
    path('candidateprofile/',views.candidateprofile,name="candidateprofile"),
    path('candidateupdate/<id>/',views.candidateupdate,name="candidateupdate"),
    path('attendance/',views.attendance,name="attendance"),
    path('search/',views.search,name="search"),
    
    path('training-courses/', views.training_courses, name='training_courses'),
    path('freelancing/', views.freelancing, name='freelancing'),
    path('onsite-training/', views.onsite_training, name='onsite_training'),
    path('online-offline-training/', views.online_offline_training, name='online_offline_training'),
    
    
    path('add_freelancer/', views.add_freelancer, name='add_freelancer'),
    path('freelancer-added/', views.freelancer_added, name='freelancer-added'),
    
    # path('freelancer/<int:freelancer_id>/', views.freelancer_profile, name='freelancer_profile'),
    
    path('client-opportunities/', views.client_opportunities, name='client_opportunities'),
    # path('add_client_opportunity/', views.add_client_opportunity, name='add_client_opportunity'),

]
