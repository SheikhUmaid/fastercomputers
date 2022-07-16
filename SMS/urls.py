from django.urls import path
from SMS import views
urlpatterns = [
    path('',views.getStudent)
]
