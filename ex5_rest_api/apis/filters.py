import django_filters
from .models import (
    School, Classroom, Teacher, Student
)

class SchoolFilter(django_filters.FilterSet):
    full_name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = School
        fields = ['full_name']

class ClassroomFilter(django_filters.FilterSet):
    school = django_filters.ModelChoiceFilter(queryset=School.objects.all())

    class Meta:
        model = Classroom
        fields = ['school']

class TeacherFilter(django_filters.FilterSet):
    school = django_filters.ModelChoiceFilter(queryset=School.objects.all())
    classroom = django_filters.ModelChoiceFilter(queryset=Classroom.objects.all())
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    gender = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Teacher
        fields = ['school', 'classroom', 'first_name', 'last_name', 'gender']

class StudentFilter(django_filters.FilterSet):
    school = django_filters.ModelChoiceFilter(queryset=School.objects.all())
    classroom = django_filters.ModelChoiceFilter(queryset=Classroom.objects.all())
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    gender = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Student
        fields = ['school', 'classroom', 'first_name', 'last_name', 'gender']
