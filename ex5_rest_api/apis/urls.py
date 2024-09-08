from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views.v1.school import SchoolViewSet
from .views.v1.classroom import ClassroomViewSet
from .views.v1.teacher import TeacherViewSet
from .views.v1.student import StudentViewSet


router = DefaultRouter()
router.register("school", SchoolViewSet)
router.register("classroom", ClassroomViewSet)
router.register("teacher", TeacherViewSet)
router.register("student", StudentViewSet)


api_v1_urls = (router.urls, 'v1')

urlpatterns = [
    path('v1/', include(api_v1_urls))
]
