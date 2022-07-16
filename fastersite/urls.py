from django.urls import path
from fastersite import views



urlpatterns = [
    path('',views.index,name='index'),
    path('contactus/',views.contact,name='contact'),
    path('courses/',views.courses,name='courses'),
]
