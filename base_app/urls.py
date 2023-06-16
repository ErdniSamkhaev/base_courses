from . import views
from django.urls import path

urlpatterns = [
    path('', views.show_all_courses),
    path('course/<slug:slug_course>', views.show_one_course, name='course_detail'),
]