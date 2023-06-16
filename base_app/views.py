from django.shortcuts import render, get_object_or_404


# Create your views here.
from .models import base
from django.db.models import F, Sum, Max, Min, Count, Avg

def show_all_courses(request):
    courses = base.objects.order_by(F('year').asc(nulls_first=True), 'rating')
    agg = courses.aggregate(Avg('budget'), Max('rating'), Min('rating'), Count('id'))
    return render(request, 'base_app/all_courses.html', {
        'courses': courses,
        'agg': agg,
    })


def show_one_course(request, slug_course=str):
    course = get_object_or_404(base, slug=slug_course)
    return render(request, 'base_app/one_course.html', {
        'course': course
    })